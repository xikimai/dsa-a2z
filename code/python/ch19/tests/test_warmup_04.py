"""
Tests for Warmup 4: Count Connected Components
================================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_warmup_04.py -v
"""
from ch19.practice.warmup_04_count_components import solve


def test_two_components():
    assert solve(5, [[0, 1], [1, 2], [3, 4]]) == 2


def test_no_edges():
    assert solve(4, []) == 4


def test_fully_connected():
    assert solve(3, [[0, 1], [1, 2], [0, 2]]) == 1


def test_single_node():
    assert solve(1, []) == 1


def test_three_components():
    assert solve(7, [[0, 1], [0, 2], [3, 4], [3, 5]]) == 3
