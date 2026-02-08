"""
Tests for Challenge 2: Generate All Permutations
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_challenge_02.py -v
"""
from ch10.practice.challenge_02_generate_permutations import solve


def test_three_elements():
    result = solve([1, 2, 3])
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert len(result) == 6
    assert result == expected


def test_single_element():
    assert solve([1]) == [[1]]


def test_empty():
    assert solve([]) == [[]]


def test_two_elements():
    assert solve([1, 2]) == [[1, 2], [2, 1]]
