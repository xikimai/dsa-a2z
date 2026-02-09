"""
Tests for Practice 5: Longest Happy Prefix
============================================
Chapter 32: String Algorithms — Beyond Brute Force

Run with:
    python -m pytest code/python/ch32/tests/test_practice_05.py -v
"""
from ch32.practice.practice_05_longest_happy_prefix import solve


def test_level():
    assert solve("level") == "l"


def test_ababab():
    assert solve("ababab") == "abab"


def test_single_char():
    assert solve("a") == ""


def test_abcabc():
    assert solve("abcabc") == "abc"


def test_no_happy_prefix():
    assert solve("abcd") == ""


def test_all_same():
    assert solve("aaaa") == "aaa"
