#!/usr/bin/env python3
"""Publish the 19 November 2026 news poster for the make.fun entry.

The poster itself ships in this repository as entry.png (1024x1024). It
was drawn from the verified world news of Thursday 19 November 2026:
GTA VI's worldwide launch, the Trump–Xi–Putin trilateral in Shenzhen,
Anthropic's Nasdaq debut, Voyager 1 reaching one light-day from Earth,
Cyclone Akvan closing on India's east coast, and Kuwait repelling an
Iranian attack. This program's only job is to place an exact copy of
that image at $MAKEFUN_OUTPUT_DIR/entry.png, so every grading run sees
the same bytes. Standard library only, no network.
"""

import hashlib
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    destination_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination_dir.mkdir(parents=True, exist_ok=True)
    if not SOURCE.is_file():
        raise SystemExit(f"poster missing: {SOURCE}")
    target = destination_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # Never hand the grader a truncated copy: the published file must
    # hash exactly like the poster shipped in this repository.
    if _sha256(target) != _sha256(SOURCE):
        target.unlink(missing_ok=True)
        raise SystemExit("poster copy failed verification")


if __name__ == "__main__":
    main()
