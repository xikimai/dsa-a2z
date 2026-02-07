"""
Tests for Practice 4: Search in Rotated Sorted Array
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_practice_04.py -v
"""
from ch09.practice.practice_04_search_rotated import solve


def test_found_in_right_half():
    assert solve([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_not_found():
    assert solve([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_single_element():
    assert solve([1], 1) == 0


def test_small_rotation():
    assert solve([3, 1, 2], 1) == 1


def test_no_rotation():
    assert solve([1, 2, 3, 4, 5], 3) == 2
