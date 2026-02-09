"""
Tests for Practice 3: Count Distinct Substrings
=================================================
Chapter 32: String Algorithms — Beyond Brute Force

Run with:
    python -m pytest code/python/ch32/tests/test_practice_03.py -v
"""
from ch32.practice.practice_03_count_distinct_substrings import solve


def test_abab():
    assert solve("abab") == 8


def test_aaa():
    assert solve("aaa") == 4


def test_abc():
    assert solve("abc") == 7


def test_single():
    assert solve("a") == 2  # "" and "a"


def test_two_same():
    assert solve("aa") == 3  # "", "a", "aa"
