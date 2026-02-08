"""
Tests for Warmup 3: Max Sum of Fixed Window
=============================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_warmup_03.py -v
"""
from ch15.practice.warmup_03_max_sum_fixed_window import solve


def test_basic():
    assert solve([2, 1, 5, 1, 3, 2], 3) == 9


def test_k_equals_length():
    assert solve([1, 2, 3], 3) == 6


def test_k_greater_than_length():
    assert solve([1, 2], 3) == 0


def test_single_window():
    assert solve([5], 1) == 5


def test_all_negatives():
    assert solve([-1, -2, -3, -4], 2) == -3


def test_mixed():
    assert solve([4, -1, 2, 1, 6, -5], 3) == 9


def test_empty():
    assert solve([], 1) == 0
