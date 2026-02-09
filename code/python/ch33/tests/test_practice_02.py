"""
Tests for Practice 2: Strongly Connected Components (Kosaraju's)
=================================================================
Chapter 33: Advanced Trees & Graph Algorithms

Run with:
    python -m pytest code/python/ch33/tests/test_practice_02.py -v
"""
from ch33.practice.practice_02_scc_count import solve


def test_basic():
    assert solve(5, [[0,1],[1,2],[2,0],[1,3],[3,4]]) == 3


def test_single_scc():
    assert solve(4, [[0,1],[1,2],[2,3],[3,0]]) == 1


def test_all_separate():
    assert solve(3, [[0,1],[1,2]]) == 3


def test_two_sccs():
    assert solve(4, [[0,1],[1,0],[2,3],[3,2]]) == 2
