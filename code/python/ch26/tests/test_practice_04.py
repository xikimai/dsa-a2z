"""
Tests for Practice 4: Validate BST
=====================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_practice_04.py -v
"""
from ch26.practice.practice_04_validate_bst import solve, build_tree


def test_valid():
    assert solve(build_tree([2, 1, 3])) is True


def test_invalid():
    assert solve(build_tree([5, 1, 4, None, None, 3, 6])) is False


def test_single():
    assert solve(build_tree([1])) is True
