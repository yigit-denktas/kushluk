from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class PrintResult:
    attempted: bool
    success: bool
    detail: str


def print_pdf(pdf_path: Path, printer: str | None = None, *, execute: bool = False) -> PrintResult:
    if not execute:
        return PrintResult(False, True, "Print skipped (dry-run). Use --print to submit the job.")
    if not pdf_path.exists():
        return PrintResult(True, False, f"PDF not found: {pdf_path}")
    lp = shutil.which("lp")
    if not lp:
        return PrintResult(True, False, "CUPS 'lp' command is not available.")
    command = [lp]
    if printer:
        command += ["-d", printer]
    command += ["-o", "media=A4", str(pdf_path)]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode == 0:
        return PrintResult(True, True, completed.stdout.strip() or "Print job submitted.")
    return PrintResult(True, False, completed.stderr.strip() or "Print submission failed.")
