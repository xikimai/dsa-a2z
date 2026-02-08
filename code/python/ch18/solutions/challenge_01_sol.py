"""
Solution for Challenge 1: Job Sequencing with Deadlines
========================================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
Sort by profit descending. For each job, schedule in latest available
slot before its deadline.

TIME COMPLEXITY:  O(n log n + n * d) where d = max deadline
SPACE COMPLEXITY: O(d)
"""


def solve(jobs: list[list[int]]) -> tuple[int, int]:
    """Return (count of jobs done, total profit)."""
    if not jobs:
        return (0, 0)
    # Sort by profit descending (index 2)
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(j[1] for j in jobs)
    slots = [False] * (max_deadline + 1)
    count = 0
    total_profit = 0
    for job_id, deadline, profit in jobs:
        for t in range(deadline, 0, -1):
            if not slots[t]:
                slots[t] = True
                count += 1
                total_profit += profit
                break
    return (count, total_profit)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    jobs = []
    for _ in range(n):
        parts = list(map(int, input().strip().split()))
        jobs.append(parts)
    count, profit = solve(jobs)
    print(count, profit)
