"""
Tests for Practice 1: Merge Sort
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_practice_01.py -v
"""

from ch08.practice.practice_01_merge_sort import solve


def test_basic():
    assert solve([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]


def test_reverse():
    assert solve([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_single():
    assert solve([1]) == [1]


def test_empty():
    assert solve([]) == []


def test_duplicates():
    assert solve([2, 1, 2, 1, 2]) == [1, 1, 2, 2, 2]


def test_already_sorted():
    assert solve([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
