"""
Solution for Warmup 4: Search in Linked List
==============================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
Build a linked list, traverse it checking each node's value
against the target.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for building the list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int], target: int) -> bool:
    """Return True if target exists in the linked list built from arr."""
    # Build linked list
    dummy = ListNode(0)
    current = dummy
    for v in arr:
        current.next = ListNode(v)
        current = current.next

    # Search
    current = dummy.next
    while current:
        if current.val == target:
            return True
        current = current.next
    return False


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    target = int(input().strip())
    print(solve(arr, target))
