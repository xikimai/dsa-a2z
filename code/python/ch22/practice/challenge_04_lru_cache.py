"""
Challenge 4: LRU Cache
==========================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Design and implement an LRU (Least Recently Used) cache.
Operations are given as a list of [operation, ...args] entries:
  - ["get", key]: return value if key exists, else -1
  - ["put", key, value]: insert or update; evict LRU item if at capacity

Return a list of results for all "get" operations.

CONSTRAINTS
-----------
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 operations

EXAMPLES
--------
capacity = 2
operations = [["put",1,1],["put",2,2],["get",1],["put",3,3],["get",2],["put",4,4],["get",1],["get",3],["get",4]]
Output: [1, -1, -1, 3, 4]

HINT
----
Use an OrderedDict (Python) for O(1) get/put with ordering.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(capacity: int, operations: list[list]) -> list[int]:
    """Execute LRU cache operations and return results of get queries."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    capacity = int(input().strip())
    ops = json.loads(input().strip())
    print(solve(capacity, ops))
