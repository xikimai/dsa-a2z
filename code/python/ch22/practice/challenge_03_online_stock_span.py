"""
Challenge 3: Online Stock Span
=================================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Given a list of daily stock prices, compute the "span" of each day.
The span on day i is the number of consecutive days (ending at day i)
where the price was less than or equal to price[i].

CONSTRAINTS
-----------
- 1 <= len(prices) <= 10^5
- 1 <= prices[i] <= 10^5

EXAMPLES
--------
Input: 100 80 60 70 60 75 85
Output: [1, 1, 1, 2, 1, 4, 6]

HINT
----
Use a monotonic stack storing (price, span) pairs. Pop entries with
price <= current and accumulate their spans.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(prices: list[int]) -> list[int]:
    """Return the stock span for each day."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().strip().split()))
    print(solve(prices))
