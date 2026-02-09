"""
Tests for Challenge 4: Longest String Chain
==============================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_challenge_04.py -v
"""
from ch25.practice.challenge_04_longest_string_chain import solve


def test_basic():
    assert solve(["a", "b", "ba", "bca", "bda", "bdca"]) == 4


def test_longer():
    assert solve(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5


def test_single():
    assert solve(["abc"]) == 1


def test_no_chain():
    assert solve(["abc", "def", "ghi"]) == 1


def test_two_chain():
    assert solve(["a", "ab"]) == 2
