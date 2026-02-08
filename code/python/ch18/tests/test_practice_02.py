"""
Tests for Practice 2: Fractional Knapsack
===========================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_practice_02.py -v
"""
from ch18.practice.practice_02_fractional_knapsack import solve


def test_basic():
    result = solve(50, [(10, 60), (20, 100), (30, 120)])
    assert abs(result - 240.0) < 1e-6


def test_exact_fit():
    result = solve(30, [(10, 60), (20, 100)])
    assert abs(result - 160.0) < 1e-6


def test_partial_take():
    result = solve(15, [(10, 60), (20, 100)])
    assert abs(result - 85.0) < 1e-6  # All of (10,60) + 5/20 of (20,100)=25


def test_zero_capacity():
    assert solve(0, [(10, 60)]) == 0.0


def test_single_item_fits():
    assert abs(solve(100, [(10, 50)]) - 50.0) < 1e-6


def test_single_item_partial():
    assert abs(solve(5, [(10, 50)]) - 25.0) < 1e-6


def test_empty_items():
    assert solve(10, []) == 0.0
