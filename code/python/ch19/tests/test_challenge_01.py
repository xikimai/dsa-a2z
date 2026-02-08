"""
Tests for Challenge 1: Number of Provinces
============================================
Chapter 19: Graphs I — Exploring Networks

Run with:
    python -m pytest code/python/ch19/tests/test_challenge_01.py -v
"""
from ch19.practice.challenge_01_num_provinces import solve


def test_two_provinces():
    assert solve([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2


def test_three_provinces():
    assert solve([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3


def test_one_province():
    assert solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 1


def test_single_city():
    assert solve([[1]]) == 1


def test_chain():
    assert solve([
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 1, 1],
        [0, 0, 1, 1]
    ]) == 1
