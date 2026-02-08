"""
Tests for Warmup 1: Climbing Stairs
=======================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_warmup_01.py -v
"""
from ch23.practice.warmup_01_climbing_stairs import solve


def test_one_step():
    assert solve(1) == 1


def test_two_steps():
    assert solve(2) == 2


def test_three_steps():
    assert solve(3) == 3


def test_five_steps():
    assert solve(5) == 8


def test_ten_steps():
    assert solve(10) == 89


def test_large():
    assert solve(45) == 1836311903
