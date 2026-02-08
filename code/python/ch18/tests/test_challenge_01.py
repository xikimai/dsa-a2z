"""
Tests for Challenge 1: Job Sequencing with Deadlines
======================================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_challenge_01.py -v
"""
from ch18.practice.challenge_01_job_sequencing import solve


def test_basic():
    jobs = [[1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30]]
    count, profit = solve(jobs)
    assert count == 2
    assert profit == 60


def test_five_jobs():
    jobs = [[1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15]]
    count, profit = solve(jobs)
    assert count == 2
    assert profit == 127


def test_all_same_deadline():
    jobs = [[1, 1, 10], [2, 1, 20], [3, 1, 30]]
    count, profit = solve(jobs)
    assert count == 1
    assert profit == 30


def test_all_fit():
    jobs = [[1, 1, 10], [2, 2, 20], [3, 3, 30]]
    count, profit = solve(jobs)
    assert count == 3
    assert profit == 60


def test_single():
    jobs = [[1, 1, 50]]
    count, profit = solve(jobs)
    assert count == 1
    assert profit == 50


def test_empty():
    count, profit = solve([])
    assert count == 0
    assert profit == 0
