"""
Tests for Practice 1: Cheapest Flights Within K Stops
======================================================
Chapter 27: Shortest Paths — Finding the Best Route

Run with:
    python -m pytest code/python/ch27/tests/test_practice_01.py -v
"""
from ch27.practice.practice_01_cheapest_flights import solve


def test_basic():
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    assert solve(4, flights, 0, 3, 1) == 700


def test_cheaper_via_stop():
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    assert solve(3, flights, 0, 2, 1) == 200


def test_no_stops():
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    assert solve(3, flights, 0, 2, 0) == 500


def test_unreachable():
    assert solve(3, [[0,1,100]], 0, 2, 1) == -1


def test_direct():
    assert solve(2, [[0,1,50]], 0, 1, 0) == 50
