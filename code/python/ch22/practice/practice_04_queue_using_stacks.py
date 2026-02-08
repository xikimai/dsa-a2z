"""
Practice 4: Queue Using Two Stacks
======================================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Implement a queue using two stacks. Support the following operations:
  - ["enqueue", x]: add x to the back of the queue
  - ["dequeue", 0]: remove and return the front element
  - ["peek", 0]: return the front element without removing
  - ["empty", 0]: return 1 if empty, 0 otherwise

Return a list of results for dequeue, peek, and empty operations.

EXAMPLES
--------
Input: [["enqueue",1],["enqueue",2],["peek",0],["dequeue",0],["empty",0]]
Output: [1, 1, 0]

HINT
----
Use an "in" stack and an "out" stack. Transfer from in to out when out is empty.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(operations: list[list]) -> list[int]:
    """Execute queue-using-stacks operations and return results."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    ops = json.loads(input().strip())
    print(solve(ops))
