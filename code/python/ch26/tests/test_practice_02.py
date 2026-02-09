"""
Tests for Practice 2: Balanced Binary Tree
=============================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_practice_02.py -v
"""
from ch26.practice.practice_02_balanced import solve, build_tree


def test_balanced():
    assert solve(build_tree([3, 9, 20, None, None, 15, 7])) is True


def test_unbalanced():
    assert solve(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])) is False


def test_empty():
    assert solve(None) is True
