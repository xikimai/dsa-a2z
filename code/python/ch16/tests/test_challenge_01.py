"""
Tests for Challenge 1: Aggressive Cows
=======================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_challenge_01.py -v
"""
from ch16.practice.challenge_01_aggressive_cows import solve


def test_basic():
    assert solve([1, 2, 8, 4, 9], 3) == 3


def test_two_cows():
    assert solve([1, 2, 4, 8, 9], 2) == 8


def test_all_stalls_used():
    assert solve([1, 3, 5], 3) == 2


def test_large_gap():
    assert solve([1, 100], 2) == 99


def test_evenly_spaced():
    assert solve([1, 5, 9, 13], 4) == 4


def test_unsorted_input():
    assert solve([10, 1, 5, 7, 3], 3) == 4


def test_many_stalls_few_cows():
    assert solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == 9
