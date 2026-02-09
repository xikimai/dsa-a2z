"""
Tests for Warmup 2: Unique Paths with Obstacles
==================================================
Chapter 24: Dynamic Programming II — Grids and Paths

Run with:
    python -m pytest code/python/ch24/tests/test_warmup_02.py -v
"""
from ch24.practice.warmup_02_unique_paths_obstacles import solve


def test_basic():
    assert solve([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2


def test_small():
    assert solve([[0, 1], [0, 0]]) == 1


def test_start_blocked():
    assert solve([[1, 0]]) == 0


def test_end_blocked():
    assert solve([[0, 0], [0, 1]]) == 0


def test_no_obstacle():
    assert solve([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 6


def test_single_cell():
    assert solve([[0]]) == 1
