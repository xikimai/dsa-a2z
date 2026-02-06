"""
Tests for Challenge 2: Apply Operations
========================================
Chapter 4: Functions

Run with:
    python -m pytest code/python/ch04/tests/test_challenge_02.py -v
"""

from ch04.practice.challenge_02_apply_operations import solve


def test_double_then_sort():
    """Double and sort."""
    assert solve([3, 1, 2], ["double", "sort"]) == [2, 4, 6]


def test_negate_then_reverse():
    """Negate and reverse."""
    assert solve([1, -2, 3], ["negate", "reverse"]) == [-3, 2, -1]


def test_sort_reverse_double():
    """Sort, reverse, then double."""
    assert solve([5, 3, 1], ["sort", "reverse", "double"]) == [10, 6, 2]


def test_no_operations():
    """No operations returns original list."""
    assert solve([3, 1, 2], []) == [3, 1, 2]


def test_empty_list():
    """Empty list with operations."""
    assert solve([], ["double", "sort"]) == []


def test_single_double():
    """Just double."""
    assert solve([1, 2, 3], ["double"]) == [2, 4, 6]


def test_single_negate():
    """Just negate."""
    assert solve([1, -2, 0], ["negate"]) == [-1, 2, 0]


def test_single_sort():
    """Just sort."""
    assert solve([3, 1, 2], ["sort"]) == [1, 2, 3]


def test_single_reverse():
    """Just reverse."""
    assert solve([1, 2, 3], ["reverse"]) == [3, 2, 1]
