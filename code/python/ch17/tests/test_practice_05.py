"""
Tests for Practice 5: K Closest Points to Origin
====================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

Run with:
    python -m pytest code/python/ch17/tests/test_practice_05.py -v
"""
from ch17.practice.practice_05_k_closest_points import solve


def test_basic():
    assert solve([[1, 3], [-2, 2]], 1) == [[-2, 2]]


def test_two_closest():
    result = solve([[3, 3], [5, -1], [-2, 4]], 2)
    # dist_sq: 18, 26, 20 -> closest two: [3,3](18), [-2,4](20)
    assert result == [[3, 3], [-2, 4]]


def test_all_points():
    result = solve([[1, 0], [0, 1]], 2)
    assert len(result) == 2


def test_single():
    assert solve([[0, 1]], 1) == [[0, 1]]


def test_origin():
    result = solve([[0, 0], [1, 1]], 1)
    assert result == [[0, 0]]


def test_k_equals_n():
    result = solve([[1, 2], [3, 4], [0, 1]], 3)
    assert len(result) == 3
    assert result[0] == [0, 1]  # closest
