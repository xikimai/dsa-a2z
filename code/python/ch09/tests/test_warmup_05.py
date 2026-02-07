"""
Tests for Warmup 5: Count Occurrences
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_warmup_05.py -v
"""
from ch09.practice.warmup_05_count_occurrences import solve


def test_multiple_occurrences():
    assert solve([1, 2, 2, 2, 3, 4], 2) == 3


def test_all_same():
    assert solve([1, 1, 1, 1, 1], 1) == 5


def test_single_occurrence():
    assert solve([1, 3, 5, 7], 5) == 1


def test_not_found():
    assert solve([1, 3, 5, 7], 4) == 0


def test_empty_array():
    assert solve([], 1) == 0
