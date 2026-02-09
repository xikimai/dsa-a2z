"""
Tests for Warmup 4: Maximum Depth
===================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_warmup_04.py -v
"""
from ch26.practice.warmup_04_max_depth import solve, build_tree


def test_basic():
    assert solve(build_tree([3, 9, 20, None, None, 15, 7])) == 3


def test_skewed():
    assert solve(build_tree([1, None, 2])) == 2


def test_empty():
    assert solve(None) == 0
