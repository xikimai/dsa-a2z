"""
Tests for Warmup 5: Symmetric Tree
=====================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_warmup_05.py -v
"""
from ch26.practice.warmup_05_symmetric import solve, build_tree


def test_symmetric():
    assert solve(build_tree([1, 2, 2, 3, 4, 4, 3])) is True


def test_asymmetric():
    assert solve(build_tree([1, 2, 2, None, 3, None, 3])) is False


def test_empty():
    assert solve(None) is True
