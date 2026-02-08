"""
Tests for Warmup 5: Maximum Subarray
========================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_warmup_05.py -v
"""
from ch23.practice.warmup_05_max_subarray import solve


def test_mixed():
    assert solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_single():
    assert solve([1]) == 1


def test_all_positive():
    assert solve([5, 4, -1, 7, 8]) == 23


def test_all_negative():
    assert solve([-1, -2, -3]) == -1


def test_single_negative():
    assert solve([-1]) == -1
