"""
Tests for Practice 1: Diameter of Binary Tree
================================================
Chapter 26: Trees — Branches of Logic

Run with:
    python -m pytest code/python/ch26/tests/test_practice_01.py -v
"""
from ch26.practice.practice_01_diameter import solve, build_tree


def test_basic():
    assert solve(build_tree([1, 2, 3, 4, 5])) == 3


def test_two_nodes():
    assert solve(build_tree([1, 2])) == 1


def test_empty():
    assert solve(None) == 0
