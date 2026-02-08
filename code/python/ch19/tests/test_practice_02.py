"""
Tests for Practice 2: Detect Cycle in Undirected Graph
=======================================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_practice_02.py -v
"""
from ch19.practice.practice_02_detect_cycle import solve


def test_no_cycle():
    assert solve(4, [[0, 1], [1, 2], [2, 3]]) is False


def test_has_cycle():
    assert solve(4, [[0, 1], [1, 2], [2, 3], [3, 0]]) is True


def test_triangle():
    assert solve(3, [[0, 1], [1, 2], [0, 2]]) is True


def test_no_edges():
    assert solve(3, []) is False


def test_disconnected_with_cycle():
    assert solve(5, [[0, 1], [2, 3], [3, 4], [4, 2]]) is True


def test_disconnected_no_cycle():
    assert solve(5, [[0, 1], [2, 3]]) is False
