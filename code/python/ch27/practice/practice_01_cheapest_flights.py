"""
Practice 1: Cheapest Flights Within K Stops
===========================================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return cheapest price from src to dst with at most k stops.

EXAMPLES
--------
  solve(4, flights, 0, 3, 1) -> 700
  solve(3, flights, 0, 2, 1) -> 200
  solve(3, flights, 0, 2, 0) -> 500

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Modified Bellman-Ford with at most k+1 relaxation rounds. Use a copy of dist each round to prevent cascading updates within the same round.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    """Return cheapest price from src to dst with at most k stops."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    flights = []
    for _ in range(m):
        u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        flights.append([u, v, w])
    src = int(data[idx]); idx += 1
    dst = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    print(solve(n, flights, src, dst, k))
