"""
Tests for Practice 4: Min Cost to Connect All Points
======================================================
Chapter 29: Union-Find & Minimum Spanning Trees

Run with:
    python -m pytest code/python/ch29/tests/test_practice_04.py -v
"""
from ch29.practice.practice_04_min_cost_connect_points import solve


def test_basic():
    assert solve([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20


def test_three_points():
    assert solve([[3, 12], [-2, 5], [-4, 1]]) == 18


def test_single_point():
    assert solve([[0, 0]]) == 0
