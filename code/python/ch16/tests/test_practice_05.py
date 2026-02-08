"""
Tests for Practice 5: Minimum Pages Allocation
================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_practice_05.py -v
"""
from ch16.practice.practice_05_min_pages import solve


def test_basic():
    assert solve([12, 34, 67, 90], 2) == 113


def test_single_student():
    assert solve([10, 20, 30], 1) == 60


def test_one_book_each():
    assert solve([10, 20, 30], 3) == 30


def test_equal_pages():
    assert solve([25, 25, 25, 25], 2) == 50


def test_more_students_than_books():
    assert solve([10, 20], 3) == -1


def test_large_last_book():
    assert solve([5, 5, 5, 100], 2) == 100


def test_single_book():
    assert solve([50], 1) == 50
