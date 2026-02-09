"""
Tests for Practice 1: Articulation Points
==========================================
Chapter 33: Advanced Trees & Graph Algorithms

Run with:
    python -m pytest code/python/ch33/tests/test_practice_01.py -v
"""
from ch33.practice.practice_01_articulation_points import solve


def test_basic():
    assert solve(5, [[0,1],[1,2],[2,0],[1,3],[3,4]]) == [1, 3]


def test_cycle_no_ap():
    assert solve(4, [[0,1],[1,2],[2,3],[3,0]]) == []


def test_star():
    assert solve(5, [[0,1],[0,2],[0,3],[0,4]]) == [0]


def test_chain():
    # In a chain 0-1-2-3, nodes 1 and 2 are articulation points
    assert solve(4, [[0,1],[1,2],[2,3]]) == [1, 2]
