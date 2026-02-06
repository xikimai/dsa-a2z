"""
Warmup 3: Mystery Complexity
==============================
Chapter 6: How Fast Is Your Code?

PROBLEM
-------
You ran a mystery function on several input sizes and recorded how many
operations it performed.  Given parallel lists of n_values and counts,
figure out the Big-O complexity class.

Classification rules (using consecutive pairs where n roughly doubles):
  - All counts are the same                  -> "O(1)"
  - Count increases by ~1 when n doubles     -> "O(log n)"
  - Count doubles when n doubles             -> "O(n)"
  - Count quadruples when n doubles          -> "O(n^2)"

INPUT FORMAT
------------
Two lines:
  Line 1: space-separated n_values (integers)
  Line 2: space-separated counts (integers)

OUTPUT FORMAT
-------------
One of: "O(1)", "O(log n)", "O(n)", "O(n^2)"

CONSTRAINTS
-----------
- At least 2 data points
- n_values are in increasing order
- Consecutive n_values roughly double (ratio close to 2)

EXAMPLES
--------
Input:
  1 10 100 1000
  5 5 5 5
Output: O(1)

Input:
  100 200 400 800
  100 200 400 800
Output: O(n)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n_values: list[int], counts: list[int]) -> str:
    """Classify the growth rate from observed (n, count) data points."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n_values = list(map(int, input().split()))
    counts = list(map(int, input().split()))
    print(solve(n_values, counts))
