"""
Tests for Practice 2: 01 Matrix
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_practice_02.py -v
"""
from ch20.practice.practice_02_zero_one_matrix import solve


def test_all_zeros():
    assert solve([[0, 0, 0], [0, 0, 0]]) == [[0, 0, 0], [0, 0, 0]]


def test_center_one():
    assert solve([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]


def test_bottom_row():
    assert solve([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]


def test_single_zero():
    assert solve([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[2, 1, 2], [1, 0, 1], [2, 1, 2]]


def test_single_cell():
    assert solve([[0]]) == [[0]]


def test_row():
    assert solve([[0, 1, 1, 1, 0]]) == [[0, 1, 2, 1, 0]]
