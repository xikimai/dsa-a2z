"""
Tests for Challenge 4: Cherry Pickup I
=========================================
Chapter 24: Dynamic Programming II — Grids and Paths

Run with:
    python -m pytest code/python/ch24/tests/test_challenge_04.py -v
"""
from ch24.practice.challenge_04_cherry_pickup import solve


def test_basic():
    assert solve([[0, 1, -1], [1, 0, -1], [1, 1, 1]]) == 5


def test_blocked():
    assert solve([[1, 1, -1], [1, -1, 1], [-1, 1, 1]]) == 0


def test_single():
    assert solve([[1]]) == 1


def test_no_cherries():
    assert solve([[0, 0], [0, 0]]) == 0


def test_all_cherries():
    assert solve([[1, 1], [1, 1]]) == 4
