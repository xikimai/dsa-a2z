"""
Tests for Challenge 5: Flatten Binary Tree
=============================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_challenge_05.py -v
"""
from ch26.practice.challenge_05_flatten import solve, build_tree


def test_basic():
    assert solve(build_tree([1, 2, 5, 3, 4, None, 6])) == [1, 2, 3, 4, 5, 6]


def test_empty():
    assert solve(None) == []
