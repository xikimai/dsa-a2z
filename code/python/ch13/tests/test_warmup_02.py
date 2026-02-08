"""
Tests for Warmup 2: Generate All Subsets
Run with: python -m pytest code/python/ch13/tests/test_warmup_02.py -v
"""
from ch13.practice.warmup_02_generate_subsets import solve


def test_three_elements():
    assert solve([1, 2, 3]) == [
        [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
    ]


def test_single_element():
    assert solve([1]) == [[], [1]]


def test_empty():
    assert solve([]) == [[]]


def test_two_elements():
    assert solve([2, 1]) == [[], [1], [2], [1, 2]]


def test_four_elements():
    result = solve([1, 2, 3, 4])
    assert len(result) == 16
    assert result[0] == []
    assert result[-1] == [1, 2, 3, 4]
