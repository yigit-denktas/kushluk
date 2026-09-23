from datetime import date

from kushluk.connectors.calendar_ics import ICSCalendarConnector


def test_ics_connector_reads_target_day(tmp_path):
    calendar = tmp_path / "calendar.ics"
    calendar.write_text(
        """BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
UID:one
DTSTART;TZID=Europe/Berlin:20260923T093000
SUMMARY:Morning meeting
LOCATION:Office
END:VEVENT
BEGIN:VEVENT
UID:two
DTSTART;VALUE=DATE:20260924
SUMMARY:Tomorrow
END:VEVENT
END:VCALENDAR
""",
        encoding="utf-8",
    )
    items = ICSCalendarConnector(
        str(calendar), date(2026, 9, 23), "Europe/Berlin"
    ).fetch()
    assert len(items) == 1
    assert items[0].label == "09:30"
    assert items[0].value == "Morning meeting"
    assert items[0].detail == "Office"
