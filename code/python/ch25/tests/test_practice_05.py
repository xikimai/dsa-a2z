"""
Tests for Practice 5: Distinct Subsequences
==============================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_practice_05.py -v
"""
from ch25.practice.practice_05_distinct_subsequences import solve


def test_rabbbit():
    assert solve("rabbbit", "rabbit") == 3


def test_babgbag():
    assert solve("babgbag", "bag") == 5


def test_aaa():
    assert solve("aaa", "a") == 3


def test_no_match():
    assert solve("abc", "d") == 0


def test_identical():
    assert solve("abc", "abc") == 1
