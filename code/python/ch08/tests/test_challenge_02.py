"""
Tests for Challenge 2: Count Inversions
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_challenge_02.py -v
"""

from ch08.practice.challenge_02_count_inversions import solve


def test_basic():
    assert solve([2, 4, 1, 3, 5]) == 3


def test_sorted():
    assert solve([1, 2, 3, 4, 5]) == 0


def test_reverse():
    assert solve([5, 4, 3, 2, 1]) == 10


def test_single():
    assert solve([1]) == 0


def test_empty():
    assert solve([]) == 0


def test_all_equal():
    assert solve([1, 1, 1]) == 0
