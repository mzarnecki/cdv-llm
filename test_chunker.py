"""Tests for chunk_text."""

import unittest

from chunker import chunk_text


class ChunkTextTests(unittest.TestCase):
    def test_chunks_into_maximum_word_counts(self):
        self.assertEqual(
            chunk_text("one two three four five", 2),
            ["one two", "three four", "five"],
        )

    def test_keeps_word_order_spelling_and_punctuation(self):
        self.assertEqual(
            chunk_text("Hello, WORLD! don't stop.", 2),
            ["Hello, WORLD!", "don't stop."],
        )

    def test_normalizes_whitespace_to_single_spaces(self):
        self.assertEqual(chunk_text("  one\n\ttwo   three  ", 2), ["one two", "three"])

    def test_empty_text_returns_empty_list(self):
        self.assertEqual(chunk_text(" \n\t", 3), [])

    def test_one_word_limit(self):
        self.assertEqual(chunk_text("alpha beta", 1), ["alpha", "beta"])

    def test_non_positive_limit_raises_value_error(self):
        for max_words in (0, -1):
            with self.subTest(max_words=max_words):
                with self.assertRaises(ValueError):
                    chunk_text("one two", max_words)


if __name__ == "__main__":
    unittest.main()
