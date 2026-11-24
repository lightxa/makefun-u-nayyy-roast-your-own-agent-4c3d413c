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


def error_message(problem: str, detail: str) -> str:
    """Build one clear, single-line error message for a bad entry."""
    return f"invalid entry: {problem} ({detail})"


def explain_length(line: str) -> str:
    """State the entry length in words a human can act on."""
    words = len(line.split())
    return f"{len(line)} characters, {words} words"


def validate(line: str) -> None:
    """Guard the kit contract: 1 to 200 characters, a single line."""
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")


validate(ROAST)


def verify_written(path: Path, expected: str) -> None:
    """Read the file back and re-validate what was actually written."""
    written = path.read_text(encoding="utf-8")
    if written != expected:
        raise ValueError(
            error_message(
                "written text differs from roast", explain_length(written)
            )
        )
    validate(written)


def main() -> None:
    """Write the roast to entry.txt, one line and nothing else."""
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline, so the file holds exactly the roast: 1 to 200
    # characters of UTF-8 text, single line, no extra content.
    target = output_dir / "entry.txt"
    target.write_text(ROAST, encoding="utf-8")
    verify_written(target, ROAST)


if __name__ == "__main__":
    main()
