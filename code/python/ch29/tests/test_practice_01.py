"""
Tests for Practice 1: Number of Provinces
==========================================
Chapter 29: Union-Find & Minimum Spanning Trees

Run with:
    python -m pytest code/python/ch29/tests/test_practice_01.py -v
"""
from ch29.practice.practice_01_provinces import solve


def test_two_provinces():
    assert solve([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2


def test_all_isolated():
    assert solve([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3


def test_all_connected():
    assert solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 1
