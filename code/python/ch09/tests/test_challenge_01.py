"""
Tests for Challenge 1: Find Peak Element
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_challenge_01.py -v
"""
from ch09.practice.challenge_01_find_peak import solve, solve_linear, solve_binary


def is_peak(arr, idx):
    """Helper: verify that idx is a valid peak in arr."""
    if idx < 0 or idx >= len(arr):
        return False
    if len(arr) == 1:
        return True
    left_ok = (idx == 0) or (arr[idx] > arr[idx - 1])
    right_ok = (idx == len(arr) - 1) or (arr[idx] > arr[idx + 1])
    return left_ok and right_ok


def test_simple_peak():
    arr = [1, 2, 3, 1]
    assert is_peak(arr, solve(arr))


def test_multiple_peaks():
    arr = [1, 2, 1, 3, 5, 6, 4]
    assert is_peak(arr, solve(arr))


def test_single_element():
    arr = [1]
    assert is_peak(arr, solve(arr))


def test_descending():
    arr = [3, 2, 1]
    assert is_peak(arr, solve(arr))


def test_ascending():
    arr = [1, 2, 3]
    assert is_peak(arr, solve(arr))


def test_larger_array():
    arr = [5, 10, 20, 15, 7, 3]
    assert is_peak(arr, solve(arr))


def test_linear_simple():
    arr = [1, 2, 3, 1]
    assert is_peak(arr, solve_linear(arr))


def test_linear_multiple_peaks():
    arr = [1, 2, 1, 3, 5, 6, 4]
    assert is_peak(arr, solve_linear(arr))


def test_binary_simple():
    arr = [1, 2, 3, 1]
    assert is_peak(arr, solve_binary(arr))


def test_binary_multiple_peaks():
    arr = [1, 2, 1, 3, 5, 6, 4]
    assert is_peak(arr, solve_binary(arr))
