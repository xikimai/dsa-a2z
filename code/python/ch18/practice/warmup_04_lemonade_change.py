"""
Warmup 4: Lemonade Change
===========================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
Lemonade costs $5. Customers pay $5, $10, or $20.
Can you give correct change to every customer?
You start with no change.

EXAMPLES
--------
>>> solve([5, 5, 5, 10, 20])
True
>>> solve([5, 5, 10, 10, 20])
False

CONSTRAINTS
-----------
- 1 <= len(bills) <= 10^5
- bills[i] in {5, 10, 20}
"""


def solve(bills: list[int]) -> bool:
    """Return True if you can make change for every customer."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    bills = list(map(int, input().strip().split()))
    print(solve(bills))
