"""
Tests for Practice 3: Count Occurrences
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_practice_03.py -v
"""
from ch10.practice.practice_03_count_occurrences import solve


def test_multiple_occurrences():
    assert solve([1, 2, 3, 2, 4, 2], 2) == 3


def test_not_found():
    assert solve([1, 2, 3], 4) == 0


def test_empty_array():
    assert solve([], 1) == 0


def test_all_same():
    assert solve([5, 5, 5], 5) == 3


def test_single_element_found():
    assert solve([7], 7) == 1
