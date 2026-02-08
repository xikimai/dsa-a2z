"""
Challenge 1: Job Sequencing with Deadlines
============================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
Given jobs with [id, deadline, profit], schedule jobs to maximize
total profit. Each job takes 1 unit of time and must finish by its deadline.

EXAMPLES
--------
>>> solve([[1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30]])
(2, 60)

CONSTRAINTS
-----------
- 0 <= n <= 10^4
- 1 <= deadline <= n
- 1 <= profit <= 10^5
"""


def solve(jobs: list[list[int]]) -> tuple[int, int]:
    """Return (count of jobs done, total profit)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    jobs = []
    for _ in range(n):
        parts = list(map(int, input().strip().split()))
        jobs.append(parts)
    count, profit = solve(jobs)
    print(count, profit)
