"""
Tests for Warmup 1: Cross Product and Orientation
===================================================
Chapter 34: Computational Geometry & Sweep Line

Run with:
    python -m pytest code/python/ch34/tests/test_warmup_01.py -v
"""
from ch34.practice.warmup_01_orientation import solve


def test_mixed_orientations():
    queries = [[[0, 0], [4, 4], [1, 2]],
               [[0, 0], [4, 4], [1, 0]],
               [[0, 0], [4, 4], [2, 2]]]
    assert solve(queries) == [1, -1, 0]


def test_clockwise():
    queries = [[[0, 0], [1, 0], [0, 1]]]
    assert solve(queries) == [1]


def test_all_collinear():
    queries = [[[0, 0], [1, 1], [2, 2]],
               [[0, 0], [5, 5], [10, 10]]]
    assert solve(queries) == [0, 0]


def test_single_query():
    queries = [[[0, 0], [0, 1], [1, 0]]]
    assert solve(queries) == [-1]
