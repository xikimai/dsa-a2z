"""
Tests for Practice 5: Sort Characters by Frequency
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_practice_05.py -v
"""
from ch11.practice.practice_05_sort_chars_by_freq import solve


def test_basic():
    assert solve("tree") == "eert"


def test_tie():
    assert solve("cccaaa") == "aaaccc"


def test_simple():
    assert solve("aab") == "aab"


def test_multiple():
    assert solve("hello") == "lleho"


def test_single():
    assert solve("x") == "x"


def test_empty():
    assert solve("") == ""
