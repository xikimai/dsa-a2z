"""
Solution for Warmup 4: Sum of 1 to N
============================================
Chapter 6: How Fast Is Your Code?

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Implement all three methods:
  1. O(n) loop: straightforward accumulation
  2. O(1) formula: n*(n+1)//2
  3. O(n^2) nested: for each i, add 1 exactly i times

TIME COMPLEXITY:  O(n^2) overall (dominated by method 3)
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> list[int]:
    """Return [loop_result, formula_result, nested_result]."""
    # Method 1: O(n) loop
    loop_result = 0
    for i in range(1, n + 1):
        loop_result += i

    # Method 2: O(1) formula
    formula_result = n * (n + 1) // 2

    # Method 3: O(n^2) nested loop
    nested_result = 0
    for i in range(1, n + 1):
        for _ in range(i):
            nested_result += 1

    return [loop_result, formula_result, nested_result]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    result = solve(n)
    print(" ".join(map(str, result)))
