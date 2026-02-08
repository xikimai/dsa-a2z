"""
Practice 1: Frog Jump with K Steps
===================================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
A frog is on stone 0 and wants to reach stone n-1. The frog can jump
1 to k stones forward. Each stone has a cost (energy to land there).
Return the minimum total cost for the frog to reach the last stone.

EXAMPLES
--------
  costs=[0,3,2,6,1], k=2 -> 3
  costs=[10,20,30,10], k=3 -> 20
  costs=[5], k=1 -> 5

CONSTRAINTS
-----------
- 1 <= len(costs) <= 10^4
- 0 <= costs[i] <= 10^4
- 1 <= k <= len(costs)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(costs: list[int], k: int) -> int:
    """Return minimum cost for frog to reach the last stone."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    parts = input().split()
    k = int(parts[-1])
    costs = list(map(int, parts[:-1]))
    print(solve(costs, k))
