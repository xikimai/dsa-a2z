"""
Tests for Warmup 3: Bellman-Ford SSSP
======================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_warmup_03.py -v
"""
from ch27.practice.warmup_03_bellman_ford import solve


def test_negative_weights():
    edges = [[0,1,-1],[0,2,4],[1,2,3],[1,3,2],[1,4,2],[3,2,5],[3,1,1],[4,3,-3]]
    assert solve(5, edges, 0) == [0, -1, 2, -2, 1]


def test_all_positive():
    edges = [[0,1,4],[0,2,1],[2,1,2]]
    assert solve(3, edges, 0) == [0, 3, 1]


def test_single_node():
    assert solve(1, [], 0) == [0]


def test_unreachable():
    result = solve(3, [[0,1,5]], 0)
    assert result[0] == 0
    assert result[1] == 5
    assert result[2] == 10**9


def test_negative_shortcut():
    edges = [[0,1,4],[1,2,-2],[0,2,3]]
    assert solve(3, edges, 0) == [0, 4, 2]
