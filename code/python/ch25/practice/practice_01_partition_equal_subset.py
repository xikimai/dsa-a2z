"""
Practice 1: Partition Equal Subset Sum
======================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return True if nums can be split into two equal-sum subsets.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Reduce to Subset Sum: if total is odd, impossible. Otherwise find if a subset sums to total // 2.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(nums: list[int]) -> bool:
    """Return True if nums can be split into two equal-sum subsets."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))
