"""
Tests for Practice 5: Find Minimum in Rotated Sorted Array
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_practice_05.py -v
"""
from ch09.practice.practice_05_min_in_rotated import solve


def test_rotated_by_three():
    assert solve([3, 4, 5, 1, 2]) == 1


def test_rotated_by_four():
    assert solve([4, 5, 6, 7, 0, 1, 2]) == 0


def test_single_element():
    assert solve([1]) == 1


def test_two_elements():
    assert solve([2, 1]) == 1


def test_not_rotated():
    assert solve([1, 2, 3, 4, 5]) == 1
