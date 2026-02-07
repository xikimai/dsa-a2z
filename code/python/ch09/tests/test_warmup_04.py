"""
Tests for Warmup 4: Last Occurrence
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_warmup_04.py -v
"""
from ch09.practice.warmup_04_last_occurrence import solve


def test_last_of_many():
    assert solve([1, 2, 2, 2, 3, 4], 2) == 3


def test_all_same():
    assert solve([1, 1, 1, 1, 1], 1) == 4


def test_unique_element():
    assert solve([1, 3, 5, 7], 5) == 2


def test_not_found():
    assert solve([1, 3, 5, 7], 4) == -1


def test_empty_array():
    assert solve([], 1) == -1
