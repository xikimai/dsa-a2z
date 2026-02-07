"""
Tests for Practice 4: Custom Comparator
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_practice_04.py -v
"""

from ch08.practice.practice_04_custom_comparator import solve


def test_basic():
    assert solve(["banana", "apple", "kiwi", "cherry", "fig"]) == ["fig", "kiwi", "apple", "banana", "cherry"]


def test_same_length():
    assert solve(["cat", "bat", "ant"]) == ["ant", "bat", "cat"]


def test_various():
    assert solve(["a", "bb", "ccc", "dd"]) == ["a", "bb", "dd", "ccc"]


def test_single():
    assert solve(["hello"]) == ["hello"]


def test_empty():
    assert solve([]) == []
