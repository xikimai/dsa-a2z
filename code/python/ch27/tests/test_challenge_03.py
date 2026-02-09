"""
Tests for Challenge 3: Minimum Cost to Make Valid Path
=======================================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_challenge_03.py -v
"""
from ch27.practice.challenge_03_valid_path import solve


def test_needs_changes():
    assert solve([[1,1,2],[1,1,2],[1,1,1]]) == 2


def test_free_path():
    assert solve([[1,1,3],[3,2,2],[1,1,4]]) == 0


def test_all_left():
    assert solve([[2,2,2],[2,2,2]]) == 3


def test_single_cell():
    assert solve([[1]]) == 0
