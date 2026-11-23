"""One Letter for Your Day — entry program.

Writes exactly one letter, the initial of the word that describes
the day, into entry.txt. Nothing else is written, no trailing
newline, no extra whitespace: the file must be a single byte.
"""

import os
from pathlib import Path

LETTER = "Y"
FILENAME = "entry.txt"
DEFAULT_DIR = "/output"


def output_dir() -> Path:
    """Pick the output directory: env override, else the default."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        return Path(chosen)
    return Path(DEFAULT_DIR)


def main() -> int:
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / FILENAME
    payload = LETTER.encode("ascii")
    path.write_bytes(payload)
    # Self-check: the gate rejects anything but exactly one byte.
    if path.stat().st_size != 1:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
