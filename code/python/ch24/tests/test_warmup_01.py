"""
Tests for Warmup 1: Unique Paths
===================================
Chapter 24: Dynamic Programming II — Grids and Paths

Run with:
    python -m pytest code/python/ch24/tests/test_warmup_01.py -v
"""
from ch24.practice.warmup_01_unique_paths import solve


def test_basic():
    assert solve(3, 7) == 28


def test_single_cell():
    assert solve(1, 1) == 1


def test_single_column():
    assert solve(3, 2) == 3


def test_single_row():
    assert solve(2, 3) == 3


def test_large():
    assert solve(10, 10) == 48620


def test_one_row():
    assert solve(1, 5) == 1


def test_one_col():
    assert solve(5, 1) == 1
