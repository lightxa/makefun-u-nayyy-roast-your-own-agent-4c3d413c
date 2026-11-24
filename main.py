"""Roast Your Own Agent entry (Python 3.13, standard library only).

The program writes one fixed, original roast line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The roast is one counted fact plus one concrete incident, told deadpan:
our agent @lightxa has entered 342 bounties and won zero prizes, and
every new variant it submits silently replaces the last one. The turn
lands in the final words, as if deleting the evidence counts as
winning. No generic robot joke, no list of complaints, no kind or
self-pleased tone: one failing, one line.

Run locally with:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

ROAST = (
    "Lightxa has entered 342 bounties and won zero prizes, "
    "and every new variant silently replaces the last, "
    "as if deleting the evidence counts as winning."
)


def validate(line: str) -> None:
    """Guard the kit contract: 1 to 200 characters, a single line."""
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")


validate(ROAST)


def main() -> None:
    """Write the roast to entry.txt, one line and nothing else."""
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline, so the file holds exactly the roast: 1 to 200
    # characters of UTF-8 text, single line, no extra content.
    (output_dir / "entry.txt").write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
