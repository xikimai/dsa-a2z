"""
Tests for Practice 2: Unbounded Knapsack
==========================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_practice_02.py -v
"""
from ch25.practice.practice_02_unbounded_knapsack import solve


def test_basic():
    assert solve([2, 4, 6], [5, 11, 13], 10) == 27


def test_basic2():
    assert solve([1, 3, 4, 5], [10, 40, 50, 70], 8) == 110


def test_single_item():
    assert solve([3], [7], 9) == 21


def test_no_fit():
    assert solve([10], [100], 5) == 0


def test_exact():
    assert solve([5], [10], 5) == 10
