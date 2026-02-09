"""
Tests for Warmup 2: Course Schedule I
=======================================
Chapter 28: Topological Sort — Ordering Dependencies

Run with:
    python -m pytest code/python/ch28/tests/test_warmup_02.py -v
"""
from ch28.practice.warmup_02_course_schedule import solve


def test_possible():
    assert solve(2, [[1, 0]]) is True


def test_cycle():
    assert solve(2, [[1, 0], [0, 1]]) is False


def test_chain():
    assert solve(4, [[1, 0], [2, 1], [3, 2]]) is True


def test_single():
    assert solve(1, []) is True


def test_disconnected():
    assert solve(4, [[1, 0], [3, 2]]) is True
