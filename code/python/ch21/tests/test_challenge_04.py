"""
Tests for Challenge 4: Flatten a Multilevel Doubly Linked List
===============================================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_challenge_04.py -v
"""
from ch21.practice.challenge_04_flatten import solve


def test_basic_nested():
    assert solve([1, 2, [3, 4, [5, 6]], 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_deep_nesting():
    assert solve([1, [2, [3]]]) == [1, 2, 3]


def test_flat():
    assert solve([1, 2, 3]) == [1, 2, 3]


def test_empty():
    assert solve([]) == []


def test_multiple_sublists():
    assert solve([1, [2, 3], 4, [5, 6], 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_single_element():
    assert solve([42]) == [42]


def test_nested_empty():
    assert solve([1, [], 2, [], 3]) == [1, 2, 3]
