"""
Tests for Warmup 1: Build Adjacency List
==========================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_warmup_01.py -v
"""
from ch19.practice.warmup_01_build_adj_list import solve


def test_basic():
    adj = solve(4, [[0, 1], [0, 2], [1, 3]])
    assert adj[0] == [1, 2]
    assert adj[1] == [0, 3]
    assert adj[2] == [0]
    assert adj[3] == [1]


def test_no_edges():
    adj = solve(3, [])
    assert adj == [[], [], []]


def test_single_edge():
    adj = solve(2, [[0, 1]])
    assert adj[0] == [1]
    assert adj[1] == [0]


def test_complete_graph():
    adj = solve(3, [[0, 1], [0, 2], [1, 2]])
    assert adj[0] == [1, 2]
    assert adj[1] == [0, 2]
    assert adj[2] == [0, 1]


def test_single_node():
    adj = solve(1, [])
    assert adj == [[]]
