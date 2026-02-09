"""
Tests for Practice 2: Line Segment Intersection
=================================================
Chapter 34: Computational Geometry & Sweep Line

Run with:
    python -m pytest code/python/ch34/tests/test_practice_02.py -v
"""
from ch34.practice.practice_02_segment_intersection import solve


def test_mixed():
    segments = [
        [[0, 0], [2, 2], [0, 2], [2, 0]],   # X-cross -> True
        [[0, 0], [1, 0], [2, 0], [3, 0]],   # Parallel non-overlap -> False
        [[0, 0], [1, 1], [2, 2], [3, 3]],   # Collinear non-overlap -> False
    ]
    assert solve(segments) == [True, False, False]


def test_touching_endpoint():
    segments = [
        [[0, 0], [1, 1], [1, 1], [2, 0]],   # Touch at (1,1) -> True
    ]
    assert solve(segments) == [True]


def test_parallel_no_intersect():
    segments = [
        [[0, 0], [2, 0], [0, 1], [2, 1]],   # Parallel horizontal -> False
    ]
    assert solve(segments) == [False]


def test_overlapping_collinear():
    segments = [
        [[0, 0], [2, 0], [1, 0], [3, 0]],   # Overlapping on x-axis -> True
    ]
    assert solve(segments) == [True]
