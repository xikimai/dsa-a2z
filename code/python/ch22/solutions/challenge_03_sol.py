"""
Solution for Challenge 3: Online Stock Span
================================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Use a monotonic stack storing (price, span) pairs. For each new price,
pop all entries with price <= current and accumulate their spans.

TIME COMPLEXITY:  O(1) amortized per call
SPACE COMPLEXITY: O(n)
"""


def solve(prices: list[int]) -> list[int]:
    """Return the stock span for each day."""
    stack = []  # (price, span)
    result = []

    for price in prices:
        span = 1
        while stack and stack[-1][0] <= price:
            span += stack[-1][1]
            stack.pop()
        stack.append((price, span))
        result.append(span)

    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().strip().split()))
    print(solve(prices))
