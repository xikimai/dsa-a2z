"""
Tests for Practice 1: Activity Selection
==========================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_practice_01.py -v
"""
from ch18.practice.practice_01_activity_selection import solve


def test_basic():
    assert solve([[1, 2], [3, 4], [0, 6], [5, 7], [8, 9], [5, 9]]) == 4


def test_overlapping():
    assert solve([[1, 3], [2, 5], [4, 7], [6, 8]]) == 2


def test_no_overlap():
    assert solve([[1, 2], [3, 4], [5, 6]]) == 3


def test_all_overlap():
    assert solve([[1, 10], [2, 10], [3, 10]]) == 1


def test_single():
    assert solve([[0, 5]]) == 1


def test_empty():
    assert solve([]) == 0


def test_touching():
    assert solve([[0, 1], [1, 2], [2, 3], [3, 4]]) == 4
