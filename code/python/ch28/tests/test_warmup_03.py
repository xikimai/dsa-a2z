"""
Tests for Warmup 3: Course Schedule II
========================================
Chapter 28: Topological Sort — Ordering Dependencies

Run with:
    python -m pytest code/python/ch28/tests/test_warmup_03.py -v
"""
from ch28.practice.warmup_03_course_schedule_ii import solve


def is_valid_course_order(numCourses, prerequisites, order):
    """Validate that order is a valid course ordering."""
    if len(order) != numCourses:
        return False
    if set(order) != set(range(numCourses)):
        return False
    pos = {course: i for i, course in enumerate(order)}
    for a, b in prerequisites:
        # b must come before a
        if pos[b] >= pos[a]:
            return False
    return True


def test_basic():
    prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result = solve(4, prereqs)
    assert is_valid_course_order(4, prereqs, result)


def test_cycle():
    assert solve(2, [[1, 0], [0, 1]]) == []


def test_single():
    assert solve(1, []) == [0]


def test_chain():
    prereqs = [[1, 0], [2, 1]]
    result = solve(3, prereqs)
    assert is_valid_course_order(3, prereqs, result)


def test_no_prereqs():
    result = solve(3, [])
    assert is_valid_course_order(3, [], result)
