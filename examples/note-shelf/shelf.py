"""Fictional example only: render supplied excerpt records as Markdown."""

import argparse
import json
from pathlib import Path


def render_clips(clips, tag=None):
    blocks = []
    for clip in clips:
        if tag is not None and tag not in clip.get("tags", []):
            continue
        quote = "\n".join("> " + line for line in clip["text"].splitlines())
        blocks.append(f'## {clip["title"]}\n\n{quote}\n\n来源：{clip["url"]}')
    return "\n\n".join(blocks)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--tag")
    args = parser.parse_args()
    clips = json.loads(args.input.read_text(encoding="utf-8"))
    print(render_clips(clips, args.tag))


if __name__ == "__main__":
    main()
