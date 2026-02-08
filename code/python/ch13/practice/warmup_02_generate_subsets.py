"""
Solution for Warmup 2: Generate All Subsets
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Recursion: for each element, include or exclude.
Sort inputs and results for deterministic output.

TIME COMPLEXITY:  O(2^n * n)
SPACE COMPLEXITY: O(n) — recursion depth
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Return all subsets sorted by length then lexicographically."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))
    else:
        nums = []
    result = solve(nums)
    for s in result:
        print(s)

