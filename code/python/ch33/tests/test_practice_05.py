"""
Tests for Practice 5: Count SCCs of Size > 1
==============================================
Chapter 33: Advanced Trees & Graph Algorithms

Run with:
    python -m pytest code/python/ch33/tests/test_practice_05.py -v
"""
from ch33.practice.practice_05_scc_size_gt1 import solve


def test_two_large_sccs():
    assert solve(7, [[0,1],[1,2],[2,0],[3,4],[4,5],[5,3],[6,0]]) == 2


def test_no_large_sccs():
    assert solve(4, [[0,1],[1,2],[2,3]]) == 0


def test_one_large_scc():
    assert solve(3, [[0,1],[1,0],[2,0]]) == 1


def test_single_big_scc():
    assert solve(4, [[0,1],[1,2],[2,3],[3,0]]) == 1
