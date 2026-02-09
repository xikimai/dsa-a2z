"""
Tests for Practice 4: Tree Diameter via DP
============================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

Run with:
    python -m pytest code/python/ch31/tests/test_practice_04.py -v
"""
from ch31.practice.practice_04_tree_diameter import solve


def test_five_nodes():
    assert solve(5, [[0, 1], [1, 2], [1, 3], [3, 4]]) == 3


def test_two_nodes():
    assert solve(2, [[0, 1]]) == 1


def test_single_node():
    assert solve(1, []) == 0


def test_chain():
    assert solve(4, [[0, 1], [1, 2], [2, 3]]) == 3


def test_star():
    # All leaves distance 2 from each other via center
    assert solve(5, [[0, 1], [0, 2], [0, 3], [0, 4]]) == 2
