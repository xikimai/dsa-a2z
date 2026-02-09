"""
Tests for Warmup 1: Dijkstra SSSP
===================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_warmup_01.py -v
"""
from ch27.practice.warmup_01_dijkstra_sssp import solve


def test_basic():
    edges = [[0,1,4],[0,2,1],[2,1,2],[1,3,5],[2,3,8],[3,4,1]]
    assert solve(5, edges, 0) == [0, 3, 1, 8, 9]


def test_linear():
    assert solve(3, [[0,1,1],[1,2,2]], 0) == [0, 1, 3]


def test_single_node():
    assert solve(1, [], 0) == [0]


def test_unreachable():
    result = solve(3, [[0,1,5]], 0)
    assert result[0] == 0
    assert result[1] == 5
    assert result[2] == 10**9


def test_parallel_edges():
    edges = [[0,1,10],[0,1,3],[0,1,5]]
    assert solve(2, edges, 0) == [0, 3]
