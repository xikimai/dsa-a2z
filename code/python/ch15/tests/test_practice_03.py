"""
Tests for Practice 3: Minimum Window Substring
================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_practice_03.py -v
"""
from ch15.practice.practice_03_minimum_window_substring import solve


def test_basic():
    assert solve("ADOBECODEBANC", "ABC") == "BANC"


def test_exact():
    assert solve("a", "a") == "a"


def test_no_window():
    assert solve("a", "aa") == ""


def test_t_longer():
    assert solve("ab", "abc") == ""


def test_entire_string():
    assert solve("abc", "abc") == "abc"


def test_duplicates_in_t():
    assert solve("AABC", "AAB") == "AAB"


def test_empty_s():
    assert solve("", "a") == ""
