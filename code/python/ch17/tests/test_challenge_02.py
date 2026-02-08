"""
Tests for Challenge 2: Task Scheduler
=========================================
Chapter 17: Heaps & Priority Queues — The VIP Line

Run with:
    python -m pytest code/python/ch17/tests/test_challenge_02.py -v
"""
from ch17.practice.challenge_02_task_scheduler import solve


def test_basic():
    assert solve(["A", "A", "A", "B", "B", "B"], 2) == 8


def test_no_cooldown():
    assert solve(["A", "A", "A", "B", "B", "B"], 0) == 6


def test_large_cooldown():
    assert solve(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E"], 2) == 16


def test_single_task():
    assert solve(["A"], 2) == 1


def test_all_different():
    assert solve(["A", "B", "C", "D"], 2) == 4


def test_two_same():
    assert solve(["A", "A"], 2) == 4


def test_zero_cooldown_many():
    assert solve(["A", "A", "A", "B", "B", "C"], 0) == 6
