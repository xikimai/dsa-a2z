"""
Tests for Challenge 4: Kth Element of Two Sorted Arrays
========================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_challenge_04.py -v
"""
from ch16.practice.challenge_04_kth_element_two_sorted import solve


def test_basic():
    assert solve([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6


def test_first_element():
    assert solve([1, 3, 5], [2, 4, 6], 1) == 1


def test_last_element():
    assert solve([1, 3], [2, 4], 4) == 4


def test_one_empty():
    assert solve([], [1, 2, 3], 2) == 2


def test_other_empty():
    assert solve([5, 10, 15], [], 3) == 15


def test_all_from_first():
    assert solve([1, 2, 3], [10, 20, 30], 3) == 3


def test_all_from_second():
    assert solve([10, 20, 30], [1, 2, 3], 3) == 3


def test_k_equals_one():
    assert solve([3, 5], [1, 7], 1) == 1
