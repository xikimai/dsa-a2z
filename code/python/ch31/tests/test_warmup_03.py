"""
Tests for Warmup 3: House Robber on Tree
==========================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

Run with:
    python -m pytest code/python/ch31/tests/test_warmup_03.py -v
"""
from ch31.practice.warmup_03_house_robber_tree import solve


def test_four_nodes():
    assert solve(4, [1, 2, 3, 4], [[0, 1], [0, 2], [1, 3]]) == 7


def test_three_nodes():
    assert solve(3, [1, 3, 5], [[0, 1], [0, 2]]) == 8


def test_single_node():
    assert solve(1, [10], []) == 10


def test_chain():
    # 0-1-2-3: values [3, 4, 5, 6] -> pick 0+2=8 or 1+3=10
    assert solve(4, [3, 4, 5, 6], [[0, 1], [1, 2], [2, 3]]) == 10


def test_star():
    # Center 0 connected to 1,2,3,4: values [10, 1, 1, 1, 1]
    # Pick center=10 or pick all leaves=4 -> 10
    assert solve(5, [10, 1, 1, 1, 1], [[0, 1], [0, 2], [0, 3], [0, 4]]) == 10
