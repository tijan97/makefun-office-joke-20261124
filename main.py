"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

Writes a single one-line joke about office life to /output/entry.txt.
Stdlib only. The joke is a setup with a surprising punchline built on a
specific, recognisable office detail: the printer that only jams when
the document actually matters.
"""

import os

ENTRY = (
    "Our office printer only jams on urgent documents, "
    "so IT officially lists it as our most reliable deadline detector."
)

MAX_CHARS = 200


def validate_entry(text: str) -> None:
    """Enforce the bounty gate: UTF-8 text, 1-200 chars, one line,
    not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
