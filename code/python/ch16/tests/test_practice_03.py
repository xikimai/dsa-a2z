"""
Tests for Practice 3: Search in 2D Matrix
==========================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_practice_03.py -v
"""
from ch16.practice.practice_03_search_2d_matrix import solve


def test_basic():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert solve(matrix, 3) == [0, 1]


def test_not_found():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert solve(matrix, 13) == [-1, -1]


def test_first_element():
    matrix = [[1, 3, 5], [7, 9, 11]]
    assert solve(matrix, 1) == [0, 0]


def test_last_element():
    matrix = [[1, 3, 5], [7, 9, 11]]
    assert solve(matrix, 11) == [1, 2]


def test_single_element_found():
    assert solve([[5]], 5) == [0, 0]


def test_single_element_not_found():
    assert solve([[5]], 3) == [-1, -1]


def test_empty():
    assert solve([], 1) == [-1, -1]
    assert solve([[]], 1) == [-1, -1]
