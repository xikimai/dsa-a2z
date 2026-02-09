"""
Tests for Warmup 1: Connected Components (Union-Find)
======================================================
Chapter 29: Union-Find & Minimum Spanning Trees

Run with:
    python -m pytest code/python/ch29/tests/test_warmup_01.py -v
"""
from ch29.practice.warmup_01_connected_components import solve


def test_two_components():
    assert solve(5, [[0, 1], [1, 2], [3, 4]]) == 2


def test_all_isolated():
    assert solve(5, []) == 5


def test_single_component():
    assert solve(4, [[0, 1], [1, 2], [2, 3]]) == 1


def test_with_cycle():
    assert solve(3, [[0, 1], [0, 2], [1, 2]]) == 1
