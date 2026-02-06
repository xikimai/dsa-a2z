"""
Solution for Warmup 05: Sum 1 to N
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use a loop to accumulate the sum from 1 to n. The formula n*(n+1)//2
would be O(1), but the point of this exercise is to practice loops.

TIME COMPLEXITY:  O(n) — one loop iteration per number
SPACE COMPLEXITY: O(1) — just the accumulator variable
"""


def solve(n: int) -> int:
    """Return the sum 1 + 2 + ... + n using a loop."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
