"""
Solution for Challenge 2: Painter's Partition
==============================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Binary search on answer space [max(boards), sum(boards)]. For each candidate
max section length, greedily assign boards to painters and count painters needed.

TIME COMPLEXITY:  O(n * log(sum(boards)))
SPACE COMPLEXITY: O(1)
"""


def solve(boards: list[int], k: int) -> int:
    """Return minimum possible maximum section any painter paints."""
    if k > len(boards):
        return max(boards)

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
