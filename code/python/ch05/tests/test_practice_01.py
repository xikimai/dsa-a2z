"""
Tests for Practice 1: Union of Two Arrays
===========================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_practice_01.py -v
"""

from ch05.practice.practice_01_union_arrays import solve


def test_basic_overlap():
    """Two lists with partial overlap."""
    assert solve([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5]


def test_with_duplicates():
    """Lists containing internal duplicates."""
    assert solve([1, 1, 2], [2, 3, 3]) == [1, 2, 3]


def test_one_empty():
    """One list is empty."""
    assert solve([], [1, 2]) == [1, 2]


def test_same_element():
    """Both lists have the same single element."""
    assert solve([1], [1]) == [1]


def test_no_overlap():
    """No common elements."""
    assert solve([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
