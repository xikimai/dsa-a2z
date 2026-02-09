"""
Tests for Practice 4: Maximum Points on a Line
================================================
Chapter 34: Computational Geometry & Sweep Line

Run with:
    python -m pytest code/python/ch34/tests/test_practice_04.py -v
"""
from ch34.practice.practice_04_max_points_on_line import solve


def test_three_collinear():
    assert solve([[1, 1], [2, 2], [3, 3], [4, 1]]) == 3


def test_four_collinear():
    assert solve([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4


def test_single_point():
    assert solve([[0, 0]]) == 1


def test_two_points():
    assert solve([[0, 0], [1, 1]]) == 2


def test_all_same():
    assert solve([[1, 1], [1, 1], [1, 1]]) == 3
