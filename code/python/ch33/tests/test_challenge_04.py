"""
Tests for Challenge 4: SCC Condensation (DAG of SCCs)
======================================================
Chapter 33: Advanced Trees & Graph Algorithms

Run with:
    python -m pytest code/python/ch33/tests/test_challenge_04.py -v
"""
from ch33.practice.challenge_04_scc_condensation import solve


def test_two_sccs_one_edge():
    assert solve(6, [[0,1],[1,2],[2,0],[3,4],[4,5],[5,3],[2,3]]) == 1


def test_two_sccs_connected():
    assert solve(4, [[0,1],[1,0],[2,3],[3,2],[1,2]]) == 1


def test_all_separate():
    assert solve(3, [[0,1],[1,2]]) == 2


def test_single_scc():
    assert solve(3, [[0,1],[1,2],[2,0]]) == 0
