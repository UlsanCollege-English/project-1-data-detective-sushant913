"""Tests for project.py."""

from pathlib import Path

from src.project import (
    count_words,
    extra_insight,
    load_text,
    normalize_text,
    run_demo,
    tokenize,
    top_n_words,
)


# =========================================================
# load_text
# =========================================================

def test_load_text_reads_file(tmp_path: Path) -> None:
    sample_file = tmp_path / "sample.txt"

    sample_file.write_text(
        "Hello world",
        encoding="utf-8",
    )

    assert load_text(str(sample_file)) == "Hello world"


# =========================================================
# normalize_text
# =========================================================

def test_normalize_text_lowercases_text() -> None:
    assert normalize_text("Hello WORLD") == "hello world"


def test_normalize_text_removes_punctuation() -> None:
    assert normalize_text(
        "Hello!!! World???"
    ) == "hello world"


def test_normalize_text_empty_string() -> None:
    assert normalize_text("") == ""


def test_normalize_text_mixed_case() -> None:
    assert normalize_text(
        "PyThOn TeSt"
    ) == "python test"


def test_normalize_text_removes_extra_spaces() -> None:
    assert normalize_text(
        "hello     world"
    ) == "hello world"


# =========================================================
# tokenize
# =========================================================

def test_tokenize_splits_words() -> None:
    assert tokenize(
        "one two three"
    ) == ["one", "two", "three"]


def test_tokenize_empty_string() -> None:
    assert tokenize("") == []


def test_tokenize_multiple_spaces() -> None:
    assert tokenize(
        "one   two    three"
    ) == ["one", "two", "three"]


# =========================================================
# count_words
# =========================================================

def test_count_words_counts_repeated_words() -> None:
    words = ["red", "blue", "red"]

    assert count_words(words) == {
        "red": 2,
        "blue": 1,
    }


def test_count_words_empty_list() -> None:
    assert count_words([]) == {}


def test_count_words_all_same() -> None:
    words = ["a", "a", "a"]

    assert count_words(words) == {"a": 3}


# =========================================================
# top_n_words
# =========================================================

def test_top_n_words_returns_most_common_items() -> None:
    counts = {
        "apple": 3,
        "banana": 1,
        "carrot": 2,
    }

    assert top_n_words(counts, 2) == [
        ("apple", 3),
        ("carrot", 2),
    ]


def test_top_n_words_with_non_positive_n_returns_empty_list() -> None:
    counts = {"apple": 3}

    assert top_n_words(counts, 0) == []


def test_top_n_words_n_larger_than_dict() -> None:
    counts = {
        "apple": 3,
        "banana": 2,
    }

    assert top_n_words(counts, 5) == [
        ("apple", 3),
        ("banana", 2),
    ]


def test_top_n_words_tie_breaker_alphabetical() -> None:
    counts = {
        "banana": 2,
        "apple": 2,
    }

    assert top_n_words(counts, 2) == [
        ("apple", 2),
        ("banana", 2),
    ]


def test_top_n_words_single_element() -> None:
    counts = {"apple": 5}

    assert top_n_words(counts, 1) == [
        ("apple", 5),
    ]


def test_top_n_words_empty_dict() -> None:
    assert top_n_words({}, 3) == []


# =========================================================
# extra_insight
# =========================================================

def test_extra_insight_returns_dictionary() -> None:
    words = ["red", "blue", "red"]

    counts = {
        "red": 2,
        "blue": 1,
    }

    insight = extra_insight(words, counts)

    assert isinstance(insight, dict)


def test_extra_insight_average_word_length() -> None:
    words = ["cat", "dog"]

    counts = {
        "cat": 1,
        "dog": 1,
    }

    insight = extra_insight(words, counts)

    assert insight["average_word_length"] == 3.0


# =========================================================
# run_demo
# =========================================================

def test_run_demo_returns_expected_keys(
    tmp_path: Path,
) -> None:
    sample_file = tmp_path / "sample.txt"

    sample_file.write_text(
        "apple banana apple",
        encoding="utf-8",
    )

    results = run_demo(str(sample_file), n=2)

    assert "total_words" in results
    assert "unique_words" in results
    assert "top_words" in results
    assert "extra_insight" in results