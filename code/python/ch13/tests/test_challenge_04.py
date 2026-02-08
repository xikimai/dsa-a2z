"""
Tests for Challenge 4: Fence Painting (USACO Bronze Style)
Run with: python -m pytest code/python/ch13/tests/test_challenge_04.py -v
"""
from ch13.practice.challenge_04_fence_painting import solve


def test_overlapping():
    assert solve([[1, 5], [3, 8]]) == 7


def test_non_overlapping():
    assert solve([[1, 3], [5, 7]]) == 4


def test_contained():
    assert solve([[1, 10], [2, 5], [3, 7]]) == 9


def test_single_segment():
    assert solve([[0, 5]]) == 5


def test_adjacent():
    assert solve([[1, 3], [3, 5]]) == 4


def test_fully_overlapping():
    assert solve([[1, 5], [1, 5]]) == 4


def test_multiple_groups():
    assert solve([[1, 3], [5, 7], [10, 15]]) == 9
