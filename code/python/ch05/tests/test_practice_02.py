"""
Tests for Practice 2: Anagram Check
=====================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_practice_02.py -v
"""

from ch05.practice.practice_02_anagram_check import solve


def test_classic_anagram():
    """listen and silent are anagrams."""
    assert solve("listen", "silent") is True


def test_not_anagram():
    """hello and world are not anagrams."""
    assert solve("hello", "world") is False


def test_empty_strings():
    """Two empty strings are anagrams of each other."""
    assert solve("", "") is True


def test_case_insensitive():
    """Anagram check should ignore case."""
    assert solve("Aa", "aA") is True


def test_different_lengths():
    """Different lengths can never be anagrams."""
    assert solve("abc", "ab") is False
