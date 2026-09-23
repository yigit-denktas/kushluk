from __future__ import annotations

import json
from pathlib import Path

from kushluk.models import PracticalItem, SourceRef


class CalendarFixtureConnector:
    def __init__(self, path: Path) -> None:
        self.path = path

    def fetch(self) -> list[PracticalItem]:
        if not self.path.exists():
            return []
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        source = SourceRef(kind="calendar", name="Calendar fixture")
        items: list[PracticalItem] = []
        for event in payload.get("events", []):
            items.append(
                PracticalItem(
                    label=event.get("time", "All day"),
                    value=event.get("title", "Untitled event"),
                    detail=event.get("location"),
                    source=source,
                )
            )
        return items
