"""
Tests for Practice 4: Longest Increasing Subsequence
=======================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_practice_04.py -v
"""
from ch25.practice.practice_04_lis import solve


def test_basic():
    assert solve([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_mixed():
    assert solve([0, 1, 0, 3, 2, 3]) == 4


def test_all_same():
    assert solve([7, 7, 7, 7, 7]) == 1


def test_increasing():
    assert solve([1, 2, 3, 4, 5]) == 5


def test_decreasing():
    assert solve([5, 4, 3, 2, 1]) == 1


def test_single():
    assert solve([42]) == 1
