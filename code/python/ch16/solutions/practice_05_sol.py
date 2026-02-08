"""
Solution for Practice 5: Minimum Pages Allocation
===================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Binary search on answer space [max(pages), sum(pages)]. For each candidate
max-pages, greedily assign books to students and count students needed.

TIME COMPLEXITY:  O(n * log(sum(pages)))
SPACE COMPLEXITY: O(1)
"""


def solve(pages: list[int], students: int) -> int:
    """Return minimum possible maximum pages any student reads."""
    if students > len(pages):
        return -1

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
