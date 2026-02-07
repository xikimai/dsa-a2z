"""
Tests for Practice 5: Merge Two Sorted Arrays
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_practice_05.py -v
"""

from ch08.practice.practice_05_merge_two_sorted import solve


def test_interleave():
    assert solve([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_no_interleave():
    assert solve([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_one_empty():
    assert solve([], [1, 2, 3]) == [1, 2, 3]


def test_both_empty():
    assert solve([], []) == []


def test_all_same():
    assert solve([1, 1, 1], [1, 1]) == [1, 1, 1, 1, 1]
