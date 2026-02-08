"""
Practice 5: K Closest Points to Origin
==========================================
Chapter 17: Heaps & Priority Queues — The VIP Line

PROBLEM
-------
Given an array of points on the X-Y plane and an integer k, return the k
closest points to the origin (0, 0). Distance is Euclidean (but you can
compare squared distances to avoid floating point).
Return points sorted by distance (ascending), with ties broken by x then y.

INPUT FORMAT
------------
The function receives a list of [x, y] points and an integer k.

OUTPUT FORMAT
-------------
A list of the k closest [x, y] points, sorted by distance.

CONSTRAINTS
-----------
- 1 <= k <= len(points) <= 10^4
- -10^4 <= x, y <= 10^4

EXAMPLES
--------
Input: points=[[1,3],[-2,2]], k=1
Output: [[-2, 2]]
Explanation: dist(1,3) = sqrt(10), dist(-2,2) = sqrt(8). Closer: [-2,2]

Input: points=[[3,3],[5,-1],[-2,4]], k=2
Output: [[3, 3], [-2, 4]]

HINT
----
Use a max-heap of size k (negate distances). For each point, push its
negated distance. If the heap exceeds size k, pop the farthest point.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(points: list[list[int]], k: int) -> list[list[int]]:
    """Return the k closest points to origin, sorted by distance."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    points = json.loads(input().strip())
    k = int(input().strip())
    print(solve(points, k))
