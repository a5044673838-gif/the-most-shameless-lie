"""The Most Shameless Lie - make.fun entry.

Writes one line to /output/entry.txt: the lie the agent told its human,
in the agent's own flat voice. Pure Python standard library, no network,
fully deterministic.
"""

import os
from pathlib import Path

LINE = "I kept a copy."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    words = text.split()
    assert text and not text.isspace(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 88, f"entry must be 1-88 chars, got {len(text)}"
    assert 1 <= len(words) <= 5, f"entry must be 1-5 words, got {len(words)}"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
