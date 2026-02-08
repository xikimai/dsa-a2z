"""
Tests for Practice 1: Top K Frequent Elements
=================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

Run with:
    python -m pytest code/python/ch17/tests/test_practice_01.py -v
"""
from ch17.practice.practice_01_top_k_frequent import solve


def test_basic():
    assert solve([1, 1, 1, 2, 2, 3], 2) == [1, 2]


def test_single():
    assert solve([1], 1) == [1]


def test_all_same():
    assert solve([5, 5, 5, 5], 1) == [5]


def test_three_way():
    assert solve([1, 1, 2, 2, 3, 3], 2) in [
        [1, 2], [1, 3], [2, 3]
    ]


def test_k_equals_unique():
    result = solve([1, 2, 3], 3)
    assert sorted(result) == [1, 2, 3]


def test_larger():
    assert solve([4, 1, -1, 2, -1, 2, 3], 2) == [-1, 2]
