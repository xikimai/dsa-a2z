"""
Tests for Warmup 1: Selection Sort
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_warmup_01.py -v
"""

from ch08.practice.warmup_01_selection_sort import solve


def test_basic():
    assert solve([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]


def test_already_sorted():
    assert solve([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse():
    assert solve([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_single():
    assert solve([1]) == [1]


def test_duplicates():
    assert solve([3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3]
