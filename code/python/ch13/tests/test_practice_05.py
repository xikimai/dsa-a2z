"""
Tests for Practice 5: Combination Sum
Run with: python -m pytest code/python/ch13/tests/test_practice_05.py -v
"""
from ch13.practice.practice_05_combination_sum import solve


def test_basic():
    assert solve([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]


def test_three_candidates():
    assert solve([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


def test_no_solution():
    assert solve([2], 1) == []


def test_single_candidate():
    assert solve([1], 3) == [[1, 1, 1]]


def test_larger_target():
    result = solve([2, 3, 7], 9)
    assert [2, 2, 2, 3] in result
    assert [2, 7] in result
    assert [3, 3, 3] in result


def test_single_element_match():
    assert solve([5], 5) == [[5]]
