"""
Tests for Practice 4: Queue Using Two Stacks
================================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_practice_04.py -v
"""
from ch22.practice.practice_04_queue_using_stacks import solve


def test_basic():
    ops = [["enqueue", 1], ["enqueue", 2], ["peek", 0], ["dequeue", 0], ["empty", 0]]
    assert solve(ops) == [1, 1, 0]


def test_fifo_order():
    ops = [["enqueue", 10], ["enqueue", 20], ["enqueue", 30],
           ["dequeue", 0], ["dequeue", 0], ["dequeue", 0]]
    assert solve(ops) == [10, 20, 30]


def test_empty_check():
    ops = [["empty", 0], ["enqueue", 1], ["empty", 0], ["dequeue", 0], ["empty", 0]]
    assert solve(ops) == [1, 0, 1, 1]


def test_interleaved():
    ops = [["enqueue", 1], ["dequeue", 0], ["enqueue", 2],
           ["enqueue", 3], ["dequeue", 0], ["dequeue", 0]]
    assert solve(ops) == [1, 2, 3]


def test_peek_multiple():
    ops = [["enqueue", 5], ["peek", 0], ["peek", 0], ["dequeue", 0]]
    assert solve(ops) == [5, 5, 5]
