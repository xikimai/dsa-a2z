"""
Warmup 5: Min Stack
=======================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Design a stack that supports push, pop, top, and getMin — all in O(1).
Operations are given as a list of [operation, value] pairs:
  - ["push", x]: push x onto the stack
  - ["pop", 0]: remove the top element
  - ["top", 0]: return the top element
  - ["getMin", 0]: return the minimum element in the stack

Return a list of results for top and getMin operations.

EXAMPLES
--------
Input: [["push",-2],["push",0],["push",-3],["getMin",0],["pop",0],["top",0],["getMin",0]]
Output: [-3, 0, -2]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(operations: list[list]) -> list[int]:
    """Execute MinStack operations and return results of queries."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    ops = json.loads(input().strip())
    print(solve(ops))
