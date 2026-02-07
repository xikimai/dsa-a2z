"""
Tests for Warmup 2: Bubble Sort
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_warmup_02.py -v
"""

from ch08.practice.warmup_02_bubble_sort import solve


def test_basic():
    assert solve([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]


def test_already_sorted():
    assert solve([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_two_elements():
    assert solve([2, 1]) == [1, 2]


def test_empty():
    assert solve([]) == []


def test_all_equal():
    assert solve([5, 5, 5]) == [5, 5, 5]
