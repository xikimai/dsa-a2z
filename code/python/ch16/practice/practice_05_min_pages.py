"""
Practice 5: Minimum Pages Allocation
======================================
Chapter 16: Binary Search Beyond — When the Answer Is the Question

PROBLEM
-------
Given an array of book page counts and a number of students, allocate
books to students such that: each student gets contiguous books, every
book is assigned, and the maximum pages any student reads is minimized.
Return -1 if there are more students than books.

INPUT FORMAT
------------
First line: space-separated integers (page counts).
Second line: a single integer (number of students).

OUTPUT FORMAT
-------------
A single integer — the minimized maximum pages, or -1.

CONSTRAINTS
-----------
- 1 <= len(pages) <= 10^5
- 1 <= pages[i] <= 10^6
- 1 <= students <= 10^5

EXAMPLES
--------
Input:
  12 34 67 90
  2
Output: 113

Input:
  10 20 30
  3
Output: 30

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(pages: list[int], students: int) -> int:
    """Return minimum possible maximum pages any student reads."""
    pass  # TODO: Replace this with your solution

    def feasible(max_pages):
        count, current = 1, 0
        for p in pages:
            if current + p > max_pages:
                count += 1
                current = 0
            current += p
        return count <= students

    lo, hi = max(pages), sum(pages)
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
    pages = list(map(int, line.split()))
    students = int(input().strip())
    print(solve(pages, students))
