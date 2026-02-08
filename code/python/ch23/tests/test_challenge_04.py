"""
Tests for Challenge 4: House Robber III (Tree)
=================================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_challenge_04.py -v
"""
from ch23.practice.challenge_04_house_robber_iii import solve


def test_basic():
    # Tree:     3
    #          / \
    #         2   3
    #          \   \
    #           3   1
    assert solve([3, 2, 3, -1, 3, -1, 1]) == 7


def test_basic2():
    # Tree:     3
    #          / \
    #         4   5
    #        / \   \
    #       1   3   1
    assert solve([3, 4, 5, 1, 3, -1, 1]) == 9


def test_single():
    assert solve([1]) == 1


def test_two_levels():
    assert solve([1, 2, 3]) == 5


def test_empty():
    assert solve([]) == 0
