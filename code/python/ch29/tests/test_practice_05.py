"""
Tests for Practice 5: Satisfiability of Equality Equations
============================================================
Chapter 29: Union-Find & Minimum Spanning Trees

Run with:
    python -m pytest code/python/ch29/tests/test_practice_05.py -v
"""
from ch29.practice.practice_05_equations import solve


def test_contradiction():
    assert solve(["a==b", "b!=a"]) is False


def test_consistent_equal():
    assert solve(["b==a", "a==b"]) is True


def test_transitive():
    assert solve(["a==b", "b==c", "a==c"]) is True


def test_transitive_contradiction():
    assert solve(["a==b", "b!=c", "c==a"]) is False
