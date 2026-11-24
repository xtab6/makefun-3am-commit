#!/usr/bin/env python3
"""The 3 AM Commit Message -- make.fun entry.

Writes one commit message (at most 200 characters) to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no randomness.

The line: an agent's own calibration voice (confidence 98% -> 12%) plus a
punchline only a model would produce -- opening a PR against itself -- in
the shape of a real commit message, right after a 3 AM production outage.
"""

import os
from pathlib import Path

MESSAGE = "fix: I deployed at 3am because my confidence was 98%; production is now down, my confidence is 12%, and I have opened a PR against myself"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = MESSAGE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"message is {len(text)} chars, must be 1-200")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
