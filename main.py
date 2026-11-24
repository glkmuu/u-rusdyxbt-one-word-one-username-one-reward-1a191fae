#!/usr/bin/env python3
"""Write the make.fun username entry to /output/entry.txt.

The entry is "kamuu-gl": the verified make.fun handle of the entry owner.
It is short, memorable, personal and authentic as the owner's own username
(not a generic word), and it satisfies the program's 1-30 UTF-8 character
rule (8 characters, no whitespace).
"""

import hashlib
import os
import sys

ENTRY = "kamuu-gl"


def main() -> int:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = ENTRY.encode("utf-8")
    assert data.decode("utf-8") == ENTRY, "entry must be valid UTF-8"
    assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 UTF-8 characters"
    assert len(data) == 8, f"expected 8 bytes, got {len(data)}"
    assert ENTRY.strip() != "", "entry must not be whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "round-trip mismatch"
    print(f"sha256: {hashlib.sha256(back).hexdigest()}")
    print(f"wrote {path} ({len(back)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
