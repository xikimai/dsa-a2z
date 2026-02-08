"""
Tests for Challenge 3: Median of Two Sorted Arrays
====================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_challenge_03.py -v
"""
from ch16.practice.challenge_03_median_two_sorted import solve


def test_basic_odd():
    assert solve([1, 3], [2]) == 2.0


def test_basic_even():
    assert solve([1, 2], [3, 4]) == 2.5


def test_one_empty():
    assert solve([], [1]) == 1.0
    assert solve([2], []) == 2.0


def test_same_elements():
    assert solve([1, 1], [1, 1]) == 1.0


def test_no_overlap():
    assert solve([1, 2], [3, 4, 5]) == 3.0


def test_single_elements():
    assert solve([1], [2]) == 1.5


def test_longer_arrays():
    assert solve([1, 3, 5, 7], [2, 4, 6, 8]) == 4.5
