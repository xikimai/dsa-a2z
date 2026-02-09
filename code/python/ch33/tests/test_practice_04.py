"""
Tests for Practice 4: LCA Queries with Node Values
====================================================
Chapter 33: Advanced Trees & Graph Algorithms

Run with:
    python -m pytest code/python/ch33/tests/test_practice_04.py -v
"""
from ch33.practice.practice_04_lca_values import solve


def test_basic():
    assert solve(5, [10,20,30,40,50], [[0,1],[0,2],[1,3],[1,4]], [[3,4],[3,2]]) == [20, 10]


def test_small():
    assert solve(3, [5,10,15], [[0,1],[0,2]], [[1,2]]) == [5]


def test_same_node():
    assert solve(3, [5,10,15], [[0,1],[0,2]], [[1,1]]) == [10]


def test_root_is_lca():
    assert solve(4, [100,200,300,400], [[0,1],[0,2],[2,3]], [[1,3]]) == [100]
