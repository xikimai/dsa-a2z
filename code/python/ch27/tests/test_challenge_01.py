"""
Tests for Challenge 1: Minimum Obstacle Removal to Reach Corner
=================================================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_challenge_01.py -v
"""
from ch27.practice.challenge_01_obstacle_removal import solve


def test_basic():
    assert solve([[0,1,1],[1,1,0],[1,1,0]]) == 2


def test_clear_path():
    assert solve([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]) == 0


def test_single_cell():
    assert solve([[0]]) == 0


def test_all_blocked():
    assert solve([[0,1],[1,0]]) == 1
