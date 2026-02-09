"""
Tests for Challenge 1: Construct from Preorder + Inorder
==========================================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_challenge_01.py -v
"""
from ch26.practice.challenge_01_construct import solve


def test_basic():
    assert solve([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]) == [3, 9, 20, None, None, 15, 7]


def test_single():
    assert solve([-1], [-1]) == [-1]
