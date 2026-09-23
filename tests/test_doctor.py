from kushluk.config import Settings
from kushluk.doctor import core_ready, run_doctor


def test_doctor_core_is_ready_with_fixture(tmp_path):
    fixture = tmp_path / "calendar.json"
    fixture.write_text('{"events": []}', encoding="utf-8")
    settings = Settings(
        output_dir=tmp_path / "output",
        archive_dir=tmp_path / "archive",
        calendar_fixture=fixture,
    )
    checks = run_doctor(settings)
    assert core_ready(checks)
    names = {check.name for check in checks}
    assert {"python", "output", "archive", "calendar", "pdf", "printer", "email"} <= names
