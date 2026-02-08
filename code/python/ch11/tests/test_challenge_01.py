"""
Tests for Challenge 1: Missing Number — Four Ways
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_challenge_01.py -v
"""
from ch11.practice.challenge_01_missing_number_four_ways import (
    solve_sort,
    solve_xor,
    solve_math,
    solve_hash,
    solve,
)


def test_sort_basic():
    assert solve_sort([3, 0, 1]) == 2


def test_sort_last():
    assert solve_sort([0, 1]) == 2


def test_sort_large():
    assert solve_sort([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_xor_basic():
    assert solve_xor([3, 0, 1]) == 2


def test_xor_last():
    assert solve_xor([0, 1]) == 2


def test_xor_large():
    assert solve_xor([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_math_basic():
    assert solve_math([3, 0, 1]) == 2


def test_math_first():
    assert solve_math([1]) == 0


def test_math_large():
    assert solve_math([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_hash_basic():
    assert solve_hash([3, 0, 1]) == 2


def test_hash_last():
    assert solve_hash([0]) == 1


def test_hash_large():
    assert solve_hash([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_solve_default():
    assert solve([3, 0, 1]) == 2


def test_solve_first():
    assert solve([1]) == 0
