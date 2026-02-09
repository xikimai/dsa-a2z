"""
Tests for Challenge 2: Maximal Rectangle
===========================================
Chapter 24: Dynamic Programming II — Grids and Paths

Run with:
    python -m pytest code/python/ch24/tests/test_challenge_02.py -v
"""
from ch24.practice.challenge_02_maximal_rectangle import solve


def test_basic():
    assert solve([[1, 0, 1, 0, 0],
                  [1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 1],
                  [1, 0, 0, 1, 0]]) == 6


def test_zero():
    assert solve([[0]]) == 0


def test_one():
    assert solve([[1]]) == 1


def test_all_ones():
    assert solve([[1, 1], [1, 1]]) == 4


def test_single_row():
    assert solve([[1, 1, 1, 0, 1]]) == 3
