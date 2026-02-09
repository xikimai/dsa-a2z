"""
Practice 4: Longest Increasing Subsequence
==========================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the length of the longest strictly increasing subsequence.

EXAMPLES
--------
  solve([10, 9, 2, 5, 3, 7, 101, 18]) -> 4
  solve([0, 1, 0, 3, 2, 3]) -> 4
  solve([7, 7, 7, 7, 7]) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
O(n^2) DP. dp[i] = length of LIS ending at index i. For each i, check all j < i where nums[j] < nums[i].

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(nums: list[int]) -> int:
    """Return the length of the longest strictly increasing subsequence."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))
