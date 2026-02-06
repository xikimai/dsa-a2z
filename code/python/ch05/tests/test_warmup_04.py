"""
Tests for Warmup 4: Remove Duplicates from Sorted List
========================================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_warmup_04.py -v
"""

from ch05.practice.warmup_04_remove_duplicates import solve


def test_basic_duplicates():
    """Simple case with adjacent duplicates."""
    assert solve([1, 1, 2]) == [1, 2]


def test_multiple_duplicates():
    """Several groups of duplicates."""
    assert solve([1, 1, 1, 2, 2, 3]) == [1, 2, 3]


def test_single_element():
    """Single element — nothing to remove."""
    assert solve([1]) == [1]


def test_empty_list():
    """Empty list stays empty."""
    assert solve([]) == []


def test_no_duplicates():
    """Already unique — no changes."""
    assert solve([1, 2, 3]) == [1, 2, 3]
