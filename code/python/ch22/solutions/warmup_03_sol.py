"""
Solution for Warmup 3: Implement Queue Using Array
======================================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Use collections.deque for O(1) popleft. Track front with deque[0].

TIME COMPLEXITY:  O(1) per operation
SPACE COMPLEXITY: O(n)
"""

from collections import deque


def solve(operations: list[list]) -> list[int]:
    """Execute queue operations and return results of queries."""
    q = deque()
    results = []
    for op in operations:
        name = op[0]
        if name == "enqueue":
            q.append(op[1])
        elif name == "dequeue":
            if q:
                results.append(q.popleft())
            else:
                results.append(-1)
        elif name == "front":
            if q:
                results.append(q[0])
            else:
                results.append(-1)
        elif name == "is_empty":
            results.append(1 if not q else 0)
    return results


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    ops = json.loads(input().strip())
    print(solve(ops))
