"""
Tests for Warmup 1: Linear Search
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_warmup_01.py -v
"""
from ch09.practice.warmup_01_linear_search import solve


def test_found_middle():
    assert solve([1, 3, 5, 7, 9], 5) == 2


def test_not_found():
    assert solve([1, 3, 5, 7, 9], 4) == -1


def test_first_of_duplicates():
    assert solve([2, 2, 2, 2], 2) == 0


def test_empty_array():
    assert solve([], 1) == -1


def test_single_element_found():
    assert solve([7], 7) == 0
