"""
Tests for Warmup 2: Implement Stack Using Array
===================================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_warmup_02.py -v
"""
from ch22.practice.warmup_02_implement_stack import solve


def test_basic():
    ops = [["push", 1], ["push", 2], ["top", 0], ["pop", 0], ["is_empty", 0]]
    assert solve(ops) == [2, 2, 0]


def test_empty_pop():
    ops = [["pop", 0], ["top", 0], ["is_empty", 0]]
    assert solve(ops) == [-1, -1, 1]


def test_push_pop_sequence():
    ops = [["push", 10], ["push", 20], ["push", 30],
           ["pop", 0], ["pop", 0], ["pop", 0], ["is_empty", 0]]
    assert solve(ops) == [30, 20, 10, 1]


def test_single_element():
    ops = [["push", 5], ["top", 0], ["pop", 0], ["is_empty", 0]]
    assert solve(ops) == [5, 5, 1]


def test_multiple_tops():
    ops = [["push", 7], ["top", 0], ["top", 0], ["pop", 0]]
    assert solve(ops) == [7, 7, 7]
