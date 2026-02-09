"""
Tests for Challenge 1: Operations to Make Network Connected
=============================================================
Chapter 29: Union-Find & Minimum Spanning Trees

Run with:
    python -m pytest code/python/ch29/tests/test_challenge_01.py -v
"""
from ch29.practice.challenge_01_make_connected import solve


def test_one_spare():
    assert solve(4, [[0, 1], [0, 2], [1, 2]]) == 1


def test_two_spare():
    assert solve(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]) == 2


def test_impossible():
    assert solve(4, [[0, 1], [0, 2]]) == -1
