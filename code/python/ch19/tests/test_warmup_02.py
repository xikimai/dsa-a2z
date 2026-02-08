"""
Tests for Warmup 2: BFS Traversal
===================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_warmup_02.py -v
"""
from ch19.practice.warmup_02_bfs_traversal import solve


def test_basic():
    result = solve(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]], 0)
    assert result == [0, 1, 2, 3, 4]


def test_from_different_source():
    result = solve(3, [[0, 1], [1, 2]], 2)
    assert result == [2, 1, 0]


def test_linear_graph():
    result = solve(4, [[0, 1], [1, 2], [2, 3]], 0)
    assert result == [0, 1, 2, 3]


def test_single_node():
    result = solve(1, [], 0)
    assert result == [0]


def test_disconnected():
    # BFS from 0 only visits component containing 0
    result = solve(4, [[0, 1], [2, 3]], 0)
    assert result == [0, 1]
