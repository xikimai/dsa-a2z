"""
Tests for Challenge 1: Largest Rectangle in Histogram
=========================================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_challenge_01.py -v
"""
from ch22.practice.challenge_01_largest_rectangle import solve


def test_basic():
    assert solve([2, 1, 5, 6, 2, 3]) == 10


def test_two_bars():
    assert solve([2, 4]) == 4


def test_single():
    assert solve([5]) == 5


def test_increasing():
    assert solve([1, 2, 3, 4, 5]) == 9


def test_decreasing():
    assert solve([5, 4, 3, 2, 1]) == 9


def test_all_same():
    assert solve([3, 3, 3, 3]) == 12


def test_with_zero():
    assert solve([0, 9]) == 9


def test_valley():
    assert solve([6, 2, 5, 4, 5, 1, 6]) == 12
