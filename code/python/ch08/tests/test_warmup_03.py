"""
Tests for Warmup 3: Insertion Sort
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_warmup_03.py -v
"""

from ch08.practice.warmup_03_insertion_sort import solve


def test_basic():
    assert solve([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]


def test_already_sorted():
    assert solve([1, 2, 3]) == [1, 2, 3]


def test_reverse():
    assert solve([3, 2, 1]) == [1, 2, 3]


def test_single():
    assert solve([7]) == [7]


def test_duplicates():
    assert solve([4, 2, 4, 1, 2]) == [1, 2, 2, 4, 4]
