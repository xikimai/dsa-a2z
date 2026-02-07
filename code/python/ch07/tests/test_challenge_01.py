"""
Tests for Challenge 1: GCD Three Ways
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_challenge_01.py -v
"""

from ch07.practice.challenge_01_gcd_three_ways import (
    solve,
    solve_subtract,
    solve_euclidean,
    solve_extended,
)


# ── Tests for solve_subtract ──────────────────────────────────────

def test_subtract_basic():
    assert solve_subtract(48, 18) == 6


def test_subtract_coprime():
    assert solve_subtract(7, 13) == 1


def test_subtract_equal():
    assert solve_subtract(10, 10) == 10


# ── Tests for solve_euclidean ─────────────────────────────────────

def test_euclidean_basic():
    assert solve_euclidean(48, 18) == 6


def test_euclidean_coprime():
    assert solve_euclidean(7, 13) == 1


def test_euclidean_zero():
    assert solve_euclidean(0, 5) == 5


def test_euclidean_large():
    assert solve_euclidean(1000000000, 999999999) == 1


# ── Tests for solve_extended ──────────────────────────────────────

def test_extended_basic():
    result = solve_extended(35, 15)
    assert result[0] == 5
    assert 35 * result[1] + 15 * result[2] == 5


def test_extended_coprime():
    result = solve_extended(7, 11)
    assert result[0] == 1
    assert 7 * result[1] + 11 * result[2] == 1


def test_extended_equal():
    result = solve_extended(6, 6)
    assert result[0] == 6
    assert 6 * result[1] + 6 * result[2] == 6


# ── Tests for solve (default) ────────────────────────────────────

def test_default_uses_euclidean():
    assert solve(48, 18) == 6
