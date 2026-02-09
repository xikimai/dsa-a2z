"""
Practice 4: Repeated String Match
=================================
Chapter 32: String Algorithms — Beyond Brute Force

PROBLEM
-------
Return minimum repeats of a so that b is a substring, or -1 if impossible.

EXAMPLES
--------
  solve("abcd", "cdabcdab") -> 3
  solve("a", "aa") -> 2
  solve("abc", "xyz") -> -1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
The minimum number of repeats needed is at least ceil(len(b) / len(a)). We try that many repeats and one more. If b is not found as a substring

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(a: str, b: str) -> int:
    """Return minimum repeats of a so that b is a substring, or -1 if impossible."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    print(solve(data[0], data[1]))
