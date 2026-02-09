"""
Warmup 2: Subset Sum
====================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return True if a subset of nums sums to target.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
1D boolean DP. dp[s] = True if sum s is achievable. Iterate backwards to avoid using same element twice.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(nums: list[int], target: int) -> bool:
    """Return True if a subset of nums sums to target."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    target = int(input().strip())
    print(solve(nums, target))
