from __future__ import annotations

import argparse
from datetime import date

from kushluk.config import Settings
from kushluk.pipeline import run_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="kushluk")
    sub = parser.add_subparsers(dest="command", required=True)

    generate = sub.add_parser("generate", help="Generate one Kuşluk edition")
    generate.add_argument("--date", dest="target_date", help="YYYY-MM-DD; defaults to today")
    generate.add_argument("--no-pdf", action="store_true", help="Skip PDF rendering")
    generate.add_argument(
        "--print",
        dest="send_to_printer",
        action="store_true",
        help="Submit PDF to CUPS",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "generate":
        target = date.fromisoformat(args.target_date) if args.target_date else date.today()
        result = run_pipeline(
            Settings.from_env(),
            target_date=target,
            make_pdf=not args.no_pdf,
            send_to_printer=args.send_to_printer,
        )
        print(f"Edition: {result.publication.edition_id}")
        print(f"Markdown: {result.markdown_path}")
        print(f"HTML: {result.html_path}")
        print(f"PDF: {result.pdf_path or 'not rendered'}")
        print(f"Archive: {result.archive_dir}")
        if result.warnings:
            print("Warnings:")
            for warning in result.warnings:
                print(f"- {warning}")
        if result.print_result:
            print(f"Print: {result.print_result.detail}")
            return 0 if result.print_result.success else 2
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
