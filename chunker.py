"""Utilities for splitting text into word-count-limited chunks."""


def chunk_text(text, max_words):
    """Split text into chunks containing at most ``max_words`` words.

    Words are defined by :meth:`str.split`, and are joined with single spaces
    in each returned chunk.
    """
    if max_words <= 0:
        raise ValueError("max_words must be greater than zero")

    words = text.split()
    return [
        " ".join(words[index : index + max_words])
        for index in range(0, len(words), max_words)
    ]
