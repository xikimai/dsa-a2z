"""
Tests for Practice 3: Two Sum
===============================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_practice_03.py -v
"""

from ch05.practice.practice_03_two_sum import solve


def test_basic_case():
    """First example: 2 + 7 = 9."""
    assert solve([2, 7, 11, 15], 9) == [0, 1]


def test_middle_elements():
    """Target found with middle elements."""
    assert solve([3, 2, 4], 6) == [1, 2]


def test_same_values():
    """Two identical values that sum to target."""
    assert solve([3, 3], 6) == [0, 1]


def test_no_solution():
    """No pair sums to target."""
    assert solve([1, 2, 3], 10) == [-1, -1]


def test_negative_numbers():
    """Negative numbers in the list."""
    assert solve([-1, -2, -3, -4, -5], -8) == [2, 4]
