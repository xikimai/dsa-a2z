"""
Tests for Challenge 2: Course Schedule
========================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_challenge_02.py -v
"""
from ch19.practice.challenge_02_course_schedule import solve


def test_no_cycle():
    assert solve(2, [[1, 0]]) is True


def test_has_cycle():
    assert solve(2, [[1, 0], [0, 1]]) is False


def test_chain():
    assert solve(4, [[1, 0], [2, 1], [3, 2]]) is True


def test_no_prereqs():
    assert solve(3, []) is True


def test_complex_cycle():
    assert solve(4, [[1, 0], [2, 1], [0, 2]]) is False


def test_disconnected_no_cycle():
    assert solve(4, [[1, 0], [3, 2]]) is True
