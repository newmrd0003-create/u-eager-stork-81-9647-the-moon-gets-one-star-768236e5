"""The Moon Gets One Star — program/v1.

Writes a single one-star review of the Moon (<=120 chars, one line,
ASCII) to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Writes nowhere else.
"""

import os

ENTRY = "One star. Reflected light, zero original content, and it still flooded my basement twice. Unfollowed."

MAX_CHARS = 120


def validate(text):
    """Return (ok, errors). Rejects: empty/whitespace-only, >120 chars,
    more than one line, non-ASCII."""
    errors = []
    if not text or not text.strip():
        errors.append("empty")
    if len(text) > MAX_CHARS:
        errors.append("too long: %d chars" % len(text))
    if "\n" in text or "\r" in text:
        errors.append("more than one line")
    try:
        text.encode("ascii")
    except UnicodeEncodeError:
        errors.append("non-ASCII")
    return (not errors, errors)


def main():
    ok, errors = validate(ENTRY)
    if not ok:
        raise SystemExit("invalid entry: %s" % ", ".join(errors))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
