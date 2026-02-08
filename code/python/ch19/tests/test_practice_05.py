"""
Tests for Practice 5: All Paths from Source to Target
======================================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_practice_05.py -v
"""
from ch19.practice.practice_05_all_paths import solve


def test_basic():
    paths = solve(4, [[0, 1], [0, 2], [1, 3], [2, 3]])
    assert paths == [[0, 1, 3], [0, 2, 3]]


def test_multiple_paths():
    paths = solve(4, [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3]])
    assert paths == [[0, 1, 2, 3], [0, 1, 3], [0, 2, 3]]


def test_direct_path():
    paths = solve(2, [[0, 1]])
    assert paths == [[0, 1]]


def test_no_path():
    paths = solve(3, [[0, 1]])
    assert paths == []


def test_diamond():
    paths = solve(4, [[0, 1], [0, 2], [1, 3], [2, 3], [0, 3]])
    assert paths == [[0, 1, 3], [0, 2, 3], [0, 3]]
