"""
Challenge 4: Candy Distribution
==================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
Children stand in a line with ratings. Each child gets >= 1 candy.
Children with a higher rating than a neighbor must get more candies
than that neighbor. Minimize total candies.

EXAMPLES
--------
>>> solve([1, 0, 2])
5
>>> solve([1, 2, 2])
4

CONSTRAINTS
-----------
- 1 <= n <= 10^5
- 0 <= ratings[i] <= 10^5
"""


def solve(ratings: list[int]) -> int:
    """Return minimum total candies needed."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    ratings = list(map(int, input().strip().split()))
    print(solve(ratings))
