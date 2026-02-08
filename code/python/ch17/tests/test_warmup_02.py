"""
Tests for Warmup 2: Sort Using Heap (Heapsort)
==================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

Run with:
    python -m pytest code/python/ch17/tests/test_warmup_02.py -v
"""
from ch17.practice.warmup_02_heap_sort import solve


def test_basic():
    assert solve([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]


def test_already_sorted():
    assert solve([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    assert solve([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_single():
    assert solve([1]) == [1]


def test_empty():
    assert solve([]) == []


def test_duplicates():
    assert solve([3, 1, 3, 1, 2]) == [1, 1, 2, 3, 3]


def test_negative():
    assert solve([-3, -1, -2, 0, 2, 1]) == [-3, -2, -1, 0, 1, 2]
