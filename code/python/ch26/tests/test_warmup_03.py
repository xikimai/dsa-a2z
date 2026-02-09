"""
Tests for Warmup 3: Level Order Traversal
===========================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_warmup_03.py -v
"""
from ch26.practice.warmup_03_level_order import solve, build_tree


def test_basic():
    assert solve(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]


def test_single():
    assert solve(build_tree([1])) == [[1]]


def test_empty():
    assert solve(None) == []
