"""
Tests for Practice 3: Right Side View
========================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_practice_03.py -v
"""
from ch26.practice.practice_03_right_view import solve, build_tree


def test_basic():
    assert solve(build_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]


def test_right_skewed():
    assert solve(build_tree([1, None, 3])) == [1, 3]


def test_empty():
    assert solve(None) == []
