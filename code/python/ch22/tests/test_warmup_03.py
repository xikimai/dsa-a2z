"""
Tests for Warmup 3: Implement Queue Using Array
===================================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_warmup_03.py -v
"""
from ch22.practice.warmup_03_implement_queue import solve


def test_basic():
    ops = [["enqueue", 1], ["enqueue", 2], ["front", 0], ["dequeue", 0], ["is_empty", 0]]
    assert solve(ops) == [1, 1, 0]


def test_empty_dequeue():
    ops = [["dequeue", 0], ["front", 0], ["is_empty", 0]]
    assert solve(ops) == [-1, -1, 1]


def test_fifo_order():
    ops = [["enqueue", 10], ["enqueue", 20], ["enqueue", 30],
           ["dequeue", 0], ["dequeue", 0], ["dequeue", 0], ["is_empty", 0]]
    assert solve(ops) == [10, 20, 30, 1]


def test_single_element():
    ops = [["enqueue", 5], ["front", 0], ["dequeue", 0], ["is_empty", 0]]
    assert solve(ops) == [5, 5, 1]


def test_interleaved():
    ops = [["enqueue", 1], ["enqueue", 2], ["dequeue", 0],
           ["enqueue", 3], ["front", 0], ["dequeue", 0]]
    assert solve(ops) == [1, 2, 2]
