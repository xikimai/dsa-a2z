"""
Warmup 2: Implement Stack Using Array
=========================================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Implement a stack that supports push, pop, top, and is_empty operations.
Operations are given as a list of [operation, value] pairs:
  - ["push", x]: push x onto the stack
  - ["pop", 0]: pop and return the top element (return -1 if empty)
  - ["top", 0]: return the top element without removing (return -1 if empty)
  - ["is_empty", 0]: return 1 if empty, 0 otherwise

Return a list of results for pop, top, and is_empty operations.

EXAMPLES
--------
Input: [["push",1],["push",2],["top",0],["pop",0],["is_empty",0]]
Output: [2, 2, 0]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(operations: list[list]) -> list[int]:
    """Execute stack operations and return results of queries."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    ops = json.loads(input().strip())
    print(solve(ops))
