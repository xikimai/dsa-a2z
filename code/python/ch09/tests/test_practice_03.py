"""
Tests for Practice 3: Floor and Ceil
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_practice_03.py -v
"""
from ch09.practice.practice_03_floor_and_ceil import solve


def test_exact_match():
    assert solve([1, 3, 5, 7, 9], 5) == [5, 5]


def test_between_elements():
    assert solve([1, 3, 5, 7, 9], 4) == [3, 5]


def test_below_all():
    assert solve([1, 3, 5, 7, 9], 0) == [-1, 1]


def test_above_all():
    assert solve([1, 3, 5, 7, 9], 10) == [9, -1]


def test_single_element_match():
    assert solve([1], 1) == [1, 1]
