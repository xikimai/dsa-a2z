"""
Tests for Challenge 4: Candy Distribution
============================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_challenge_04.py -v
"""
from ch18.practice.challenge_04_candy import solve


def test_basic():
    assert solve([1, 0, 2]) == 5


def test_equal_neighbors():
    assert solve([1, 2, 2]) == 4


def test_decreasing():
    assert solve([3, 2, 1]) == 6


def test_increasing():
    assert solve([1, 2, 3]) == 6


def test_single():
    assert solve([5]) == 1


def test_two_same():
    assert solve([1, 1]) == 2


def test_valley():
    assert solve([1, 3, 2, 2, 1]) == 7


def test_all_same():
    assert solve([5, 5, 5, 5]) == 4
