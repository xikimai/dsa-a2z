"""
Tests for Challenge 3: Rotate Array
=====================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_challenge_03.py -v
"""

from ch05.practice.challenge_03_rotate_array import solve


def test_basic_rotation():
    """Rotate [1,2,3,4,5,6,7] by 3 steps."""
    assert solve([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]


def test_k_greater_than_length():
    """k is larger than the list length."""
    assert solve([1, 2], 3) == [2, 1]


def test_single_element():
    """Single element — rotation has no effect."""
    assert solve([1], 5) == [1]


def test_negative_numbers():
    """List with negative numbers."""
    assert solve([-1, -100, 3, 99], 2) == [3, 99, -1, -100]


def test_k_zero():
    """k=0 means no rotation."""
    assert solve([1, 2, 3], 0) == [1, 2, 3]
