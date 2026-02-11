"""
Challenge 2: Maximum Subarray Sum Three Ways
==============================================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Find the maximum subarray sum using three different approaches:
  1. Brute force: try every subarray, sum each one (O(n^3)).
  2. Prefix sum: precompute prefix sums, try all (l, r) pairs (O(n^2)).
  3. Kadane's algorithm: single pass extend-or-restart (O(n)).

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single line: brute=<answer> prefix=<answer> kadane=<answer>

CONSTRAINTS
-----------
- 1 <= len(arr) <= 1000 (brute force limits)
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  -2 1 -3 4 -1 2 1 -5 4
Output: brute=6 prefix=6 kadane=6

Input:
  -5 -3 -1 -4
Output: brute=-1 prefix=-1 kadane=-1

INSTRUCTIONS
------------
Replace the `pass` in solve_brute(), solve_prefix(), and solve_kadane() with your solutions.
The main block at the bottom handles input/output — don't change it.
"""


def solve_brute(arr: list[int]) -> int:
    """O(n^3) brute force: try every subarray, sum each one."""
    pass  # TODO: Replace this with your solution


def solve_prefix(arr: list[int]) -> int:
    """O(n^2) prefix sum: precompute prefix, try all (l, r) pairs."""
    pass  # TODO: Replace this with your solution


def solve_kadane(arr: list[int]) -> int:
    """O(n) Kadane's: extend-or-restart in one pass."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    b = solve_brute(arr)
    p = solve_prefix(arr)
    k = solve_kadane(arr)
    print(f"brute={b} prefix={p} kadane={k}")

