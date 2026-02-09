"""
Tests for Practice 6: LCA of Binary Tree
==========================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_practice_06.py -v
"""
from ch26.practice.practice_06_lca import solve, build_tree


def test_lca_root():
    assert solve(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), 5, 1) == 3


def test_lca_ancestor():
    assert solve(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), 5, 4) == 5


def test_lca_parent_child():
    assert solve(build_tree([1, 2]), 1, 2) == 1
