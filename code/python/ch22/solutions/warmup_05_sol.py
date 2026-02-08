"""
Solution for Warmup 5: Min Stack
====================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Maintain two stacks: main stack and min stack. On each push,
also push the current minimum to the min stack.

TIME COMPLEXITY:  O(1) per operation
SPACE COMPLEXITY: O(n)
"""


def solve(operations: list[list]) -> list[int]:
    """Execute MinStack operations and return results of queries."""
    stack = []
    min_stack = []
    results = []

    for op in operations:
        name = op[0]
        if name == "push":
            x = op[1]
            stack.append(x)
            if not min_stack or x <= min_stack[-1]:
                min_stack.append(x)
            else:
                min_stack.append(min_stack[-1])
        elif name == "pop":
            stack.pop()
            min_stack.pop()
        elif name == "top":
            results.append(stack[-1])
        elif name == "getMin":
            results.append(min_stack[-1])
    return results


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    ops = json.loads(input().strip())
    print(solve(ops))
