"""
Solution for Warmup 04: Count Down
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use range(n, 0, -1) to count from n down to 1, then convert to a list.
You could also use a while loop that decrements a counter.

TIME COMPLEXITY:  O(n) — we visit each number once
SPACE COMPLEXITY: O(n) — the result list has n elements
"""


def solve(n: int) -> list[int]:
    """Return a list counting from n down to 1."""
    return list(range(n, 0, -1))


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
