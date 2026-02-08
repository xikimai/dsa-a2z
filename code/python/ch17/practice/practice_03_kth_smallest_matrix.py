"""
Practice 3: Kth Smallest Element in a Sorted Matrix
=======================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

PROBLEM
-------
Given an n x n matrix where each row and each column is sorted in
ascending order, find the kth smallest element.

INPUT FORMAT
------------
The function receives a 2D matrix and an integer k.

OUTPUT FORMAT
-------------
A single integer — the kth smallest element.

CONSTRAINTS
-----------
- 1 <= n <= 300
- -10^9 <= matrix[i][j] <= 10^9
- 1 <= k <= n^2

EXAMPLES
--------
Input: matrix=[[1,5,9],[10,11,13],[12,13,15]], k=8
Output: 13

Input: matrix=[[-5]], k=1
Output: -5

HINT
----
Use a min-heap. Start by pushing the first element of each row.
Pop the minimum, and push the next element from the same row.
The kth element you pop is the answer.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(matrix: list[list[int]], k: int) -> int:
    """Return the kth smallest element in the sorted matrix."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    data = json.loads(input().strip())
    k = int(input().strip())
    print(solve(data, k))
