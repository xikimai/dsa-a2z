"""
Tests for Challenge 4: Fruit Into Baskets (Max Two Distinct Types)
===================================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

Run with:
    python -m pytest code/python/ch15/tests/test_challenge_04.py -v
"""
from ch15.practice.challenge_04_fruit_into_baskets import solve


def test_basic():
    assert solve([1, 2, 1]) == 3


def test_three_types():
    assert solve([0, 1, 2, 2]) == 3


def test_longer():
    assert solve([1, 2, 3, 2, 2]) == 4


def test_single_type():
    assert solve([1, 1, 1, 1]) == 4


def test_alternating():
    assert solve([1, 2, 1, 2, 1]) == 5


def test_single():
    assert solve([5]) == 1


def test_two_elements():
    assert solve([1, 2]) == 2


def test_many_types():
    assert solve([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
