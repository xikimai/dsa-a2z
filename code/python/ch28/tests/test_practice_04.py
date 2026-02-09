"""
Tests for Practice 4: All Ancestors of a Node
===============================================
Chapter 28: Topological Sort — Ordering Dependencies

Run with:
    python -m pytest code/python/ch28/tests/test_practice_04.py -v
"""
from ch28.practice.practice_04_all_ancestors import solve


def test_basic():
    result = solve(5, [[0, 1], [0, 2], [0, 3], [1, 4], [2, 4]])
    assert result == [[], [0], [0], [0], [0, 1, 2]]


def test_chain():
    result = solve(3, [[0, 1], [1, 2]])
    assert result == [[], [0], [0, 1]]


def test_no_edges():
    result = solve(3, [])
    assert result == [[], [], []]


def test_diamond():
    result = solve(4, [[0, 1], [0, 2], [1, 3], [2, 3]])
    assert result == [[], [0], [0], [0, 1, 2]]
