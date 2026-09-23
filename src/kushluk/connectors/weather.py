from __future__ import annotations

from datetime import datetime

import httpx

from kushluk.models import PracticalItem, SourceRef


class OpenMeteoWeatherConnector:
    endpoint = "https://api.open-meteo.com/v1/forecast"

    def __init__(
        self, latitude: float, longitude: float, timezone: str, location_name: str
    ) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.location_name = location_name

    def fetch(self) -> list[PracticalItem]:
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "timezone": self.timezone,
            "current": "temperature_2m,apparent_temperature,weather_code",
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
            "forecast_days": 1,
        }
        with httpx.Client(timeout=12.0, follow_redirects=True) as client:
            response = client.get(self.endpoint, params=params)
            response.raise_for_status()
            payload = response.json()

        current = payload.get("current", {})
        daily = payload.get("daily", {})
        max_temp = _first(daily.get("temperature_2m_max"))
        min_temp = _first(daily.get("temperature_2m_min"))
        rain = _first(daily.get("precipitation_probability_max"))
        temp = current.get("temperature_2m")
        apparent = current.get("apparent_temperature")

        detail_parts = []
        if max_temp is not None and min_temp is not None:
            detail_parts.append(f"{min_temp:.0f}–{max_temp:.0f} °C")
        if rain is not None:
            detail_parts.append(f"rain up to {rain:.0f}%")
        if apparent is not None:
            detail_parts.append(f"feels {apparent:.0f} °C")

        source = SourceRef(
            kind="weather",
            name="Open-Meteo",
            url="https://open-meteo.com/",
            retrieved_at=datetime.now().astimezone().isoformat(timespec="seconds"),
        )
        value = f"{temp:.0f} °C" if isinstance(temp, (int, float)) else "Weather available"
        return [
            PracticalItem(
                label=self.location_name,
                value=value,
                detail=" · ".join(detail_parts) or None,
                source=source,
            )
        ]


def _first(value):
    if isinstance(value, list) and value:
        return value[0]
    return None
