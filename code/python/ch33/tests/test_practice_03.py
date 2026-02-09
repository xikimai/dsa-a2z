"""
Tests for Practice 3: Subtree Sum (Euler Tour + Array)
=======================================================
Chapter 33: Advanced Trees & Graph Algorithms

Run with:
    python -m pytest code/python/ch33/tests/test_practice_03.py -v
"""
from ch33.practice.practice_03_subtree_sum import solve


def test_basic():
    assert solve(5, [1,2,3,4,5], [[0,1],[0,2],[1,3],[1,4]], [0,1,2]) == [15, 11, 3]


def test_small():
    assert solve(3, [10,20,30], [[0,1],[0,2]], [0,1]) == [60, 20]


def test_single():
    assert solve(1, [42], [], [0]) == [42]


def test_leaf_query():
    assert solve(3, [5,10,15], [[0,1],[0,2]], [1,2]) == [10, 15]
