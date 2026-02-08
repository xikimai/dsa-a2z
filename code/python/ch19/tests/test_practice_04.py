"""
Tests for Practice 4: Clone Graph
===================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_practice_04.py -v
"""
from ch19.practice.practice_04_clone_graph import solve


def test_basic():
    adj = [[1, 2], [0, 3], [0, 3], [1, 2]]
    clone = solve(adj)
    assert clone == adj
    # Ensure it's a deep copy (different objects)
    assert clone is not adj
    for i in range(len(adj)):
        assert clone[i] is not adj[i]


def test_empty_graph():
    adj = []
    clone = solve(adj)
    assert clone == []


def test_single_node():
    adj = [[]]
    clone = solve(adj)
    assert clone == [[]]
    assert clone is not adj
    assert clone[0] is not adj[0]


def test_disconnected():
    adj = [[1], [0], [3], [2]]
    clone = solve(adj)
    assert clone == adj
    assert clone is not adj


def test_modification_independence():
    adj = [[1, 2], [0], [0]]
    clone = solve(adj)
    clone[0].append(99)
    assert 99 not in adj[0]
