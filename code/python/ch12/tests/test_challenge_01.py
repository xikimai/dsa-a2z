"""
Tests for Challenge 1: Single Number — Three Ways
====================================================
Chapter 12: Bit Manipulation — The Language of Computers

Run with:
    python -m pytest code/python/ch12/tests/test_challenge_01.py -v
"""
from ch12.practice.challenge_01_single_number_three_ways import (
    solve_sort, solve_hash, solve_xor
)


def _test_all_three(nums, expected):
    assert solve_sort(nums[:]) == expected, f"sort failed for {nums}"
    assert solve_hash(nums[:]) == expected, f"hash failed for {nums}"
    assert solve_xor(nums[:]) == expected, f"xor failed for {nums}"


def test_basic():
    _test_all_three([4, 1, 2, 1, 2], 4)


def test_small():
    _test_all_three([2, 2, 1], 1)


def test_single():
    _test_all_three([1], 1)


def test_larger():
    _test_all_three([1, 3, 5, 3, 1], 5)


def test_negative():
    _test_all_three([-1, 2, -1], 2)


def test_zero_single():
    _test_all_three([0, 5, 0], 5)
