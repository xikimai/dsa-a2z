"""
Tests for Warmup 3: Simulate Robot Moves
Run with: python -m pytest code/python/ch13/tests/test_warmup_03.py -v
"""
from ch13.practice.warmup_03_simulate_robot import solve


def test_cancel_out():
    assert solve("UUDDLR") == [0, 0]


def test_all_right_up():
    assert solve("RRRUUU") == [3, 3]


def test_empty():
    assert solve("") == [0, 0]


def test_all_left():
    assert solve("LLLL") == [-4, 0]


def test_all_down():
    assert solve("DDD") == [0, -3]


def test_complex_path():
    assert solve("UURRDDDLL") == [0, -1]
