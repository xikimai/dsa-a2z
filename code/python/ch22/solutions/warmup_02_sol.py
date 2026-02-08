"""
Solution for Warmup 2: Implement Stack Using Array
======================================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Use a Python list as the underlying storage. Append for push, pop for pop.

TIME COMPLEXITY:  O(1) per operation (amortized)
SPACE COMPLEXITY: O(n)
"""


def solve(operations: list[list]) -> list[int]:
    """Execute stack operations and return results of queries."""
    stack = []
    results = []
    for op in operations:
        name = op[0]
        if name == "push":
            stack.append(op[1])
        elif name == "pop":
            if stack:
                results.append(stack.pop())
            else:
                results.append(-1)
        elif name == "top":
            if stack:
                results.append(stack[-1])
            else:
                results.append(-1)
        elif name == "is_empty":
            results.append(1 if not stack else 0)
    return results


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    ops = json.loads(input().strip())
    print(solve(ops))
