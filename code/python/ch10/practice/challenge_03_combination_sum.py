"""
Challenge 3: Combination Sum
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Given an array of distinct positive integers (candidates) and a target
integer, find all unique combinations of candidates that sum to the target.
The same number may be used an unlimited number of times.

Return the combinations sorted (sort candidates first, and the
backtracking order will produce sorted results naturally).

INPUT FORMAT
------------
Line 1: space-separated integers (candidates).
Line 2: a single integer (target).

OUTPUT FORMAT
-------------
One combination per line, printed as a Python list.

CONSTRAINTS
-----------
- 1 <= len(candidates) <= 20
- 1 <= candidates[i] <= 40
- 1 <= target <= 40
- All candidates are distinct.

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

HINT
----
Sort candidates first. Use backtracking with a start index (to avoid
duplicate combinations). At each step, try each candidate from the
start index onward. If the remaining target goes to 0, record the
combination. If a candidate exceeds the remaining target, break early
(since candidates are sorted). Recurse with the SAME start index
to allow reuse of the same number.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(candidates: list[int], target: int) -> list[list[int]]:
    """Find all combinations that sum to target (numbers reusable)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    cands = list(map(int, input().split()))
    target = int(input())
    result = solve(cands, target)
    for combo in result:
        print(combo)
