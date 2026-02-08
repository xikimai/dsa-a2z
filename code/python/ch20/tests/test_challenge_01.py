"""
Tests for Challenge 1: Walls and Gates
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_challenge_01.py -v
"""
from ch20.practice.challenge_01_walls_and_gates import solve

INF = 2147483647


def test_basic():
    rooms = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]
    expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
    assert solve(rooms) == expected


def test_no_gates():
    rooms = [[INF, -1], [-1, INF]]
    expected = [[INF, -1], [-1, INF]]
    assert solve(rooms) == expected


def test_single_gate():
    rooms = [[0, INF], [INF, INF]]
    expected = [[0, 1], [1, 2]]
    assert solve(rooms) == expected


def test_all_walls():
    rooms = [[-1, -1], [-1, -1]]
    expected = [[-1, -1], [-1, -1]]
    assert solve(rooms) == expected


def test_gate_only():
    rooms = [[0]]
    expected = [[0]]
    assert solve(rooms) == expected


def test_two_gates():
    rooms = [[0, INF, INF, 0]]
    expected = [[0, 1, 1, 0]]
    assert solve(rooms) == expected
