"""
Tests for Warmup 4: Peak Element in Array
==========================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_warmup_04.py -v
"""
from ch16.practice.warmup_04_peak_element import solve


def _is_peak(arr, idx):
    """Helper: check if idx is a valid peak in arr."""
    if idx < 0 or idx >= len(arr):
        return False
    left_ok = (idx == 0) or (arr[idx] > arr[idx - 1])
    right_ok = (idx == len(arr) - 1) or (arr[idx] > arr[idx + 1])
    return left_ok and right_ok


def test_basic():
    arr = [1, 2, 3, 1]
    assert _is_peak(arr, solve(arr))


def test_multiple_peaks():
    arr = [1, 2, 1, 3, 5, 6, 4]
    assert _is_peak(arr, solve(arr))


def test_single():
    assert solve([1]) == 0


def test_ascending():
    arr = [1, 2, 3, 4, 5]
    assert _is_peak(arr, solve(arr))


def test_descending():
    arr = [5, 4, 3, 2, 1]
    assert _is_peak(arr, solve(arr))


def test_two_ascending():
    arr = [1, 2]
    assert _is_peak(arr, solve(arr))


def test_two_descending():
    arr = [2, 1]
    assert _is_peak(arr, solve(arr))
