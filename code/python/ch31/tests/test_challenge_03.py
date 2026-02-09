"""
Tests for Challenge 3: Binary Tree Cameras
============================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

Run with:
    python -m pytest code/python/ch31/tests/test_challenge_03.py -v
"""
from ch31.practice.challenge_03_binary_tree_cameras import solve


def test_five_nodes():
    assert solve(5, [[0, 1], [0, 2], [1, 3], [1, 4]]) == 2


def test_three_chain():
    assert solve(3, [[0, 1], [1, 2]]) == 1


def test_single():
    assert solve(1, []) == 1


def test_two_nodes():
    assert solve(2, [[0, 1]]) == 1
