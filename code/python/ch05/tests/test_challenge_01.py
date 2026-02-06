"""
Tests for Challenge 1: Find All Duplicates
============================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_challenge_01.py -v
"""

from ch05.practice.challenge_01_find_duplicates import (
    solve,
    solve_brute,
    solve_sort,
    solve_set,
)


def test_basic_case():
    """Multiple duplicates in the list."""
    assert solve([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]


def test_no_duplicates():
    """All elements are unique."""
    assert solve([1, 2, 3]) == []


def test_all_same():
    """All elements are the same."""
    assert solve([1, 1, 1, 1]) == [1]


def test_empty_list():
    """Empty list has no duplicates."""
    assert solve([]) == []


def test_brute_force():
    """Verify the brute force approach works."""
    assert solve_brute([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]


def test_sort_approach():
    """Verify the sort-based approach works."""
    assert solve_sort([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]


def test_set_approach():
    """Verify the set-based approach works."""
    assert solve_set([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
