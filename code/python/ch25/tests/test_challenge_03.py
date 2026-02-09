"""
Tests for Challenge 3: Target Sum
====================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_challenge_03.py -v
"""
from ch25.practice.challenge_03_target_sum import solve


def test_basic():
    assert solve([1, 1, 1, 1, 1], 3) == 5


def test_single():
    assert solve([1], 1) == 1


def test_with_zero():
    assert solve([1, 0], 1) == 2


def test_impossible():
    assert solve([1], 2) == 0


def test_all_plus():
    assert solve([1, 2, 3], 6) == 1
