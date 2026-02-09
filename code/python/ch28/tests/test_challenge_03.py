"""
Tests for Challenge 3: Largest Color Value in Directed Graph
=============================================================
Chapter 28: Topological Sort — Ordering Dependencies

Run with:
    python -m pytest code/python/ch28/tests/test_challenge_03.py -v
"""
from ch28.practice.challenge_03_largest_color_value import solve


def test_basic():
    assert solve("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]) == 3


def test_self_loop():
    assert solve("a", [[0, 0]]) == -1


def test_single_node():
    assert solve("a", []) == 1


def test_chain_same_color():
    assert solve("aaa", [[0, 1], [1, 2]]) == 3


def test_chain_diff_colors():
    assert solve("abc", [[0, 1], [1, 2]]) == 1
