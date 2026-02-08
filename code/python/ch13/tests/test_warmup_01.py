"""
Tests for Warmup 1: Generate All Permutations
Run with: python -m pytest code/python/ch13/tests/test_warmup_01.py -v
"""
from ch13.practice.warmup_01_generate_permutations import solve


def test_three_elements():
    assert solve([1, 2, 3]) == [
        [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
    ]


def test_single_element():
    assert solve([1]) == [[1]]


def test_two_elements():
    assert solve([2, 1]) == [[1, 2], [2, 1]]


def test_four_elements():
    result = solve([1, 2, 3, 4])
    assert len(result) == 24
    assert result[0] == [1, 2, 3, 4]
    assert result[-1] == [4, 3, 2, 1]


def test_negative_numbers():
    assert solve([-1, 0, 1]) == [
        [-1, 0, 1], [-1, 1, 0], [0, -1, 1], [0, 1, -1], [1, -1, 0], [1, 0, -1]
    ]
