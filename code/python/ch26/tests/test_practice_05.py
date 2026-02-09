"""
Tests for Practice 5: Kth Smallest in BST
============================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_practice_05.py -v
"""
from ch26.practice.practice_05_kth_smallest import solve, build_tree


def test_first():
    assert solve(build_tree([3, 1, 4, None, 2]), 1) == 1


def test_third():
    assert solve(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
