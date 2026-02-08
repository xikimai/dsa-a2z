"""
Solution for Warmup 4: Check if Array is a Min-Heap
=======================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

APPROACH
--------
Check every parent node against its children. A parent at index i
must be <= its left child at 2i+1 and right child at 2i+2.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int]) -> bool:
    """Return True if arr satisfies the min-heap property."""
    n = len(arr)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
