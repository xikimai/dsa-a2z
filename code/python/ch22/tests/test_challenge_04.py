"""
Tests for Challenge 4: LRU Cache
====================================
Chapter 22: Stacks & Queues — Order Matters

Run with:
    python -m pytest code/python/ch22/tests/test_challenge_04.py -v
"""
from ch22.practice.challenge_04_lru_cache import solve


def test_basic():
    ops = [["put", 1, 1], ["put", 2, 2], ["get", 1],
           ["put", 3, 3], ["get", 2],
           ["put", 4, 4], ["get", 1], ["get", 3], ["get", 4]]
    assert solve(2, ops) == [1, -1, -1, 3, 4]


def test_update_existing():
    ops = [["put", 1, 1], ["put", 1, 10], ["get", 1]]
    assert solve(2, ops) == [10]


def test_get_missing():
    ops = [["get", 1]]
    assert solve(1, ops) == [-1]


def test_eviction_order():
    ops = [["put", 1, 1], ["put", 2, 2], ["put", 3, 3], ["get", 1], ["get", 2], ["get", 3]]
    # capacity 2: put(1,1), put(2,2) — full. put(3,3) evicts 1.
    assert solve(2, ops) == [-1, 2, 3]


def test_get_refreshes():
    # get(1) refreshes key 1, so key 2 becomes LRU
    ops = [["put", 1, 1], ["put", 2, 2], ["get", 1],
           ["put", 3, 3], ["get", 2], ["get", 1], ["get", 3]]
    # After get(1): LRU order = 2,1. put(3,3) evicts 2.
    assert solve(2, ops) == [1, -1, 1, 3]


def test_capacity_one():
    ops = [["put", 1, 10], ["get", 1], ["put", 2, 20], ["get", 1], ["get", 2]]
    assert solve(1, ops) == [10, -1, 20]
