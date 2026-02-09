"""
Tests for Warmup 1: LCA with Binary Lifting
=============================================
Chapter 33: Advanced Trees & Graph Algorithms

Run with:
    python -m pytest code/python/ch33/tests/test_warmup_01.py -v
"""
from ch33.practice.warmup_01_lca_binary_lifting import solve


def test_basic_tree():
    assert solve(7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [[3,4],[3,6],[5,6]]) == [1, 0, 2]


def test_chain():
    assert solve(3, [[0,1],[1,2]], [[1,2],[0,2]]) == [1, 0]


def test_same_node():
    assert solve(3, [[0,1],[0,2]], [[1,1]]) == [1]


def test_root_query():
    assert solve(3, [[0,1],[0,2]], [[1,2]]) == [0]
