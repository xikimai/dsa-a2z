"""
Tests for Challenge 4: Subset Sum
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_challenge_04.py -v
"""
from ch10.practice.challenge_04_subset_sum import solve


def test_has_subset():
    assert solve([3, 34, 4, 12, 5, 2], 9) is True


def test_no_subset():
    assert solve([3, 34, 4, 12, 5, 2], 30) is False


def test_exact_total():
    assert solve([1, 2, 3], 6) is True


def test_impossible_sum():
    assert solve([1, 2, 3], 7) is False


def test_empty_target_zero():
    assert solve([], 0) is True


def test_single_match():
    assert solve([5], 5) is True


def test_single_no_match():
    assert solve([5], 3) is False
