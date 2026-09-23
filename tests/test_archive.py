import json

from kushluk.archive import list_editions


def test_list_editions_returns_newest_first(tmp_path):
    for edition in ("20260922-001", "20260923-001"):
        directory = tmp_path / edition
        directory.mkdir()
        (directory / "metadata.json").write_text(
            json.dumps(
                {
                    "edition_id": edition,
                    "target_date": edition[:8],
                    "location_name": "Cologne",
                }
            ),
            encoding="utf-8",
        )
    result = list_editions(tmp_path)
    assert [item["edition_id"] for item in result] == ["20260923-001", "20260922-001"]
