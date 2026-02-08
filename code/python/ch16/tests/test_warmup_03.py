"""
Tests for Warmup 3: Search in Rotated Sorted Array
====================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_warmup_03.py -v
"""
from ch16.practice.warmup_03_search_rotated import solve


def test_basic():
    assert solve([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_not_found():
    assert solve([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_single():
    assert solve([1], 1) == 0


def test_not_rotated():
    assert solve([1, 2, 3, 4, 5], 3) == 2


def test_empty():
    assert solve([], 5) == -1


def test_target_at_pivot():
    assert solve([3, 4, 5, 1, 2], 5) == 2


def test_two_elements():
    assert solve([2, 1], 1) == 1


def test_target_first():
    assert solve([4, 5, 6, 7, 0, 1, 2], 4) == 0
