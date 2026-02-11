"""
Practice 5: Combination Sum
==============================
Chapter 13: Bronze Battle Plan — Putting It All Together

PROBLEM
-------
Given a list of distinct positive integers (candidates) and a target
integer, find all unique combinations where the candidates sum to the
target. Each candidate may be used unlimited times. Return combinations
in sorted order.

INPUT FORMAT
------------
First line: space-separated integers (candidates).
Second line: a single integer (target).

OUTPUT FORMAT
-------------
Each combination on its own line as a list.

CONSTRAINTS
-----------
- 1 <= len(candidates) <= 30
- 1 <= candidates[i] <= 200
- 1 <= target <= 500
- All candidates are distinct

EXAMPLES
--------
Input:
  2 3 6 7
  7
Output:
  [2, 2, 3]
  [7]

Input:
  2 3 5
  8
Output:
  [2, 2, 2, 2]
  [2, 3, 3]
  [3, 5]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(candidates: list[int], target: int) -> list[list[int]]:
    """Return all unique combinations summing to target."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    candidates = list(map(int, input().split()))
    target = int(input())
    result = solve(candidates, target)
    for combo in result:
        print(combo)

