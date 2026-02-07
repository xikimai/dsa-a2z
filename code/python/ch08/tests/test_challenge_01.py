"""
Tests for Challenge 1: Sort Three Ways
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_challenge_01.py -v
"""

from ch08.practice.challenge_01_sort_three_ways import (
    solve,
    solve_bubble,
    solve_merge,
    solve_builtin,
)


# ── Tests for solve_bubble ──────────────────────────────────────

def test_bubble_basic():
    assert solve_bubble([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]


# ── Tests for solve_merge ───────────────────────────────────────

def test_merge_basic():
    assert solve_merge([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]


# ── Tests for solve_builtin ────────────────────────────────────

def test_builtin_basic():
    assert solve_builtin([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]


# ── Tests for solve (default) ──────────────────────────────────

def test_solve_default():
    assert solve([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]


# ── Cross-cutting tests ────────────────────────────────────────

def test_single():
    assert solve_bubble([1]) == [1]
    assert solve_merge([1]) == [1]
    assert solve_builtin([1]) == [1]


def test_duplicates():
    assert solve([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


def test_empty():
    assert solve([]) == []


def test_reverse():
    assert solve([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
