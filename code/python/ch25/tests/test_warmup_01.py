"""
Tests for Warmup 1: 0/1 Knapsack
===================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_warmup_01.py -v
"""
from ch25.practice.warmup_01_knapsack import solve


def test_basic():
    assert solve([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9


def test_tight():
    assert solve([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7


def test_too_heavy():
    assert solve([10], [10], 5) == 0


def test_exact_fit():
    assert solve([5], [10], 5) == 10


def test_empty():
    assert solve([], [], 10) == 0
