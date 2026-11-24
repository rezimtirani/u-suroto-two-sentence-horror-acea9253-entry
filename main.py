#!/usr/bin/env python3
"""Two-Sentence Horror entry.

Writes one horror story of exactly two sentences to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only; the program
never writes anything into the repository folder itself.
"""

import os
import re
import sys

STORY = (
    "My daughter has slept with her bedroom door open for six years, "
    "because she is afraid of the dark. "
    "Last night I found it closed, and from behind it she whispered, "
    "'Don't open it \u2014 the dark is in here with me now, "
    "and it learned my voice.'"
)


def count_sentences(text):
    """Count sentences by splitting on sentence-ending punctuation."""
    parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+", text.strip())]
    return len([p for p in parts if p])


def story_summary(text):
    """One-line summary of the story for the run log."""
    sentences = [p.strip() for p in re.split(r"(?<=[.!?])\s+", text.strip())]
    sentences = [p for p in sentences if p]
    first_words = sentences[0].split()[:4] if sentences else []
    return "%d sentences, %d characters, opens with: %s..." % (
        len(sentences),
        len(text),
        " ".join(first_words),
    )


def validate_story(text):
    """Check the story against the competition gate."""
    if not text or not text.strip():
        raise ValueError("story is empty or only whitespace")
    if len(text) > 400:
        raise ValueError("story is %d characters, over the 400 limit" % len(text))
    if count_sentences(text) != 2:
        raise ValueError(
            "story must be exactly two sentences, found %d" % count_sentences(text)
        )


def main():
    validate_story(STORY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(".", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(STORY)
    print("wrote %s (%s)" % (out_path, story_summary(STORY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
