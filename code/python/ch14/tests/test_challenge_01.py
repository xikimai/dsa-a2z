"""
Tests for Challenge 1: 2D Prefix Sum and Range Query
======================================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_challenge_01.py -v
"""
from ch14.practice.challenge_01_2d_prefix_sum import solve


def test_3x3():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert solve(matrix, [[0, 0, 2, 2], [1, 1, 2, 2], [0, 0, 0, 0]]) == [45, 28, 1]


def test_single_element():
    matrix = [[5]]
    assert solve(matrix, [[0, 0, 0, 0]]) == [5]


def test_single_row():
    matrix = [[1, 2, 3, 4]]
    assert solve(matrix, [[0, 0, 0, 3], [0, 1, 0, 2]]) == [10, 5]


def test_single_column():
    matrix = [[1], [2], [3]]
    assert solve(matrix, [[0, 0, 2, 0], [1, 0, 2, 0]]) == [6, 5]


def test_2x2():
    matrix = [[1, 2], [3, 4]]
    assert solve(matrix, [[0, 0, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]) == [10, 3, 7]


def test_negatives():
    matrix = [[-1, 2], [3, -4]]
    assert solve(matrix, [[0, 0, 1, 1]]) == [0]
