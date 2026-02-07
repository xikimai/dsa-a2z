"""
Tests for Practice 2: Quick Sort
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_practice_02.py -v
"""

from ch08.practice.practice_02_quick_sort import solve


def test_basic():
    assert solve([10, 7, 8, 9, 1, 5]) == [1, 5, 7, 8, 9, 10]


def test_reverse():
    assert solve([3, 2, 1]) == [1, 2, 3]


def test_sorted():
    assert solve([1, 2, 3]) == [1, 2, 3]


def test_empty():
    assert solve([]) == []


def test_all_equal():
    assert solve([4, 4, 4, 4]) == [4, 4, 4, 4]
