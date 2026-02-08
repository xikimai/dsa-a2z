"""
Solution for Challenge 4: LRU Cache
========================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Use OrderedDict: on get, move key to end (most recent). On put, if key
exists move to end and update; if full, pop the first item (least recent).

TIME COMPLEXITY:  O(1) per operation (amortized)
SPACE COMPLEXITY: O(capacity)
"""

from collections import OrderedDict


def solve(capacity: int, operations: list[list]) -> list[int]:
    """Execute LRU cache operations and return results of get queries."""
    cache = OrderedDict()
    results = []

    for op in operations:
        if op[0] == "get":
            key = op[1]
            if key in cache:
                cache.move_to_end(key)
                results.append(cache[key])
            else:
                results.append(-1)
        elif op[0] == "put":
            key, value = op[1], op[2]
            if key in cache:
                cache.move_to_end(key)
                cache[key] = value
            else:
                if len(cache) >= capacity:
                    cache.popitem(last=False)  # evict LRU
                cache[key] = value

    return results


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    capacity = int(input().strip())
    ops = json.loads(input().strip())
    print(solve(capacity, ops))
