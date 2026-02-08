"""
Tests for Challenge 2: Maximum Subarray Sum Three Ways
========================================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_challenge_02.py -v
"""
from ch14.practice.challenge_02_max_subarray_three_ways import (
    solve_brute, solve_prefix, solve_kadane
)


def _check_all(arr, expected):
    assert solve_brute(arr) == expected
    assert solve_prefix(arr) == expected
    assert solve_kadane(arr) == expected


def test_basic():
    _check_all([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)


def test_all_negative():
    _check_all([-5, -3, -1, -4], -1)


def test_single():
    _check_all([7], 7)


def test_all_positive():
    _check_all([1, 2, 3], 6)


def test_mixed():
    _check_all([5, -9, 6, -2, 3], 7)


def test_single_negative():
    _check_all([-10], -10)
