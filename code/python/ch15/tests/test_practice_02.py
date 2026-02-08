"""
Tests for Practice 2: Longest Substring Without Repeating Characters
======================================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_practice_02.py -v
"""
from ch15.practice.practice_02_longest_substring_no_repeat import solve


def test_basic():
    assert solve("abcabcbb") == 3


def test_all_same():
    assert solve("bbbbb") == 1


def test_alternating():
    assert solve("pwwkew") == 3


def test_empty():
    assert solve("") == 0


def test_single():
    assert solve("a") == 1


def test_all_unique():
    assert solve("abcdef") == 6


def test_spaces():
    assert solve("ab cd") == 5
