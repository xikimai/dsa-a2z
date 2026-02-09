"""
Tests for Warmup 1: Traveling Salesman Problem (TSP)
=====================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

Run with:
    python -m pytest code/python/ch31/tests/test_warmup_01.py -v
"""
from ch31.practice.warmup_01_tsp import solve


def test_four_cities():
    dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    assert solve(4, dist) == 80


def test_three_cities():
    dist = [[0, 1, 15], [1, 0, 7], [15, 7, 0]]
    assert solve(3, dist) == 23


def test_two_cities():
    dist = [[0, 5], [5, 0]]
    assert solve(2, dist) == 10


def test_symmetric():
    dist = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
    assert solve(4, dist) == 4
