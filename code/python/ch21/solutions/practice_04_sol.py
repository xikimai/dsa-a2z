"""
Solution for Practice 4: Remove Nth Node From End
===================================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
Use a dummy node and two pointers with a gap of n+1 between them.
When the front pointer reaches null, the back pointer is right
before the node to remove.

TIME COMPLEXITY:  O(n) — single pass
SPACE COMPLEXITY: O(n) for building the list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int], n: int) -> list[int]:
    """Remove the nth node from the end and return the result as a list."""
    # Build linked list
    dummy = ListNode(0)
    current = dummy
    for v in arr:
        current.next = ListNode(v)
        current = current.next
    head = dummy.next

    # Use dummy node for edge case (removing head)
    sentinel = ListNode(0)
    sentinel.next = head

    # Two pointers with gap of n
    front = sentinel
    back = sentinel
    for _ in range(n + 1):
        front = front.next

    while front:
        front = front.next
        back = back.next

    # Remove the node
    back.next = back.next.next

    # Collect result
    result = []
    current = sentinel.next
    while current:
        result.append(current.val)
        current = current.next
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    n = int(input().strip())
    print(solve(arr, n))
