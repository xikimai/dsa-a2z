"""
Tests for Practice 1: Subsets Using Bitmasks
Run with: python -m pytest code/python/ch13/tests/test_practice_01.py -v
"""
from ch13.practice.practice_01_subsets_bitmask import solve


def test_three_elements():
    assert solve([1, 2, 3]) == [
        [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
    ]


def test_single():
    assert solve([5]) == [[], [5]]


def test_empty():
    assert solve([]) == [[]]


def test_two_elements():
    assert solve([3, 1]) == [[], [1], [3], [1, 3]]


def test_four_elements():
    result = solve([4, 2, 3, 1])
    assert len(result) == 16
    assert result[0] == []
    assert result[-1] == [1, 2, 3, 4]
