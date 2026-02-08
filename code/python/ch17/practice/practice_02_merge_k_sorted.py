"""
Practice 2: Merge K Sorted Arrays
=====================================
Chapter 17: Heaps & Priority Queues — The VIP Line

PROBLEM
-------
Given K sorted arrays, merge them into one sorted array.

INPUT FORMAT
------------
The function receives a list of sorted lists.

OUTPUT FORMAT
-------------
A single sorted list containing all elements.

CONSTRAINTS
-----------
- 0 <= K <= 100
- 0 <= length of each array <= 1000
- -10^9 <= elements <= 10^9

EXAMPLES
--------
Input: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

Input: [[1, 3, 5], [2, 4, 6]]
Output: [1, 2, 3, 4, 5, 6]

Input: [[], [1]]
Output: [1]

HINT
----
Use a min-heap of size K. Push (value, array_index, element_index)
tuples. Pop the minimum, then push the next element from the same array.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arrays: list[list[int]]) -> list[int]:
    """Merge K sorted arrays into one sorted array."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    arrays = json.loads(input().strip())
    print(solve(arrays))
