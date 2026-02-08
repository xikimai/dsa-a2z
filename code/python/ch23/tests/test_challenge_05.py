"""
Tests for Challenge 5: Longest Increasing Subsequence
========================================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_challenge_05.py -v
"""
from ch23.practice.challenge_05_lis import solve


def test_basic():
    assert solve([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_mixed():
    assert solve([0, 1, 0, 3, 2, 3]) == 4


def test_all_same():
    assert solve([7, 7, 7, 7]) == 1


def test_increasing():
    assert solve([1, 2, 3, 4, 5]) == 5


def test_decreasing():
    assert solve([5, 4, 3, 2, 1]) == 1


def test_single():
    assert solve([10]) == 1
