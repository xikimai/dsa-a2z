"""
Tests for Challenge 3: Rectangle Union Area
=============================================
Chapter 34: Computational Geometry & Sweep Line

Run with:
    python -m pytest code/python/ch34/tests/test_challenge_03.py -v
"""
from ch34.practice.challenge_03_rectangle_union_area import solve


def test_overlapping():
    assert solve([[0, 0, 2, 2], [1, 1, 3, 3]]) == 7


def test_disjoint():
    assert solve([[0, 0, 1, 1], [2, 2, 3, 3]]) == 2


def test_contained():
    assert solve([[0, 0, 10, 10], [1, 1, 9, 9]]) == 100


def test_single():
    assert solve([[0, 0, 5, 5]]) == 25


def test_three_overlapping():
    assert solve([[0, 0, 3, 3], [1, 1, 4, 4], [2, 2, 5, 5]]) == 19
