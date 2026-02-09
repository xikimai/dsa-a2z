"""
Tests for Challenge 3: Tree Distance Queries (Binary Lifting)
==============================================================
Chapter 33: Advanced Trees & Graph Algorithms

Run with:
    python -m pytest code/python/ch33/tests/test_challenge_03.py -v
"""
from ch33.practice.challenge_03_tree_distance import solve


def test_basic():
    assert solve(5, [[0,1,2],[0,2,3],[1,3,4],[1,4,1]], [[3,4],[3,2]]) == [5, 9]


def test_simple():
    assert solve(3, [[0,1,5],[0,2,10]], [[1,2]]) == [15]


def test_same_node():
    assert solve(3, [[0,1,5],[0,2,10]], [[1,1]]) == [0]


def test_root_query():
    assert solve(2, [[0,1,7]], [[0,1]]) == [7]
