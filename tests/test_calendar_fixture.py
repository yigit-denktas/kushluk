import json

from kushluk.connectors.calendar_fixture import CalendarFixtureConnector


def test_calendar_fixture(tmp_path):
    path = tmp_path / "calendar.json"
    path.write_text(json.dumps({"events": [{"time": "10:00", "title": "Test"}]}))
    items = CalendarFixtureConnector(path).fetch()
    assert len(items) == 1
    assert items[0].value == "Test"
