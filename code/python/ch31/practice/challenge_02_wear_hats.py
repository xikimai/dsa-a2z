"""
Challenge 2: Number of Ways to Wear Hats
========================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

PROBLEM
-------
Return number of ways to assign distinct hats, mod 10^9+7.

EXAMPLES
--------
  solve(2, [[1, 2], [1, 2]]) -> 2
  solve(2, [[1, 2, 3], [1, 2]]) -> 4
  solve(1, [[1]]) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Bitmask DP on people (n <= 10, so 2^10 = 1024 states). Iterate over hats 1..40. For each hat, either skip it or assign

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

MOD = 10**9 + 7


def solve(n: int, hats: list[list[int]]) -> int:
    """Return number of ways to assign distinct hats, mod 10^9+7."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    hats = []
    for _ in range(n):
        cnt = int(tokens[idx]); idx += 1
        person_hats = []
        for _ in range(cnt):
            person_hats.append(int(tokens[idx])); idx += 1
        hats.append(person_hats)
    print(solve(n, hats))
