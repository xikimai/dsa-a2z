"""
Solution for Challenge 2: Task Scheduler
============================================
Chapter 17: Heaps & Priority Queues — The VIP Line

APPROACH
--------
Use a max-heap of task frequencies. Each round, pick up to (n+1) tasks.
After picking, decrement counts and re-push non-zero counts.
If there are remaining tasks, the round took (n+1) intervals (including idles).
The last round only takes as many intervals as tasks picked.

TIME COMPLEXITY:  O(total_tasks * log 26) = O(total_tasks)
SPACE COMPLEXITY: O(26) = O(1) auxiliary
"""

import heapq
from collections import Counter


def solve(tasks: list[str], n: int) -> int:
    """Return minimum intervals to complete all tasks with cooldown n."""
    freq = Counter(tasks)
    # Max-heap of frequencies (negated)
    heap = [-cnt for cnt in freq.values()]
    heapq.heapify(heap)

    time_taken = 0

    while heap:
        cycle = n + 1  # Maximum tasks per round
        temp = []      # Tasks to re-add after this round
        tasks_done = 0

        for _ in range(cycle):
            if heap:
                cnt = -heapq.heappop(heap)
                if cnt > 1:
                    temp.append(-(cnt - 1))
                tasks_done += 1

        # Re-add remaining tasks
        for item in temp:
            heapq.heappush(heap, item)

        # If there are more tasks, this round took a full cycle (n+1)
        # Otherwise, only count the tasks actually done
        if heap:
            time_taken += cycle
        else:
            time_taken += tasks_done

    return time_taken


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    tasks = input().strip().split()
    n = int(input().strip())
    print(solve(tasks, n))
