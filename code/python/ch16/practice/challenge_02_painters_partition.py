"""
Challenge 2: Painter's Partition
==================================
Chapter 16: Binary Search Beyond — When the Answer Is the Question

PROBLEM
-------
Given an array of board lengths and k painters, each painter paints
contiguous boards. Minimize the maximum length any single painter paints.
If there are more painters than boards, each painter paints at most one board.

INPUT FORMAT
------------
First line: space-separated integers (board lengths).
Second line: a single integer k (number of painters).

OUTPUT FORMAT
-------------
A single integer — the minimized maximum section length.

CONSTRAINTS
-----------
- 1 <= len(boards) <= 10^5
- 1 <= boards[i] <= 10^6
- 1 <= k <= 10^5

EXAMPLES
--------
Input:
  10 20 30 40
  2
Output: 60

Input:
  10 20 30
  3
Output: 30

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(boards: list[int], k: int) -> int:
    """Return minimum possible maximum section any painter paints."""
    pass  # TODO: Replace this with your solution

    def feasible(max_len):
        painters, current = 1, 0
        for b in boards:
            if current + b > max_len:
                painters += 1
                current = 0
            current += b
        return painters <= k

    lo, hi = max(boards), sum(boards)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    boards = list(map(int, line.split()))
    k = int(input().strip())
    print(solve(boards, k))
