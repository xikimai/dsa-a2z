"""
Solution for Practice 4: Queue Using Two Stacks
====================================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Use an "in" stack and an "out" stack. Enqueue pushes to in-stack.
Dequeue/peek checks out-stack; if empty, transfers all from in to out.

TIME COMPLEXITY:  O(1) amortized per operation
SPACE COMPLEXITY: O(n)
"""


def solve(operations: list[list]) -> list[int]:
    """Execute queue-using-stacks operations and return results."""
    stack_in = []
    stack_out = []
    results = []

    def transfer():
        while stack_in:
            stack_out.append(stack_in.pop())

    for op in operations:
        name = op[0]
        if name == "enqueue":
            stack_in.append(op[1])
        elif name == "dequeue":
            if not stack_out:
                transfer()
            results.append(stack_out.pop())
        elif name == "peek":
            if not stack_out:
                transfer()
            results.append(stack_out[-1])
        elif name == "empty":
            results.append(1 if not stack_in and not stack_out else 0)
    return results


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    ops = json.loads(input().strip())
    print(solve(ops))
