"""
Challenge 4: Fruit Into Baskets (Max Two Distinct Types)
=========================================================
Chapter 15: Two Pointers & Sliding Window — The Dance of Indices

PROBLEM
-------
You have a row of fruit trees, each bearing a type of fruit (integer).
You have two baskets, and each basket can hold only one type of fruit.
Starting from any tree, pick fruits from consecutive trees. You stop
when you encounter a third type. Return the maximum number of fruits
you can collect.

INPUT FORMAT
------------
A single line of space-separated integers (fruit types).

OUTPUT FORMAT
-------------
A single integer — the maximum number of fruits collectible.

CONSTRAINTS
-----------
- 1 <= len(fruits) <= 10^5
- 0 <= fruits[i] <= 10^5

EXAMPLES
--------
Input:
  1 2 1
Output: 3

Input:
  0 1 2 2
Output: 3

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(fruits: list[int]) -> int:
    """Return maximum fruits collectible with 2 baskets."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    arr = list(map(int, line.split()))
    print(solve(arr))

