"""
Tests for Warmup 1: Topological Sort (Kahn's)
===============================================
Chapter 28: Topological Sort — Ordering Dependencies

Run with:
    python -m pytest code/python/ch28/tests/test_warmup_01.py -v
"""
from ch28.practice.warmup_01_topo_sort import solve


def is_valid_topo_order(n, edges, order):
    """Validate that order is a valid topological ordering."""
    if len(order) != n:
        return False
    if set(order) != set(range(n)):
        return False
    pos = {node: i for i, node in enumerate(order)}
    for u, v in edges:
        if pos[u] >= pos[v]:
            return False
    return True


def test_basic():
    edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    result = solve(6, edges)
    assert is_valid_topo_order(6, edges, result)


def test_chain():
    assert solve(3, [[0, 1], [1, 2]]) == [0, 1, 2]


def test_single():
    assert solve(1, []) == [0]


def test_two_independent():
    result = solve(2, [])
    assert is_valid_topo_order(2, [], result)


def test_diamond():
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
    result = solve(4, edges)
    assert is_valid_topo_order(4, edges, result)
