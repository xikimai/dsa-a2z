"""
Tests for Practice 3: Point in Polygon
========================================
Chapter 34: Computational Geometry & Sweep Line

Run with:
    python -m pytest code/python/ch34/tests/test_practice_03.py -v
"""
from ch34.practice.practice_03_point_in_polygon import solve


def test_square():
    polygon = [[0, 0], [4, 0], [4, 4], [0, 4]]
    queries = [[2, 2], [5, 5], [0, 0], [4, 2]]
    assert solve(polygon, queries) == [True, False, True, True]


def test_triangle():
    polygon = [[0, 0], [2, 0], [1, 2]]
    queries = [[1, 1], [3, 3]]
    assert solve(polygon, queries) == [True, False]


def test_boundary_point():
    polygon = [[0, 0], [4, 0], [4, 4], [0, 4]]
    queries = [[2, 0], [0, 2], [4, 4]]
    assert solve(polygon, queries) == [True, True, True]


def test_outside():
    polygon = [[0, 0], [2, 0], [1, 2]]
    queries = [[-1, -1], [3, 0], [0, 3]]
    assert solve(polygon, queries) == [False, False, False]
