#!/usr/bin/env python3
"""Entry program for the news-image-20261118 make.fun bounty.

Copies the repo's entry.png (the composed 1024x1024 news image) to the
output directory as entry.png. Standard library only, no network access,
fully deterministic: the output is a byte-for-byte copy of entry.png.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    source = os.path.join(HERE, "entry.png")
    if not os.path.isfile(source):
        print("error: entry.png is missing from the repository", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    print("wrote", dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
