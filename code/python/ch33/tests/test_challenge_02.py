"""
Tests for Challenge 2: Reorder Routes to City Zero
====================================================
Chapter 33: Advanced Trees & Graph Algorithms

Run with:
    python -m pytest code/python/ch33/tests/test_challenge_02.py -v
"""
from ch33.practice.challenge_02_reorder_routes import solve


def test_basic():
    assert solve(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]) == 3


def test_all_toward_zero():
    assert solve(3, [[1,0],[2,0]]) == 0


def test_all_away():
    assert solve(3, [[0,1],[0,2]]) == 2


def test_chain():
    assert solve(4, [[0,1],[1,2],[2,3]]) == 3
