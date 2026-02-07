"""
Tests for Practice 1: Lower Bound
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_practice_01.py -v
"""
from ch09.practice.practice_01_lower_bound import solve


def test_exact_match():
    assert solve([1, 3, 5, 7, 9], 5) == 2


def test_between_elements():
    assert solve([1, 3, 5, 7, 9], 4) == 2


def test_first_element():
    assert solve([1, 3, 5, 7, 9], 1) == 0


def test_beyond_all():
    assert solve([1, 3, 5, 7, 9], 10) == 5


def test_all_same():
    assert solve([2, 2, 2, 2], 2) == 0


def test_empty_array():
    assert solve([], 5) == 0
