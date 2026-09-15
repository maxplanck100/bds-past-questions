#!/usr/bin/env python3
"""
split_pdf.py
------------
Splits a single multi-subject past-question PDF into one PDF per subject,
using page ranges you define in a config file. Built for the
bds-past-questions repo layout: reads one combined scan, writes
raw-pdfs/year-N/<subject>.pdf files ready for the OCR extraction step.

Usage:
    python split_pdf.py --input all_subjects.pdf --config ranges.json --output-dir raw-pdfs/year-2

ranges.json format (1-indexed, inclusive page numbers, as seen in a PDF viewer):
{
    "anatomy":      [1, 6],
    "biochemistry": [7, 18],
    "microbiology": [19, 29],
    "pathology":    [30, 41],
    "pharmacology": [42, 55],
    "physiology":   [56, 68],
    "mixed_2017-22":   [69, 83],
}

If you don't know the page ranges yet, run with --inspect to print a
page-count summary first, then build ranges.json from that.
"""

import argparse
import json
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def inspect(input_path: Path) -> None:
    reader = PdfReader(str(input_path))
    print(f"'{input_path.name}' has {len(reader.pages)} pages.")
    print("Open it in a viewer, note where each subject starts/ends, "
          "then write those into a ranges.json (see --help for format).")


def load_ranges(config_path: Path) -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        ranges = json.load(f)

    if not ranges:
        raise ValueError("Config file is empty.")

    for subject, pages in ranges.items():
        if (not isinstance(pages, list) or len(pages) != 2
                or pages[0] < 1 or pages[1] < pages[0]):
            raise ValueError(
                f"Invalid range for '{subject}': {pages}. "
                "Expected [start, end], 1-indexed, start <= end."
            )
    return ranges


def split_pdf(input_path: Path, ranges: dict, output_dir: Path) -> None:
    reader = PdfReader(str(input_path))
    total_pages = len(reader.pages)
    output_dir.mkdir(parents=True, exist_ok=True)

    for subject, (start, end) in ranges.items():
        if end > total_pages:
            print(f"[WARN] '{subject}' range ends at page {end}, "
                  f"but PDF only has {total_pages} pages. Skipping.")
            continue

        writer = PdfWriter()
        for page_num in range(start - 1, end):  # convert to 0-indexed
            writer.add_page(reader.pages[page_num])

        out_path = output_dir / f"{subject}.pdf"
        with open(out_path, "wb") as f:
            writer.write(f)

        print(f"[OK] {subject}: pages {start}-{end} -> {out_path}")

    print(f"\nDone. {len(ranges)} subject PDFs written to '{output_dir}'.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Split a combined past-question PDF into per-subject PDFs."
    )
    parser.add_argument("--input", required=True, type=Path,
                         help="Path to the combined multi-subject PDF.")
    parser.add_argument("--config", type=Path,
                         help="Path to ranges.json (subject -> [start, end] pages).")
    parser.add_argument("--output-dir", type=Path,
                         help="Directory to write split PDFs into "
                              "(e.g. raw-pdfs/year-2).")
    parser.add_argument("--inspect", action="store_true",
                         help="Just print page count, don't split anything.")

    args = parser.parse_args()

    if not args.input.exists():
        sys.exit(f"Input file not found: {args.input}")

    if args.inspect:
        inspect(args.input)
        return

    if not args.config or not args.output_dir:
        sys.exit("--config and --output-dir are required unless using --inspect.")

    if not args.config.exists():
        sys.exit(f"Config file not found: {args.config}")

    try:
        ranges = load_ranges(args.config)
    except (json.JSONDecodeError, ValueError) as e:
        sys.exit(f"Config error: {e}")

    split_pdf(args.input, ranges, args.output_dir)


if __name__ == "__main__":
    main()
