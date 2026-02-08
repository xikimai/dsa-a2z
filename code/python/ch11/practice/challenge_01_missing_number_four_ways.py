"""
Challenge 1: Missing Number — Four Ways
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given an array containing n distinct numbers from the range [0, n],
find the one number that is missing — using FOUR different approaches:

1. **solve_sort**: Sort the array, scan for the gap where nums[i] != i.
2. **solve_xor**: XOR all elements with 0..n (duplicates cancel out).
3. **solve_math**: Expected sum n*(n+1)//2 minus actual sum.
4. **solve_hash**: Hash set, check 0..n for missing.

Also implement solve() which delegates to solve_math (the best approach).

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single integer — the missing number.

CONSTRAINTS
-----------
- 1 <= n <= 10^4
- All numbers are distinct and in the range [0, n]

EXAMPLES
--------
Input:
  3 0 1
Output: 2

Input:
  0 1
Output: 2

Input:
  9 6 4 2 3 5 7 0 1
Output: 8

HINT
----
Sort: sort and find where index != value.
XOR: XOR is its own inverse, so x ^ x = 0. XOR all indices and all values.
Math: sum formula n*(n+1)//2 gives expected sum; subtract actual.
Hash: put everything in a set, then check each number 0..n.

INSTRUCTIONS
------------
Replace the `pass` in each function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve_sort(nums: list[int]) -> int:
    """Find missing number using sort approach."""
    pass  # TODO: Replace this with your solution


def solve_xor(nums: list[int]) -> int:
    """Find missing number using XOR approach."""
    pass  # TODO: Replace this with your solution


def solve_math(nums: list[int]) -> int:
    """Find missing number using math (sum) approach."""
    pass  # TODO: Replace this with your solution


def solve_hash(nums: list[int]) -> int:
    """Find missing number using hash set approach."""
    pass  # TODO: Replace this with your solution


def solve(nums: list[int]) -> int:
    """Default solve — uses the math approach."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
