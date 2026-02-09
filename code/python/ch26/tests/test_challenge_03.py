"""
Tests for Challenge 3: Boundary Traversal
============================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_challenge_03.py -v
"""
from ch26.practice.challenge_03_boundary import solve, build_tree


def test_basic():
    assert solve(build_tree([1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10])) == [1, 2, 4, 7, 8, 9, 10, 6, 3]


def test_single():
    assert solve(build_tree([1])) == [1]
