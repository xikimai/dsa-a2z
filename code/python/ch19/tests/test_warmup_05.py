"""
Tests for Warmup 5: Is Path Exists
====================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_warmup_05.py -v
"""
from ch19.practice.warmup_05_is_path_exists import solve


def test_path_exists():
    assert solve(5, [[0, 1], [1, 2], [3, 4]], 0, 2) is True


def test_no_path():
    assert solve(5, [[0, 1], [1, 2], [3, 4]], 0, 4) is False


def test_same_node():
    assert solve(3, [], 0, 0) is True


def test_direct_edge():
    assert solve(3, [[0, 1], [1, 2]], 0, 1) is True


def test_indirect_path():
    assert solve(4, [[0, 1], [1, 2], [2, 3]], 0, 3) is True


def test_isolated_node():
    assert solve(3, [[0, 1]], 0, 2) is False
