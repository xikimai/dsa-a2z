"""
Tests for Practice 2: Accounts Merge
======================================
Chapter 29: Union-Find & Minimum Spanning Trees

Run with:
    python -m pytest code/python/ch29/tests/test_practice_02.py -v
"""
from ch29.practice.practice_02_accounts_merge import solve


def test_basic_merge():
    accounts = [
        ["John", "j1@m", "j2@m"],
        ["John", "j1@m", "j3@m"],
        ["Mary", "m1@m"],
    ]
    result = solve(accounts)
    assert result == [
        ["John", "j1@m", "j2@m", "j3@m"],
        ["Mary", "m1@m"],
    ]


def test_no_merge():
    accounts = [
        ["John", "j1@m"],
        ["John", "j2@m"],
    ]
    result = solve(accounts)
    assert result == [
        ["John", "j1@m"],
        ["John", "j2@m"],
    ]


def test_all_merge():
    accounts = [
        ["A", "a@m", "b@m"],
        ["A", "b@m", "c@m"],
        ["A", "c@m", "d@m"],
    ]
    result = solve(accounts)
    assert result == [["A", "a@m", "b@m", "c@m", "d@m"]]
