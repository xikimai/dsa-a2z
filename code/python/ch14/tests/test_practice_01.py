"""
Tests for Practice 1: Equilibrium Index
==========================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_practice_01.py -v
"""
from ch14.practice.practice_01_equilibrium_index import solve


def test_basic():
    assert solve([-7, 1, 5, 2, -4, 3, 0]) == 3


def test_no_equilibrium():
    assert solve([1, 2, 3]) == -1


def test_equilibrium_at_start():
    assert solve([0, 1, -1]) == 0


def test_equilibrium_at_end():
    assert solve([1, -1, 0]) == 2


def test_single_element():
    assert solve([42]) == 0


def test_two_elements():
    assert solve([1, 1]) == -1


def test_another_case():
    assert solve([1, 3, 5, 2, 2]) == 2
