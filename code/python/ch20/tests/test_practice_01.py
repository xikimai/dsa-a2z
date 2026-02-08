"""
Tests for Practice 1: Rotten Oranges
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_practice_01.py -v
"""
from ch20.practice.practice_01_rotten_oranges import solve


def test_basic():
    assert solve([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4


def test_impossible():
    assert solve([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1


def test_no_fresh():
    assert solve([[0, 2]]) == 0


def test_all_rotten():
    assert solve([[2, 2], [2, 2]]) == 0


def test_single_fresh():
    assert solve([[2, 1]]) == 1


def test_empty_grid():
    assert solve([[0]]) == 0


def test_multi_source():
    assert solve([[2, 1, 1], [1, 1, 1], [1, 1, 2]]) == 2
