"""
Solution for Challenge 2: Gas Station
=======================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
If total gas >= total cost, a solution exists. Track running surplus;
when it goes negative, reset start to next station.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(gas: list[int], cost: list[int]) -> int:
    """Return starting station index, or -1 if impossible."""
    if sum(gas) < sum(cost):
        return -1
    start = 0
    tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    gas = list(map(int, input().strip().split()))
    cost = list(map(int, input().strip().split()))
    print(solve(gas, cost))
