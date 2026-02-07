"""
Tests for Warmup 5: Sort by Absolute Value
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_warmup_05.py -v
"""

from ch08.practice.warmup_05_sort_by_absolute import solve


def test_mixed():
    assert solve([3, -1, 2, -5, 4]) == [-1, 2, 3, 4, -5]


def test_negatives():
    assert solve([-10, 7, -3, 1]) == [1, -3, 7, -10]


def test_with_zero():
    assert solve([0, -5, 3, -1, 8]) == [0, -1, 3, -5, 8]


def test_positive():
    assert solve([1, 2, 3]) == [1, 2, 3]


def test_single():
    assert solve([-1]) == [-1]
