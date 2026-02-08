"""
Warmup 2: Highest and Lowest Frequency Element
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given an array of integers, find the element with the highest frequency
and the element with the lowest frequency.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A list of two integers: [element_with_highest_freq, element_with_lowest_freq].

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input:
  1 2 2 3 3 3
Output: [3, 1]

Input:
  10 10 10 20 20 30
Output: [10, 30]

HINT
----
Build a frequency map, then find the keys with the maximum and
minimum values.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Return [element_with_highest_freq, element_with_lowest_freq]."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))
