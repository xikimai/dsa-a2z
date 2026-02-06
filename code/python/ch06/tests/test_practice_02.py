"""
Tests for Practice 2: Max Subarray Sum (Brute Force)
========================================
Chapter 6: How Fast Is Your Code?

Run with:
    python -m pytest code/python/ch06/tests/test_practice_02.py -v
"""

from ch06.practice.practice_02_max_subarray_brute import solve


def test_classic():
    """Classic Kadane example."""
    assert solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_single_element():
    """Single element is its own subarray."""
    assert solve([1]) == 1


def test_all_negative():
    """Least negative element is the max subarray."""
    assert solve([-1, -2, -3]) == -1


def test_all_positive():
    """Entire array is the max subarray."""
    assert solve([5, 4, -1, 7, 8]) == 23


def test_empty():
    """Empty list returns 0."""
    assert solve([]) == 0
