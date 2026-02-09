"""
Tests for Practice 3: Find City with Smallest Neighbors at Threshold
=====================================================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_practice_03.py -v
"""
from ch27.practice.practice_03_city_threshold import solve


def test_basic():
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    assert solve(4, edges, 4) == 3


def test_larger():
    edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
    assert solve(5, edges, 2) == 0


def test_two_cities():
    assert solve(2, [[0,1,5]], 5) == 1


def test_two_cities_under():
    assert solve(2, [[0,1,5]], 4) == 1
