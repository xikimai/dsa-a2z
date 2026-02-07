"""
Tests for Practice 2: Upper Bound
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_practice_02.py -v
"""
from ch09.practice.practice_02_upper_bound import solve


def test_exact_match():
    assert solve([1, 3, 5, 7, 9], 5) == 3


def test_between_elements():
    assert solve([1, 3, 5, 7, 9], 4) == 2


def test_before_all():
    assert solve([1, 3, 5, 7, 9], 0) == 0


def test_last_element():
    assert solve([1, 3, 5, 7, 9], 9) == 5


def test_all_same():
    assert solve([2, 2, 2, 2], 2) == 4


def test_empty_array():
    assert solve([], 5) == 0
