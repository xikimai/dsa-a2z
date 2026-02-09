"""
Tests for Practice 4: Kth Order Statistics (Segment Tree on Values)
===================================================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_practice_04.py -v
"""
from ch30.practice.practice_04_kth_order import solve


def test_basic():
    # Insert 5, 3, 7, 1. Multiset = {1, 3, 5, 7}. 2nd smallest = 3.
    # Delete 3. Multiset = {1, 5, 7}. 2nd smallest = 5.
    assert solve([[1, 5], [1, 3], [1, 7], [1, 1], [3, 2], [2, 3], [3, 2]]) == [3, 5]


def test_single():
    assert solve([[1, 10], [3, 1]]) == [10]


def test_duplicates():
    assert solve([[1, 5], [1, 5], [3, 1], [3, 2], [2, 5], [3, 1]]) == [5, 5, 5]
