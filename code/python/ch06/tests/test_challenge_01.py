"""
Tests for Challenge 1: Two Sum Three Ways
========================================
Chapter 6: How Fast Is Your Code?

Run with:
    python -m pytest code/python/ch06/tests/test_challenge_01.py -v
"""

from ch06.practice.challenge_01_two_sum_three_ways import (
    solve,
    solve_brute,
    solve_hash,
    solve_sort,
)


# ── Tests for solve_brute ──────────────────────────────────────


def test_brute_basic():
    assert solve_brute([2, 7, 11, 15], 9) == [0, 1]


def test_brute_duplicates():
    assert solve_brute([3, 3], 6) == [0, 1]


def test_brute_no_solution():
    assert solve_brute([1, 2, 3], 10) == [-1, -1]


def test_brute_middle_pair():
    assert solve_brute([1, 5, 3, 8], 8) == [1, 2]


# ── Tests for solve_sort ───────────────────────────────────────


def test_sort_basic():
    assert solve_sort([2, 7, 11, 15], 9) == [0, 1]


def test_sort_duplicates():
    assert solve_sort([3, 3], 6) == [0, 1]


def test_sort_no_solution():
    assert solve_sort([1, 2, 3], 10) == [-1, -1]


def test_sort_middle_pair():
    assert solve_sort([1, 5, 3, 8], 8) == [1, 2]


# ── Tests for solve_hash ──────────────────────────────────────


def test_hash_basic():
    assert solve_hash([2, 7, 11, 15], 9) == [0, 1]


def test_hash_duplicates():
    assert solve_hash([3, 3], 6) == [0, 1]


def test_hash_no_solution():
    assert solve_hash([1, 2, 3], 10) == [-1, -1]


def test_hash_middle_pair():
    assert solve_hash([1, 5, 3, 8], 8) == [1, 2]


# ── Tests for solve (default) ─────────────────────────────────


def test_default_uses_hash():
    """Default solve() should return the same result as solve_hash."""
    assert solve([2, 7, 11, 15], 9) == [0, 1]
