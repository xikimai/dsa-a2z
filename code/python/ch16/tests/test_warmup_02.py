"""
Tests for Warmup 2: First and Last Position
=============================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_warmup_02.py -v
"""
from ch16.practice.warmup_02_first_last_position import solve


def test_basic():
    assert solve([5, 7, 7, 8, 8, 10], 8) == [3, 4]


def test_not_found():
    assert solve([5, 7, 7, 8, 8, 10], 6) == [-1, -1]


def test_single_occurrence():
    assert solve([1, 2, 3, 4, 5], 3) == [2, 2]


def test_all_same():
    assert solve([2, 2, 2, 2], 2) == [0, 3]


def test_empty():
    assert solve([], 1) == [-1, -1]


def test_single_element_found():
    assert solve([5], 5) == [0, 0]


def test_single_element_not_found():
    assert solve([5], 3) == [-1, -1]


def test_at_boundaries():
    assert solve([1, 1, 3, 5, 5], 1) == [0, 1]
    assert solve([1, 1, 3, 5, 5], 5) == [3, 4]
