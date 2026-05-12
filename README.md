# P1: Data Detective

## Project Summary

This project is a text-analysis tool written in Python. The program loads text from a UTF-8 file, normalizes and tokenizes the text, counts word frequencies using dictionaries, and displays the most common words in the dataset. It also provides additional insights such as unique words, longest unique words, and average word length.

The project focuses on practicing clean Python programming, modular function design, testing with `pytest`, dictionaries, and algorithmic thinking.

---

## Dataset

- **Dataset:** *Hidden Treasures; Or, Why Some Succeed While Others Fail*
- **Source:** Project Gutenberg
- **Why I chose it:**  
  I selected this dataset because it contains rich vocabulary, repeated patterns, and a variety of unique words. This makes it useful for testing word-frequency analysis and text-processing functions. The dataset is also classroom-safe and large enough to demonstrate meaningful results.

---

## Features

The program can:

- load text from a file
- normalize text by removing punctuation and converting to lowercase
- tokenize text into words
- count word frequencies
- display the top N most common words
- provide extra insights about the dataset

---

## Project Structure

```text
src/project.py
tests/test_project.py
README.md
data/sample.txt
.github/workflows/tests.yml