"""
Tests for Challenge 4: Smallest String With Swaps
===================================================
Chapter 29: Union-Find & Minimum Spanning Trees

Run with:
    python -m pytest code/python/ch29/tests/test_challenge_04.py -v
"""
from ch29.practice.challenge_04_smallest_string_swaps import solve


def test_two_groups():
    assert solve("dcab", [[0, 3], [1, 2]]) == "bacd"


def test_all_connected():
    assert solve("dcab", [[0, 3], [1, 2], [0, 2]]) == "abcd"


def test_chain():
    assert solve("cba", [[0, 1], [1, 2]]) == "abc"
