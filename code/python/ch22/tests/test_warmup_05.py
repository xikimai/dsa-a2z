"""
Tests for Warmup 5: Min Stack
=================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_warmup_05.py -v
"""
from ch22.practice.warmup_05_min_stack import solve


def test_basic():
    ops = [["push", -2], ["push", 0], ["push", -3],
           ["getMin", 0], ["pop", 0], ["top", 0], ["getMin", 0]]
    assert solve(ops) == [-3, 0, -2]


def test_single():
    ops = [["push", 5], ["top", 0], ["getMin", 0]]
    assert solve(ops) == [5, 5]


def test_decreasing():
    ops = [["push", 3], ["push", 2], ["push", 1],
           ["getMin", 0], ["pop", 0], ["getMin", 0], ["pop", 0], ["getMin", 0]]
    assert solve(ops) == [1, 2, 3]


def test_increasing():
    ops = [["push", 1], ["push", 2], ["push", 3],
           ["getMin", 0], ["pop", 0], ["getMin", 0]]
    assert solve(ops) == [1, 1]


def test_duplicates():
    ops = [["push", 2], ["push", 2], ["push", 1], ["push", 1],
           ["getMin", 0], ["pop", 0], ["getMin", 0],
           ["pop", 0], ["getMin", 0]]
    assert solve(ops) == [1, 1, 2]
