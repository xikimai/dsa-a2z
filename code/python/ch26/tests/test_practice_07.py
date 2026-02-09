"""
Tests for Practice 7: Maximum Path Sum
=========================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_practice_07.py -v
"""
from ch26.practice.practice_07_max_path_sum import solve, build_tree


def test_basic():
    assert solve(build_tree([1, 2, 3])) == 6


def test_negative():
    assert solve(build_tree([-10, 9, 20, None, None, 15, 7])) == 42


def test_single_negative():
    assert solve(build_tree([-3])) == -3
