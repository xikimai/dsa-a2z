"""
Tests for Practice 4: Shortest Path in Binary Matrix
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_practice_04.py -v
"""
from ch20.practice.practice_04_shortest_path_binary_matrix import solve


def test_basic_2x2():
    assert solve([[0, 1], [1, 0]]) == 2


def test_3x3():
    assert solve([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4


def test_blocked_start():
    assert solve([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1


def test_blocked_end():
    assert solve([[0, 0, 0], [0, 0, 0], [0, 0, 1]]) == -1


def test_single():
    assert solve([[0]]) == 1


def test_diagonal_path():
    assert solve([[0, 0, 0], [1, 0, 1], [1, 1, 0]]) == 3


def test_no_path():
    assert solve([[0, 1], [1, 0]]) == 2
