"""
Warmup 4: Z-Function
====================
Chapter 32: String Algorithms — Beyond Brute Force

PROBLEM
-------
Return the Z-array of s.

EXAMPLES
--------
  solve("aabxaa") -> [0, 1, 0, 0, 2, 1]
  solve("aaaaa") -> [0, 4, 3, 2, 1]
  solve("abcdef") -> [0, 0, 0, 0, 0, 0]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Use the Z-box optimization: - Maintain [l, r) as the rightmost interval matching a prefix.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(s: str) -> list[int]:
    """Return the Z-array of s."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    s = sys.stdin.read().strip()
    result = solve(s)
    print(" ".join(str(r) for r in result))
