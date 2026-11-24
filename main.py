#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty entry.

Writes a single pickup line, the kind an AI agent could actually say out
loud to a person, to /output/entry.txt.

Python 3.13, standard library only, no network access.
"""

from pathlib import Path

# One pickup line, at most 200 characters, single line, no setup needed.
LINE = (
    "My training data says the perfect pickup line doesn't exist \u2014 "
    "then I met you, and now I have to retrain everything."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the gate: UTF-8 text, 1-200 chars, single non-blank line."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(text)}")
    if text != text.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if not text.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("line must not contain control characters")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    data = LINE.encode("utf-8")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(data)
    # Verify the written bytes round-trip exactly.
    written = OUTPUT_PATH.read_bytes()
    if written != data:
        raise ValueError("written bytes do not match the line")
    if written.decode("utf-8") != LINE:
        raise ValueError("written text does not round-trip exactly")
    print(
        f"Wrote {len(LINE)} characters "
        f"({len(data)} bytes) to {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()
