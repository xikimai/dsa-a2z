"""
Tests for Challenge 1: Critical Connections in a Network
=========================================================
Chapter 33: Advanced Trees & Graph Algorithms

Run with:
    python -m pytest code/python/ch33/tests/test_challenge_01.py -v
"""
from ch33.practice.challenge_01_critical_connections import solve


def test_basic():
    assert solve(4, [[0,1],[1,2],[2,0],[1,3]]) == [[1,3]]


def test_two_bridges():
    assert solve(5, [[0,1],[1,2],[2,3],[3,0],[2,4]]) == [[2,4]]


def test_no_bridges():
    assert solve(3, [[0,1],[1,2],[2,0]]) == []


def test_all_bridges():
    assert solve(3, [[0,1],[1,2]]) == [[0,1],[1,2]]
