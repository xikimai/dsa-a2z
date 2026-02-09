"""
Tests for Practice 1: Shortest Hamiltonian Path
=================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

Run with:
    python -m pytest code/python/ch31/tests/test_practice_01.py -v
"""
from ch31.practice.practice_01_hamiltonian_path import solve


def test_four_cities():
    dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    assert solve(4, dist) == 50


def test_three_cities():
    dist = [[0, 1, 15], [1, 0, 7], [15, 7, 0]]
    assert solve(3, dist) == 8


def test_two_cities():
    dist = [[0, 5], [5, 0]]
    assert solve(2, dist) == 5


def test_all_same():
    dist = [[0, 3, 3], [3, 0, 3], [3, 3, 0]]
    assert solve(3, dist) == 6
