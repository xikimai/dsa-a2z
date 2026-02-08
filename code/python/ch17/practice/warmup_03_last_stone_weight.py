"""
Warmup 3: Last Stone Weight
===============================
Chapter 17: Heaps & Priority Queues — The VIP Line

PROBLEM
-------
You have a collection of stones, each with a positive integer weight.
Each turn, you pick the two heaviest stones and smash them together.
If the stones have equal weight, both are destroyed.
If not, the lighter stone is destroyed and the heavier stone's weight
is reduced by the lighter stone's weight.
Return the weight of the last remaining stone (or 0 if none remain).

INPUT FORMAT
------------
A single line of space-separated positive integers (stone weights).

OUTPUT FORMAT
-------------
A single integer — the last stone weight, or 0.

CONSTRAINTS
-----------
- 1 <= len(stones) <= 30
- 1 <= stones[i] <= 1000

EXAMPLES
--------
Input:
  2 7 4 1 8 1
Output: 1

Input:
  1
Output: 1

HINT
----
Use a max-heap. In Python, negate values for max-heap behavior.
Each turn: pop two largest, push their difference (if nonzero).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(stones: list[int]) -> int:
    """Return the weight of the last remaining stone, or 0."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    stones = list(map(int, input().strip().split()))
    print(solve(stones))
