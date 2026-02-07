"""
Tests for Warmup 3: First Occurrence
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_warmup_03.py -v
"""
from ch09.practice.warmup_03_first_occurrence import solve


def test_first_of_many():
    assert solve([1, 2, 2, 2, 3, 4], 2) == 1


def test_all_same():
    assert solve([1, 1, 1, 1, 1], 1) == 0


def test_unique_element():
    assert solve([1, 3, 5, 7], 5) == 2


def test_not_found():
    assert solve([1, 3, 5, 7], 4) == -1


def test_empty_array():
    assert solve([], 1) == -1
