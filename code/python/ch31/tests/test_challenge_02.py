"""
Tests for Challenge 2: Number of Ways to Wear Hats
====================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

Run with:
    python -m pytest code/python/ch31/tests/test_challenge_02.py -v
"""
from ch31.practice.challenge_02_wear_hats import solve


def test_two_people_same():
    assert solve(2, [[1, 2], [1, 2]]) == 2


def test_two_people_diff():
    assert solve(2, [[1, 2, 3], [1, 2]]) == 4


def test_single_person():
    assert solve(1, [[1]]) == 1


def test_three_people():
    # Person 0: hat 1,2; Person 1: hat 2,3; Person 2: hat 3,4
    # Valid: (1,2,3), (1,2,4), (1,3,4), (2,3,4) = 4
    assert solve(3, [[1, 2], [2, 3], [3, 4]]) == 4
