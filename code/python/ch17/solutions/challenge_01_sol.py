"""
Solution for Challenge 1: Reorganize String
===============================================
Chapter 17: Heaps & Priority Queues — The VIP Line

APPROACH
--------
Use a max-heap of (count, char). Greedily place the most frequent char.
After placing a char, put it aside (prev). Place the next most frequent.
Then push prev back if it still has count > 0.

TIME COMPLEXITY:  O(n log 26) = O(n)
SPACE COMPLEXITY: O(26) = O(1) auxiliary
"""

import heapq
from collections import Counter


def solve(s: str) -> str:
    """Rearrange s so no two adjacent chars are the same, or return ''."""
    freq = Counter(s)

    # Check feasibility: no char can appear more than (len+1)//2 times
    max_count = max(freq.values())
    if max_count > (len(s) + 1) // 2:
        return ""

    # Max-heap: (-count, char)
    heap = [(-cnt, ch) for ch, cnt in freq.items()]
    heapq.heapify(heap)

    result = []
    prev_cnt, prev_ch = 0, ""

    while heap:
        neg_cnt, ch = heapq.heappop(heap)
        result.append(ch)

        # Push previous character back if it still has remaining count
        if prev_cnt < 0:
            heapq.heappush(heap, (prev_cnt, prev_ch))

        # Update prev to current (with decremented count)
        prev_cnt = neg_cnt + 1  # +1 because negated: -3 + 1 = -2
        prev_ch = ch

    return "".join(result)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
