"""
Tests for Practice 4: Power Set Using Bitmasks
================================================
Chapter 12: Bit Manipulation — The Language of Computers

Run with:
    python -m pytest code/python/ch12/tests/test_practice_04.py -v
"""
from ch12.practice.practice_04_power_set_bitmask import solve


def test_three_elements():
    result = solve([1, 2, 3])
    assert result == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


def test_empty():
    assert solve([]) == [[]]


def test_single():
    assert solve([5]) == [[], [5]]


def test_two_elements():
    result = solve([10, 20])
    assert result == [[], [10], [20], [10, 20]]


def test_count():
    # Power set of n elements has 2^n subsets
    for n in range(5):
        elements = list(range(1, n + 1))
        result = solve(elements)
        assert len(result) == (1 << n), f"Expected {1 << n} subsets for {n} elements"
