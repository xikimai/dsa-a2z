"""
Tests for Warmup 2: Euler Tour of Tree
========================================
Chapter 33: Advanced Trees & Graph Algorithms

Run with:
    python -m pytest code/python/ch33/tests/test_warmup_02.py -v
"""
from ch33.practice.warmup_02_euler_tour import solve


def test_basic_tree():
    assert solve(5, [[0,1],[0,2],[1,3],[1,4]]) == [0, 1, 3, 4, 2]


def test_small_tree():
    assert solve(3, [[0,1],[0,2]]) == [0, 1, 2]


def test_single_node():
    assert solve(1, []) == [0]


def test_chain():
    assert solve(4, [[0,1],[1,2],[2,3]]) == [0, 1, 2, 3]
