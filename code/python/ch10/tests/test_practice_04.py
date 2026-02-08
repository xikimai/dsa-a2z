"""
Tests for Practice 4: Binary Search (Recursive)
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_practice_04.py -v
"""
from ch10.practice.practice_04_binary_search_recursive import solve


def test_found_middle():
    assert solve([1, 3, 5, 7, 9], 5) == 2


def test_not_found():
    assert solve([1, 3, 5, 7, 9], 4) == -1


def test_empty_array():
    assert solve([], 1) == -1


def test_single_element_found():
    assert solve([1], 1) == 0


def test_found_last():
    assert solve([2, 4, 6, 8, 10], 10) == 4
