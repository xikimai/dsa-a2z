"""
Solution for Warmup 4: Next Greater Element
================================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Use a monotonic stack (decreasing from bottom to top).
Process from right to left. For each element, pop all stack elements
that are not greater. The remaining top is the NGE.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(arr: list[int]) -> list[int]:
    """Return list of next greater elements for each position."""
    n = len(arr)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
