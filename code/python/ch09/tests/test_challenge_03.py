"""
Tests for Challenge 3: Search in Rotated Sorted Array II
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_challenge_03.py -v
"""
from ch09.practice.challenge_03_rotated_search_ii import solve


def test_found_with_duplicates():
    assert solve([2, 5, 6, 0, 0, 1, 2], 0) is True


def test_not_found_with_duplicates():
    assert solve([2, 5, 6, 0, 0, 1, 2], 3) is False


def test_tricky_duplicates():
    assert solve([1, 0, 1, 1, 1], 0) is True


def test_all_same_not_found():
    assert solve([1, 1, 1, 1, 1], 2) is False


def test_single_element():
    assert solve([1], 1) is True


def test_two_elements():
    assert solve([1, 3], 3) is True
