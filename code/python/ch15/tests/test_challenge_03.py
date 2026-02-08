"""
Tests for Challenge 3: Longest Repeating Character Replacement
================================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_challenge_03.py -v
"""
from ch15.practice.challenge_03_longest_repeating_char_replacement import solve


def test_basic():
    assert solve("ABAB", 2) == 4


def test_limited():
    assert solve("AABABBA", 1) == 4


def test_no_replacement():
    assert solve("AAAA", 0) == 4


def test_all_different():
    assert solve("ABCDE", 2) == 3


def test_single():
    assert solve("A", 0) == 1


def test_k_equals_length():
    assert solve("AB", 2) == 2


def test_long_run():
    assert solve("AAABBC", 2) == 5
