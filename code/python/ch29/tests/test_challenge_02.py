"""
Tests for Challenge 2: Making a Large Island
==============================================
Chapter 29: Union-Find & Minimum Spanning Trees

Run with:
    python -m pytest code/python/ch29/tests/test_challenge_02.py -v
"""
from ch29.practice.challenge_02_large_island import solve


def test_diagonal():
    assert solve([[1, 0], [0, 1]]) == 3


def test_one_zero():
    assert solve([[1, 1], [1, 0]]) == 4


def test_all_ones():
    assert solve([[1, 1], [1, 1]]) == 4
