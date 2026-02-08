"""
Warmup 3: Implement Queue Using Array
=========================================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Implement a queue that supports enqueue, dequeue, front, and is_empty operations.
Operations are given as a list of [operation, value] pairs:
  - ["enqueue", x]: add x to the back of the queue
  - ["dequeue", 0]: remove and return the front element (return -1 if empty)
  - ["front", 0]: return the front element without removing (return -1 if empty)
  - ["is_empty", 0]: return 1 if empty, 0 otherwise

Return a list of results for dequeue, front, and is_empty operations.

EXAMPLES
--------
Input: [["enqueue",1],["enqueue",2],["front",0],["dequeue",0],["is_empty",0]]
Output: [1, 1, 0]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(operations: list[list]) -> list[int]:
    """Execute queue operations and return results of queries."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    ops = json.loads(input().strip())
    print(solve(ops))
