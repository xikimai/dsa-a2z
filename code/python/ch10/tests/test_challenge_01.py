"""
Tests for Challenge 1: Fibonacci Three Ways
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_challenge_01.py -v
"""
from ch10.practice.challenge_01_fibonacci_three_ways import (
    solve_naive,
    solve_memo,
    solve_iter,
    solve,
)


# ── solve_naive tests (small n only — it's exponential!) ─────────────

def test_naive_zero():
    assert solve_naive(0) == 0


def test_naive_one():
    assert solve_naive(1) == 1


def test_naive_ten():
    assert solve_naive(10) == 55


def test_naive_fifteen():
    assert solve_naive(15) == 610


# ── solve_memo tests ─────────────────────────────────────────────────

def test_memo_zero():
    assert solve_memo(0) == 0


def test_memo_one():
    assert solve_memo(1) == 1


def test_memo_ten():
    assert solve_memo(10) == 55


def test_memo_twenty():
    assert solve_memo(20) == 6765


def test_memo_thirty():
    assert solve_memo(30) == 832040


# ── solve_iter tests ─────────────────────────────────────────────────

def test_iter_zero():
    assert solve_iter(0) == 0


def test_iter_one():
    assert solve_iter(1) == 1


def test_iter_ten():
    assert solve_iter(10) == 55


def test_iter_twenty():
    assert solve_iter(20) == 6765


def test_iter_thirty():
    assert solve_iter(30) == 832040


# ── solve (default) test ─────────────────────────────────────────────

def test_solve_thirty():
    assert solve(30) == 832040
