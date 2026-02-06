"""
Tests for Warmup 1: Second Largest
========================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_warmup_01.py -v
"""

from ch05.practice.warmup_01_second_largest import solve


def test_basic_case():
    """Mixed positive integers."""
    assert solve([3, 1, 4, 1, 5]) == 4


def test_all_same():
    """All elements identical — no second largest."""
    assert solve([7, 7, 7]) == -1


def test_two_elements():
    """Two distinct elements."""
    assert solve([1, 2]) == 1


def test_single_element():
    """Single element — no second largest."""
    assert solve([10]) == -1


def test_negative_numbers():
    """Negative numbers."""
    assert solve([-5, -2, -8]) == -5


def test_with_duplicates():
    """Duplicates present but distinct values exist."""
    assert solve([1, 2, 2, 3, 3]) == 2
