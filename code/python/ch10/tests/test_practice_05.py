"""
Tests for Practice 5: Generate All Subsets
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_practice_05.py -v
"""
from ch10.practice.practice_05_generate_subsets import solve


def test_empty_input():
    assert solve([]) == [[]]


def test_single_element():
    assert solve([1]) == [[], [1]]


def test_three_elements():
    result = solve([1, 2, 3])
    assert len(result) == 8
    expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert result == expected


def test_unordered_input():
    # Input order shouldn't matter — result should be the same
    result = solve([3, 1, 2])
    expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert result == expected
