"""
Tests for Warmup 4: Detect Cycle in Directed Graph
=====================================================
Chapter 28: Topological Sort — Ordering Dependencies

Run with:
    python -m pytest code/python/ch28/tests/test_warmup_04.py -v
"""
from ch28.practice.warmup_04_detect_cycle import solve


def test_dag():
    assert solve(4, [[0, 1], [1, 2], [2, 3]]) is True


def test_cycle():
    assert solve(3, [[0, 1], [1, 2], [2, 0]]) is False


def test_dag_with_branch():
    assert solve(4, [[0, 1], [1, 2], [3, 0]]) is True


def test_self_loop():
    assert solve(2, [[0, 0]]) is False


def test_single_no_edges():
    assert solve(1, []) is True


def test_disconnected_with_cycle():
    assert solve(5, [[0, 1], [2, 3], [3, 4], [4, 2]]) is False
