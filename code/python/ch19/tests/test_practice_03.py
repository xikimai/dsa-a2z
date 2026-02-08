"""
Tests for Practice 3: Bipartite Check
=======================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_practice_03.py -v
"""
from ch19.practice.practice_03_bipartite_check import solve


def test_even_cycle():
    # Square: 0-1-2-3-0
    assert solve(4, [[0, 1], [1, 2], [2, 3], [3, 0]]) is True


def test_odd_cycle():
    # Triangle: 0-1-2-0
    assert solve(3, [[0, 1], [1, 2], [0, 2]]) is False


def test_no_edges():
    assert solve(3, []) is True


def test_single_edge():
    assert solve(2, [[0, 1]]) is True


def test_disconnected_bipartite():
    assert solve(5, [[0, 1], [2, 3]]) is True


def test_five_cycle():
    # 0-1-2-3-4-0 is an odd cycle
    assert solve(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) is False
