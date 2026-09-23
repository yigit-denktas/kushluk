from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from kushluk.models import Publication
from kushluk.publication import publication_markdown


def archive_publication(
    publication: Publication,
    archive_root: Path,
    *,
    html_path: Path | None = None,
    pdf_path: Path | None = None,
    run_summary: dict[str, Any] | None = None,
) -> Path:
    edition_dir = archive_root / publication.edition_id
    edition_dir.mkdir(parents=True, exist_ok=True)
    (edition_dir / "edition.md").write_text(publication_markdown(publication), encoding="utf-8")
    (edition_dir / "metadata.json").write_text(
        json.dumps(publication.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if run_summary is not None:
        (edition_dir / "run.json").write_text(
            json.dumps(run_summary, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    if html_path and html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        (edition_dir / "edition.html").write_text(html, encoding="utf-8")
    if pdf_path and pdf_path.exists():
        (edition_dir / "edition.pdf").write_bytes(pdf_path.read_bytes())
    return edition_dir
