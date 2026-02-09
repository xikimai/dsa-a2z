"""
Tests for Warmup 2: Preorder Traversal
========================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_warmup_02.py -v
"""
from ch26.practice.warmup_02_preorder import solve, build_tree


def test_basic():
    assert solve(build_tree([1, None, 2, 3])) == [1, 2, 3]


def test_full():
    assert solve(build_tree([1, 2, 3, 4, 5])) == [1, 2, 4, 5, 3]


def test_empty():
    assert solve(None) == []
