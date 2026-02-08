"""
Solution for Practice 1: Find Middle Node
===========================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
Build a linked list, use slow/fast pointer technique.
When fast reaches the end, slow is at the middle.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for building the list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int]) -> int:
    """Return the value of the middle node."""
    # Build linked list
    dummy = ListNode(0)
    current = dummy
    for v in arr:
        current.next = ListNode(v)
        current = current.next
    head = dummy.next

    # Slow/fast pointer
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    print(solve(arr))
