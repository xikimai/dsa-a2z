"""
Tests for Challenge 3: Distinct Substrings of Length K
=======================================================
Chapter 32: String Algorithms — Beyond Brute Force

Run with:
    python -m pytest code/python/ch32/tests/test_challenge_03.py -v
"""
from ch32.practice.challenge_03_distinct_substr_hash import solve


def test_abc():
    assert solve("abcabc", 3) == 3


def test_all_same():
    assert solve("aaaa", 2) == 1


def test_all_different():
    assert solve("abcdef", 1) == 6


def test_k_equals_n():
    assert solve("abc", 3) == 1


def test_overlapping():
    assert solve("abab", 2) == 2  # "ab", "ba"
