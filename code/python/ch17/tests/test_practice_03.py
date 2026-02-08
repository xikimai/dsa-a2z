"""
Tests for Practice 3: Kth Smallest Element in a Sorted Matrix
=================================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

Run with:
    python -m pytest code/python/ch17/tests/test_practice_03.py -v
"""
from ch17.practice.practice_03_kth_smallest_matrix import solve


def test_basic():
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    assert solve(matrix, 8) == 13


def test_single_element():
    assert solve([[-5]], 1) == -5


def test_first_element():
    matrix = [[1, 2], [3, 4]]
    assert solve(matrix, 1) == 1


def test_last_element():
    matrix = [[1, 2], [3, 4]]
    assert solve(matrix, 4) == 4


def test_larger_matrix():
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    assert solve(matrix, 1) == 1
    assert solve(matrix, 5) == 11


def test_negative_values():
    matrix = [[-5, -4], [-3, -2]]
    assert solve(matrix, 3) == -3
