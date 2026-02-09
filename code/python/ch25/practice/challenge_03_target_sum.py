"""
Challenge 3: Target Sum
=======================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the number of ways to assign +/- to reach target.

EXAMPLES
--------
  solve([1, 1, 1, 1, 1], 3) -> 5
  solve([1], 1) -> 1
  solve([1, 0], 1) -> 2

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Reduce to subset sum count. P + N = total, P - N = target. So P = (total + target) / 2. Count subsets summing to P.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(nums: list[int], target: int) -> int:
    """Return the number of ways to assign +/- to reach target."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    target = int(input().strip())
    print(solve(nums, target))
