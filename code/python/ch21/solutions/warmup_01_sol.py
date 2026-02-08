"""
Solution for Warmup 1: Traverse Linked List
=============================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
Build a linked list from the array using a dummy head node,
then traverse from the real head, collecting values into a list.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int]) -> list[int]:
    """Build a linked list from arr, traverse and return values as list."""
    # Build linked list
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next

    # Traverse and collect
    result = []
    current = dummy.next
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
