"""
Tests for Warmup 3: Min Cost Climbing Stairs
================================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_warmup_03.py -v
"""
from ch23.practice.warmup_03_min_cost_climbing import solve


def test_basic():
    assert solve([10, 15, 20]) == 15


def test_longer():
    assert solve([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


def test_two_steps():
    assert solve([10, 15]) == 10


def test_equal_costs():
    assert solve([5, 5, 5, 5]) == 10


def test_increasing():
    assert solve([1, 2, 3, 4, 5]) == 6
