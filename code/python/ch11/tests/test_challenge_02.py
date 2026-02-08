"""
Tests for Challenge 2: Longest Consecutive Sequence
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_challenge_02.py -v
"""
from ch11.practice.challenge_02_longest_consecutive import solve


def test_basic():
    assert solve([100, 4, 200, 1, 3, 2]) == 4


def test_long():
    assert solve([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_empty():
    assert solve([]) == 0


def test_single():
    assert solve([1]) == 1


def test_duplicates():
    assert solve([1, 1, 1]) == 1


def test_negatives():
    assert solve([9, 1, 4, 7, 3, -1, 0, 5, 8, 2, 6]) == 11
