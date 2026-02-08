"""
Tests for Challenge 2: Trapping Rain Water
=============================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_challenge_02.py -v
"""
from ch22.practice.challenge_02_trapping_rain_water import solve


def test_basic():
    assert solve([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_v_shape():
    assert solve([4, 2, 0, 3, 2, 5]) == 9


def test_no_trap():
    assert solve([1, 2, 3]) == 0


def test_no_trap_decreasing():
    assert solve([3, 2, 1]) == 0


def test_empty():
    assert solve([]) == 0


def test_single():
    assert solve([5]) == 0


def test_two():
    assert solve([1, 2]) == 0


def test_all_same():
    assert solve([3, 3, 3]) == 0


def test_simple_pool():
    assert solve([3, 0, 3]) == 3
