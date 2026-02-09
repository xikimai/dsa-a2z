"""
Tests for Practice 2: Parallel Courses
========================================
Chapter 28: Topological Sort — Ordering Dependencies

Run with:
    python -m pytest code/python/ch28/tests/test_practice_02.py -v
"""
from ch28.practice.practice_02_parallel_courses import solve


def test_basic():
    assert solve(3, [[1, 3], [2, 3]]) == 2


def test_cycle():
    assert solve(3, [[1, 2], [2, 3], [3, 1]]) == -1


def test_diamond():
    assert solve(4, [[1, 2], [1, 3], [2, 4], [3, 4]]) == 3


def test_single():
    assert solve(1, []) == 1


def test_chain():
    assert solve(3, [[1, 2], [2, 3]]) == 3
