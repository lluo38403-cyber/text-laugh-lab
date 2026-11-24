"""One-Liner Laugh Lab — make.fun text entry.

Writes one short funny line, the excuse a robot vacuum gives
after eating a sock, to /output/entry.txt
(or $ENTRY_OUTPUT_DIR/entry.txt).
"""

import os
from pathlib import Path

ENTRY = "I did not eat your sock. I simply relocated it to a secure location under the couch, where it now lives rent-free."
MAX_CHARS = 200


def main():
    assert ENTRY.strip(), "entry must not be blank"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    assert back == ENTRY, "round-trip mismatch"
    print(f"wrote {len(ENTRY)} chars to {target}")


if __name__ == "__main__":
    main()
