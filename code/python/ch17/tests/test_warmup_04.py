"""
Tests for Warmup 4: Check if Array is a Min-Heap
====================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

Run with:
    python -m pytest code/python/ch17/tests/test_warmup_04.py -v
"""
from ch17.practice.warmup_04_is_heap import solve


def test_valid_heap():
    assert solve([1, 3, 2, 7, 6, 5, 4]) is True


def test_sorted_ascending():
    assert solve([1, 2, 3, 4, 5, 6, 7]) is True


def test_not_a_heap():
    assert solve([7, 3, 2, 1, 6, 5, 4]) is False


def test_single_element():
    assert solve([5]) is True


def test_empty():
    assert solve([]) is True


def test_two_elements_valid():
    assert solve([1, 2]) is True


def test_two_elements_invalid():
    assert solve([2, 1]) is False


def test_large_valid():
    assert solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) is True
