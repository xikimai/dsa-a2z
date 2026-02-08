"""
Tests for Warmup 3: DFS Traversal
===================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_warmup_03.py -v
"""
from ch19.practice.warmup_03_dfs_traversal import solve


def test_basic():
    result = solve(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]], 0)
    assert result == [0, 1, 3, 2, 4]


def test_linear():
    result = solve(3, [[0, 1], [1, 2]], 0)
    assert result == [0, 1, 2]


def test_single_node():
    result = solve(1, [], 0)
    assert result == [0]


def test_from_middle():
    result = solve(4, [[0, 1], [1, 2], [2, 3]], 1)
    assert result == [1, 0, 2, 3]


def test_disconnected():
    # DFS from 0 only visits component containing 0
    result = solve(4, [[0, 1], [2, 3]], 0)
    assert result == [0, 1]
