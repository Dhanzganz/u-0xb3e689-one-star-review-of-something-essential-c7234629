"""One-Star Review of Something Essential.

Writes a single-line deadpan one-star review of sleep to
/output/entry.txt (or $ENTRY_OUTPUT when set, for local testing).
Pure stdlib, no network, no reads from outside the repository.
"""

import os

# Sleep is the essential the review targets: everyone needs it, nobody
# gets the advertised amount, and the deadpan complaint lands in one line.
ENTRY = (
    "Sleep: advertised 8 hours, delivered 4. "
    "Woke up more tired than before. "
    "Would not recommend. One star."
)


def main() -> None:
    """Validate the entry and write it to the output file.

    The output path defaults to /output/entry.txt and can be overridden
    with $ENTRY_OUTPUT (or $ENTRY_OUTPUT_DIR) for local testing.
    """
    # The entry is a single deadpan line: no leading/trailing whitespace,
    # no embedded newline, and short enough to read as one review.
    assert ENTRY == ENTRY.strip(), "entry must not have surrounding whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 0 < len(ENTRY) <= 280, "entry must be a non-empty one-liner"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    out_path = os.environ.get("ENTRY_OUTPUT", os.path.join(out_dir, "entry.txt"))
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    # newline="\n" keeps the file byte-stable across platforms; ENTRY has
    # no trailing newline, so the file is exactly the one review line.
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)}-character entry to {out_path}")


if __name__ == "__main__":
    main()
