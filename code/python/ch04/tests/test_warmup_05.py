"""
Tests for Warmup 5: Double List
========================================
Chapter 4: Functions

Run with:
    python -m pytest code/python/ch04/tests/test_warmup_05.py -v
"""

from ch04.practice.warmup_05_double_list import solve


def test_normal_list():
    """Double a normal list of positive integers."""
    assert solve([1, 2, 3]) == [2, 4, 6]


def test_empty_list():
    """Empty list returns empty list."""
    assert solve([]) == []


def test_single_element():
    """Single element list."""
    assert solve([5]) == [10]


def test_negative_numbers():
    """Doubling negative numbers."""
    assert solve([-1, -3]) == [-2, -6]


def test_zeros():
    """Doubling zeros stays zero."""
    assert solve([0, 0, 0]) == [0, 0, 0]


def test_mixed():
    """Mix of negative, zero, and positive."""
    assert solve([-1, 0, 5]) == [-2, 0, 10]


def test_in_place():
    """Verify the function modifies the list in place."""
    original = [1, 2, 3]
    result = solve(original)
    assert result is original  # Same object, not a copy
    assert original == [2, 4, 6]
