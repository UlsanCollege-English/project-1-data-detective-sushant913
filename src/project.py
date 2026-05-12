"""Project 1: Data Detective.

A text analysis tool that:
- loads text from a file
- normalizes and tokenizes text
- counts word frequencies
- reports the most common words
- provides an additional text insight
"""

from __future__ import annotations

from pathlib import Path
import string


TRANSLATOR = str.maketrans("", "", string.punctuation)


def load_text(path: str) -> str:
    """Load and return text from a UTF-8 encoded file.

    Args:
        path: Path to the text file.

    Returns:
        The full file contents as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def normalize_text(text: str) -> str:
    """Normalize text for analysis.

    Steps:
    - convert to lowercase
    - remove punctuation
    - remove extra whitespace

    Args:
        text: Raw input text.

    Returns:
        A cleaned and normalized string.
    """
    lowered_text = text.lower()

    cleaned_text = lowered_text.translate(TRANSLATOR)

    normalized_text = " ".join(cleaned_text.split())

    return normalized_text


def tokenize(text: str) -> list[str]:
    """Split normalized text into individual words.

    Args:
        text: Normalized text.

    Returns:
        A list of words.
    """
    if not text:
        return []

    return text.split()


def count_words(words: list[str]) -> dict[str, int]:
    """Count the frequency of each word.

    Args:
        words: A list of tokenized words.

    Returns:
        A dictionary mapping words to frequencies.
    """
    word_counts: dict[str, int] = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def top_n_words(
    counts: dict[str, int],
    n: int,
) -> list[tuple[str, int]]:
    """Return the top N most common words.

    Sorting rules:
    - frequency descending
    - alphabetical ascending for ties

    Args:
        counts: Dictionary of word frequencies.
        n: Number of top words to return.

    Returns:
        A list of (word, count) tuples.
    """
    if n <= 0 or not counts:
        return []

    sorted_words = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0]),
    )

    return sorted_words[:n]


def extra_insight(
    words: list[str],
    counts: dict[str, int],
) -> dict[str, object]:
    """Analyze unique words and word lengths.

    Extra insight includes:
    - words appearing only once
    - longest unique words
    - average word length

    Args:
        words: Tokenized words list.
        counts: Word frequency dictionary.

    Returns:
        A dictionary containing text insights.
    """
    unique_once = [
        word
        for word, count in counts.items()
        if count == 1
    ]

    longest_unique = sorted(
        unique_once,
        key=lambda word: (-len(word), word),
    )[:5]

    average_length = 0.0

    if words:
        total_characters = sum(len(word) for word in words)
        average_length = round(
            total_characters / len(words),
            2,
        )

    return {
        "unique_word_count": len(unique_once),
        "longest_unique_words": longest_unique,
        "average_word_length": average_length,
    }


def run_demo(path: str, n: int = 10) -> dict[str, object]:
    """Run the complete text-analysis pipeline.

    Args:
        path: Path to the input text file.
        n: Number of top words to display.

    Returns:
        A dictionary containing analysis results.
    """
    text = load_text(path)

    normalized_text = normalize_text(text)

    words = tokenize(normalized_text)

    counts = count_words(words)

    return {
        "total_words": len(words),
        "unique_words": len(counts),
        "top_words": top_n_words(counts, n),
        "extra_insight": extra_insight(words, counts),
    }


if __name__ == "__main__":
    sample_path = Path("data/sample.txt")

    if sample_path.exists():
        results = run_demo(str(sample_path), n=10)

        print("\n=== Data Detective Results ===")

        print(f"Total words: {results['total_words']}")
        print(f"Unique words: {results['unique_words']}")

        print("\nTop words:")
        for word, count in results["top_words"]:
            print(f"- {word}: {count}")

        print("\nExtra insight:")
        for key, value in results["extra_insight"].items():
            print(f"- {key}: {value}")

    else:
        print("No demo file found at data/sample.txt")