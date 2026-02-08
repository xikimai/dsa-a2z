"""
Tests for Practice 1: Shortest Path (Unweighted)
==================================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_practice_01.py -v
"""
from ch19.practice.practice_01_shortest_path import solve


def test_basic():
    assert solve(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]], 0) == [0, 1, 1, 2, 3]


def test_disconnected():
    assert solve(4, [[0, 1], [2, 3]], 0) == [0, 1, -1, -1]


def test_single_node():
    assert solve(1, [], 0) == [0]


def test_linear():
    assert solve(4, [[0, 1], [1, 2], [2, 3]], 0) == [0, 1, 2, 3]


def test_from_middle():
    assert solve(5, [[0, 1], [1, 2], [2, 3], [3, 4]], 2) == [2, 1, 0, 1, 2]


def test_cycle():
    assert solve(4, [[0, 1], [1, 2], [2, 3], [3, 0]], 0) == [0, 1, 2, 1]
