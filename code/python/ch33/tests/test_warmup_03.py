"""
Tests for Warmup 3: Find Bridges in Graph
===========================================
Chapter 33: Advanced Trees & Graph Algorithms

Run with:
    python -m pytest code/python/ch33/tests/test_warmup_03.py -v
"""
from ch33.practice.warmup_03_bridges import solve


def test_basic():
    assert solve(5, [[0,1],[1,2],[2,0],[1,3],[3,4]]) == [[1,3],[3,4]]


def test_cycle_no_bridges():
    assert solve(4, [[0,1],[1,2],[2,3],[3,0]]) == []


def test_single_edge():
    assert solve(2, [[0,1]]) == [[0,1]]


def test_all_bridges():
    assert solve(4, [[0,1],[1,2],[2,3]]) == [[0,1],[1,2],[2,3]]
