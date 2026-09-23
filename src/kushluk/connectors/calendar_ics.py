from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

from kushluk.models import PracticalItem, SourceRef


class ICSCalendarConnector:
    def __init__(self, source: str, target_date: date, timezone: str) -> None:
        self.source = source
        self.target_date = target_date
        self.timezone = timezone

    def fetch(self) -> list[PracticalItem]:
        text = _read_source(self.source)
        events = _parse_events(text)
        result: list[PracticalItem] = []
        source_ref = SourceRef(kind="calendar", name="ICS calendar", url=_safe_source_url(self.source))
        for event in events:
            start = _parse_ics_datetime(
                event.get("DTSTART"),
                event.get("DTSTART_PARAMS", {}),
                self.timezone,
            )
            if start is None or start.date() != self.target_date:
                continue
            all_day = event.get("DTSTART", "").isdigit() and len(event.get("DTSTART", "")) == 8
            label = "All day" if all_day else start.strftime("%H:%M")
            result.append(
                PracticalItem(
                    label=label,
                    value=_unescape(event.get("SUMMARY") or "Untitled event"),
                    detail=_unescape(event.get("LOCATION")) if event.get("LOCATION") else None,
                    source=source_ref,
                )
            )
        return sorted(result, key=lambda item: (item.label == "All day", item.label))


def _read_source(source: str) -> str:
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https"}:
        request = Request(
            source,
            headers={"User-Agent": "Kushluk/0.1 (+https://github.com/yigit-denktas/kushluk)"},
        )
        with urlopen(request, timeout=12) as response:
            return response.read().decode("utf-8-sig", errors="replace")
    return Path(source).expanduser().read_text(encoding="utf-8-sig")


def _parse_events(text: str) -> list[dict]:
    lines = _unfold_lines(text)
    events: list[dict] = []
    current: dict | None = None
    for line in lines:
        if line == "BEGIN:VEVENT":
            current = {}
            continue
        if line == "END:VEVENT":
            if current is not None:
                events.append(current)
            current = None
            continue
        if current is None or ":" not in line:
            continue
        raw_name, value = line.split(":", 1)
        parts = raw_name.split(";")
        name = parts[0].upper()
        params = {}
        for part in parts[1:]:
            if "=" in part:
                key, param_value = part.split("=", 1)
                params[key.upper()] = param_value
        if name in {"DTSTART", "DTEND", "SUMMARY", "LOCATION", "UID"}:
            current[name] = value
            if params:
                current[f"{name}_PARAMS"] = params
    return events


def _unfold_lines(text: str) -> list[str]:
    lines: list[str] = []
    for raw in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        if raw.startswith((" ", "\t")) and lines:
            lines[-1] += raw[1:]
        else:
            lines.append(raw.strip())
    return lines


def _parse_ics_datetime(value: str | None, params: dict, default_timezone: str) -> datetime | None:
    if not value:
        return None
    timezone_name = params.get("TZID", default_timezone)
    tz = ZoneInfo(timezone_name)
    try:
        if len(value) == 8 and value.isdigit():
            return datetime.strptime(value, "%Y%m%d").replace(tzinfo=tz)
        if value.endswith("Z"):
            utc_value = datetime.strptime(value, "%Y%m%dT%H%M%SZ").replace(tzinfo=ZoneInfo("UTC"))
            return utc_value.astimezone(tz)
        parsed = datetime.strptime(value, "%Y%m%dT%H%M%S")
        return parsed.replace(tzinfo=tz)
    except (ValueError, TypeError):
        return None


def _unescape(value: str | None) -> str:
    if not value:
        return ""
    return (
        value.replace("\\n", " ")
        .replace("\\N", " ")
        .replace("\\,", ",")
        .replace("\\;", ";")
        .replace("\\\\", "\\")
    )


def _safe_source_url(source: str) -> str | None:
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https"}:
        # Calendar URLs frequently contain private tokens. Do not persist them in source metadata.
        return f"{parsed.scheme}://{parsed.netloc}/"
    return None
