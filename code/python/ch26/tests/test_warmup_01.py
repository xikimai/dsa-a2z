"""
Tests for Warmup 1: Inorder Traversal
=======================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_warmup_01.py -v
"""
from ch26.practice.warmup_01_inorder import solve, build_tree


def test_basic():
    assert solve(build_tree([1, None, 2, 3])) == [1, 3, 2]


def test_full():
    assert solve(build_tree([1, 2, 3, 4, 5])) == [4, 2, 5, 1, 3]


def test_empty():
    assert solve(None) == []


def test_single():
    assert solve(build_tree([1])) == [1]
