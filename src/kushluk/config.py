from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Settings:
    home_name: str = "Cologne"
    latitude: float = 50.9384
    longitude: float = 6.9603
    timezone: str = "Europe/Berlin"
    rss_urls: tuple[str, ...] = ("https://hnrss.org/frontpage",)
    archive_dir: Path = Path("archive")
    output_dir: Path = Path("output")
    calendar_ics: str | None = None
    calendar_fixture: Path = Path("fixtures/calendar.json")
    printer: str | None = None
    smtp_host: str | None = None
    smtp_port: int = 587
    smtp_username: str | None = None
    smtp_password: str | None = None
    smtp_from: str | None = None
    email_to: str | None = None
    smtp_starttls: bool = True

    @property
    def email_configured(self) -> bool:
        return bool(self.smtp_host and self.smtp_from and self.email_to)

    @classmethod
    def from_env(cls) -> "Settings":
        rss = tuple(
            item.strip()
            for item in os.getenv("KUSHLUK_RSS_URLS", "https://hnrss.org/frontpage").split(",")
            if item.strip()
        )
        return cls(
            home_name=os.getenv("KUSHLUK_HOME_NAME", "Cologne"),
            latitude=float(os.getenv("KUSHLUK_LATITUDE", "50.9384")),
            longitude=float(os.getenv("KUSHLUK_LONGITUDE", "6.9603")),
            timezone=os.getenv("KUSHLUK_TIMEZONE", "Europe/Berlin"),
            rss_urls=rss,
            archive_dir=Path(os.getenv("KUSHLUK_ARCHIVE_DIR", "archive")),
            output_dir=Path(os.getenv("KUSHLUK_OUTPUT_DIR", "output")),
            calendar_ics=os.getenv("KUSHLUK_CALENDAR_ICS") or None,
            calendar_fixture=Path(
                os.getenv("KUSHLUK_CALENDAR_FIXTURE", "fixtures/calendar.json")
            ),
            printer=os.getenv("KUSHLUK_PRINTER") or None,
            smtp_host=os.getenv("KUSHLUK_SMTP_HOST") or None,
            smtp_port=int(os.getenv("KUSHLUK_SMTP_PORT", "587")),
            smtp_username=os.getenv("KUSHLUK_SMTP_USERNAME") or None,
            smtp_password=os.getenv("KUSHLUK_SMTP_PASSWORD") or None,
            smtp_from=os.getenv("KUSHLUK_SMTP_FROM") or None,
            email_to=os.getenv("KUSHLUK_EMAIL_TO") or None,
            smtp_starttls=_env_bool("KUSHLUK_SMTP_STARTTLS", True),
        )


def _env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}
