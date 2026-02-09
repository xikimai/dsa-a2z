"""
Tests for Practice 4: Number of Ways to Arrive at Destination
==============================================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_practice_04.py -v
"""
from ch27.practice.practice_04_count_paths import solve


def test_basic():
    roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    assert solve(7, roads) == 4


def test_two_nodes():
    assert solve(2, [[1,0,10]]) == 1


def test_single_node():
    assert solve(1, []) == 1


def test_triangle():
    roads = [[0,1,1],[1,2,1],[0,2,2]]
    assert solve(3, roads) == 2
