"""
Tests for Challenge 3: Repeating and Missing Number
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_challenge_03.py -v
"""
from ch11.practice.challenge_03_repeating_missing import solve


def test_basic():
    assert solve([3, 1, 2, 5, 3]) == [3, 4]


def test_ones():
    assert solve([1, 1]) == [1, 2]


def test_twos():
    assert solve([2, 2]) == [2, 1]


def test_large():
    assert solve([4, 3, 6, 2, 1, 1]) == [1, 5]


def test_last():
    assert solve([1, 2, 3, 4, 4]) == [4, 5]
