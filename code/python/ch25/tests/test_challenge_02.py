"""
Tests for Challenge 2: Rod Cutting
=====================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_challenge_02.py -v
"""
from ch25.practice.challenge_02_rod_cutting import solve


def test_basic():
    assert solve([1, 5, 8, 9, 10, 17, 17, 20]) == 22


def test_basic2():
    assert solve([3, 5, 8, 9, 10, 17, 17, 20]) == 24


def test_single():
    assert solve([1]) == 1


def test_two():
    assert solve([1, 5]) == 5


def test_all_ones():
    assert solve([2, 3, 4, 5]) == 8
