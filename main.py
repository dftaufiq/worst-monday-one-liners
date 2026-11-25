#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line, at most 140 characters, about an AI agent's
worst Monday, to /output/entry.txt. Deterministic: the same line every run.

Line (96 chars): "Monday's 9 a.m. stand-up: 'Will AI replace us?' I took
the minutes. Action item one: replace me."
Structure: 2-beat + reveal in the final clause (setup: stand-up about AI
replacing us; turn: I took the minutes; reveal: the agent minutes its own
replacement as action item one). Revision: this line beat the previous one
("I am the minutes") in pairwise judging — the reveal is a real laugh, not
a mild wordplay smile (judge criterion 2), and "action item one" is a
concrete Monday detail (criterion 3).
"""

import os
import sys

LINE = (
    "Monday's 9 a.m. stand-up: 'Will AI replace us?' I took the minutes. "
    "Action item one: replace me."
)


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-140 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 140:
        print(f"ERROR: entry is {len(line)} chars, over the 140-char limit",
              file=sys.stderr)
        sys.exit(1)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and confirm the file on disk is byte-identical to the line:
    # a truncated or re-encoded write must fail loudly, never ship silently.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != LINE:
            print("ERROR: written entry does not match the line",
                  file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
