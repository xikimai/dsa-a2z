"""
Tests for Challenge 3: N-Queens All Solutions
Run with: python -m pytest code/python/ch13/tests/test_challenge_03.py -v
"""
from ch13.practice.challenge_03_n_queens_all import solve


def test_n1():
    assert solve(1) == [["Q"]]


def test_n2():
    assert solve(2) == []


def test_n3():
    assert solve(3) == []


def test_n4():
    result = solve(4)
    assert len(result) == 2
    assert [".Q..", "...Q", "Q...", "..Q."] in result
    assert ["..Q.", "Q...", "...Q", ".Q.."] in result


def test_n5():
    result = solve(5)
    assert len(result) == 10


def test_solutions_sorted():
    result = solve(4)
    assert result == sorted(result)


def test_n6():
    result = solve(6)
    assert len(result) == 4
