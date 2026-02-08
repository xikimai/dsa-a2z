"""
Tests for Practice 4: Remove Nth Node From End
================================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_practice_04.py -v
"""
from ch21.practice.practice_04_remove_nth_from_end import solve


def test_remove_second_from_end():
    assert solve([1, 2, 3, 4, 5], 2) == [1, 2, 3, 5]


def test_remove_last():
    assert solve([1, 2], 1) == [1]


def test_remove_only_element():
    assert solve([1], 1) == []


def test_remove_first_from_end():
    assert solve([1, 2, 3], 1) == [1, 2]


def test_remove_head():
    assert solve([1, 2, 3], 3) == [2, 3]


def test_remove_from_two_element_list():
    assert solve([1, 2], 2) == [2]
