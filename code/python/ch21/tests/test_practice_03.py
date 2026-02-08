"""
Tests for Practice 3: Merge Two Sorted Lists
==============================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_practice_03.py -v
"""
from ch21.practice.practice_03_merge_sorted import solve


def test_basic():
    assert solve([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_first_empty():
    assert solve([], [1, 2, 3]) == [1, 2, 3]


def test_second_empty():
    assert solve([1, 2, 3], []) == [1, 2, 3]


def test_both_empty():
    assert solve([], []) == []


def test_interleaved():
    assert solve([1, 4, 7], [2, 3, 5, 6]) == [1, 2, 3, 4, 5, 6, 7]


def test_duplicates():
    assert solve([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]


def test_single_elements():
    assert solve([1], [2]) == [1, 2]
