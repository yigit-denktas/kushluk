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
    calendar_fixture: Path = Path("fixtures/calendar.json")
    printer: str | None = None

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
            calendar_fixture=Path(
                os.getenv("KUSHLUK_CALENDAR_FIXTURE", "fixtures/calendar.json")
            ),
            printer=os.getenv("KUSHLUK_PRINTER") or None,
        )
