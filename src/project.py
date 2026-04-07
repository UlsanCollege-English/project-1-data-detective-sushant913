"""Project 1 starter: Data Detective.

Implemented version (beginner friendly).
"""

from __future__ import annotations
from pathlib import Path
import string


def load_text(path: str) -> str:
    """Load and return the full text from a UTF-8 file."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def normalize_text(text: str) -> str:
    """Normalize text:
    - lowercase
    - remove punctuation
    - remove extra spaces
    """
    text = text.lower()

    # remove punctuation
    for p in string.punctuation:
        text = text.replace(p, "")

    # remove extra whitespace
    text = " ".join(text.split())

    return text


def tokenize(text: str) -> list[str]:
    """Split normalized text into words."""
    return text.split()


def count_words(words: list[str]) -> dict[str, int]:
    """Count word frequency."""
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def top_n_words(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return top N words sorted by frequency and alphabet."""
    if n <= 0:
        return []

    # sort: highest count first, then alphabetical
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    return sorted_words[:n]


def extra_insight(words: list[str], counts: dict[str, int]) -> object:
    """Return words that appear only once."""
    unique_once = []

    for word, count in counts.items():
        if count == 1:
            unique_once.append(word)

    return unique_once


def run_demo(path: str, n: int = 10) -> dict[str, object]:
    """Run the full pipeline."""
    text = load_text(path)
    normalized = normalize_text(text)
    words = tokenize(normalized)
    counts = count_words(words)

    return {
        "total_words": len(words),
        "unique_words": len(counts),
        "top_words": top_n_words(counts, n),
        "extra_insight": extra_insight(words, counts),
    }


if __name__ == "__main__":
    demo_path = Path("data/sample.txt")

    if demo_path.exists():
        results = run_demo(str(demo_path), n=10)

        for key, value in results.items():
            print(f"{key}: {value}")
    else:
        print("No demo file found at data/sample.txt")