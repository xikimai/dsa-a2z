"""
Tests for Warmup 5: Longest Common Subsequence
=================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_warmup_05.py -v
"""
from ch25.practice.warmup_05_lcs import solve


def test_basic():
    assert solve("abcde", "ace") == 3


def test_identical():
    assert solve("abc", "abc") == 3


def test_no_common():
    assert solve("abc", "def") == 0


def test_longer():
    assert solve("oxcpqrsvwf", "shmtulqrypy") == 2


def test_single_char():
    assert solve("a", "a") == 1


def test_empty():
    assert solve("abc", "") == 0
