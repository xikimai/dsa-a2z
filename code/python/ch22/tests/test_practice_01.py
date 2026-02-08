"""
Tests for Practice 1: Daily Temperatures
============================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_practice_01.py -v
"""
from ch22.practice.practice_01_daily_temperatures import solve


def test_basic():
    assert solve([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_increasing():
    assert solve([30, 40, 50, 60]) == [1, 1, 1, 0]


def test_all_same():
    assert solve([30, 30, 30]) == [0, 0, 0]


def test_decreasing():
    assert solve([90, 80, 70, 60]) == [0, 0, 0, 0]


def test_single():
    assert solve([50]) == [0]


def test_two_elements():
    assert solve([50, 60]) == [1, 0]
