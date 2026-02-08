"""
Practice 3: Count Occurrences
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Given an array of integers and a target value, count how many times
the target appears in the array using recursion. Do not use any
built-in count methods.

INPUT FORMAT
------------
Line 1: space-separated integers (the array).
Line 2: a single integer (the target).

OUTPUT FORMAT
-------------
A single integer — the count of target in the array.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^4
- -10^6 <= arr[i] <= 10^6
- -10^6 <= target <= 10^6

EXAMPLES
--------
Input:
  1 2 3 2 4 2
  2
Output: 3

Input:
  5 5 5 5 5
  5
Output: 5

Input:
  1 2 3
  7
Output: 0

HINT
----
Use a helper function with an index parameter. Base case: index
reaches the end of the array (return 0). At each step, add 1 if
the current element matches the target, then recurse on the next index.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], target: int) -> int:
    """Count occurrences of target in arr, recursively."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
