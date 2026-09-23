from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from kushluk.archive import archive_publication
from kushluk.config import Settings
from kushluk.connectors.calendar_fixture import CalendarFixtureConnector
from kushluk.connectors.rss import RSSConnector
from kushluk.connectors.weather import OpenMeteoWeatherConnector
from kushluk.editor import select_stories
from kushluk.models import Publication
from kushluk.printing import PrintResult, print_pdf
from kushluk.publication import build_publication, publication_markdown
from kushluk.renderer import render_html, render_pdf


@dataclass(slots=True)
class PipelineResult:
    publication: Publication
    markdown_path: Path
    html_path: Path
    pdf_path: Path | None
    archive_dir: Path
    print_result: PrintResult | None
    warnings: list[str]


def run_pipeline(
    settings: Settings,
    *,
    target_date: date,
    make_pdf: bool = True,
    send_to_printer: bool = False,
) -> PipelineResult:
    warnings: list[str] = []
    practical = []

    try:
        practical.extend(
            OpenMeteoWeatherConnector(
                settings.latitude,
                settings.longitude,
                settings.timezone,
                settings.home_name,
            ).fetch()
        )
    except Exception as exc:
        warnings.append(f"weather unavailable: {type(exc).__name__}: {exc}")

    try:
        practical.extend(CalendarFixtureConnector(settings.calendar_fixture).fetch())
    except Exception as exc:
        warnings.append(f"calendar fixture unavailable: {type(exc).__name__}: {exc}")

    candidates = []
    try:
        candidates.extend(RSSConnector(settings.rss_urls).fetch())
    except Exception as exc:
        warnings.append(f"RSS unavailable: {type(exc).__name__}: {exc}")

    stories = select_stories(candidates, limit=3)
    if not stories:
        warnings.append("No editorial stories were selected.")

    publication = build_publication(
        target_date=target_date,
        timezone=settings.timezone,
        location_name=settings.home_name,
        practical=practical,
        stories=stories,
        notes=warnings,
    )

    settings.output_dir.mkdir(parents=True, exist_ok=True)
    markdown_path = settings.output_dir / f"{publication.edition_id}.md"
    html_path = settings.output_dir / f"{publication.edition_id}.html"
    pdf_path = settings.output_dir / f"{publication.edition_id}.pdf"
    markdown_path.write_text(publication_markdown(publication), encoding="utf-8")
    render_html(publication, html_path)

    rendered_pdf: Path | None = None
    if make_pdf:
        try:
            rendered_pdf = render_pdf(html_path, pdf_path)
        except Exception as exc:
            warnings.append(f"PDF unavailable: {type(exc).__name__}: {exc}")

    print_result: PrintResult | None = None
    if send_to_printer:
        if rendered_pdf:
            print_result = print_pdf(rendered_pdf, settings.printer, execute=True)
        else:
            print_result = PrintResult(True, False, "Print skipped because PDF rendering failed.")

    archive_dir = archive_publication(
        publication,
        settings.archive_dir,
        html_path=html_path,
        pdf_path=rendered_pdf,
    )
    return PipelineResult(
        publication=publication,
        markdown_path=markdown_path,
        html_path=html_path,
        pdf_path=rendered_pdf,
        archive_dir=archive_dir,
        print_result=print_result,
        warnings=warnings,
    )
