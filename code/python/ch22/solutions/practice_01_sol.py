"""
Solution for Practice 1: Daily Temperatures
================================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Use a monotonic stack of indices. Process left to right. For each new
temperature, pop all stack entries with lower temperatures and record
the difference in indices.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(temperatures: list[int]) -> list[int]:
    """Return list of days until a warmer temperature."""
    n = len(temperatures)
    result = [0] * n
    stack = []  # indices

    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    temps = list(map(int, input().strip().split()))
    print(solve(temps))
