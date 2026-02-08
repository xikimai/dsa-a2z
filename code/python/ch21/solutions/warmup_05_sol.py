"""
Solution for Warmup 5: Reverse a Linked List
==============================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
Build a linked list, reverse it using the 3-pointer iterative
approach (prev, current, next_node), then collect values.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for building + O(1) for reversal
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int]) -> list[int]:
    """Reverse the linked list built from arr, return as list."""
    # Build linked list
    dummy = ListNode(0)
    current = dummy
    for v in arr:
        current.next = ListNode(v)
        current = current.next
    head = dummy.next

    # Reverse using 3 pointers
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Collect values
    result = []
    current = prev  # prev is the new head
    while current:
        result.append(current.val)
        current = current.next
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
