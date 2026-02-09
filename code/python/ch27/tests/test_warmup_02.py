"""
Tests for Warmup 2: Network Delay Time
========================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_warmup_02.py -v
"""
from ch27.practice.warmup_02_network_delay import solve


def test_basic():
    assert solve([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2


def test_unreachable():
    assert solve([[1,2,1]], 2, 2) == -1


def test_single_edge():
    assert solve([[1,2,1]], 2, 1) == 1


def test_single_node():
    assert solve([], 1, 1) == 0


def test_star():
    times = [[1,2,5],[1,3,3],[1,4,7]]
    assert solve(times, 4, 1) == 7
