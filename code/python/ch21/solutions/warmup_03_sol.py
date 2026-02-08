"""
Solution for Warmup 3: Delete Node at Position
================================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
Build a linked list, walk to position pos-1, skip over the target node.
Handle pos=0 by returning head.next.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int], pos: int) -> list[int]:
    """Delete the node at pos in the linked list built from arr, return as list."""
    # Build linked list
    dummy = ListNode(0)
    current = dummy
    for v in arr:
        current.next = ListNode(v)
        current = current.next
    head = dummy.next

    if head is None:
        return []

    # Delete at position
    if pos == 0:
        head = head.next
    else:
        current = head
        for _ in range(pos - 1):
            if current.next is None:
                break
            current = current.next
        if current.next is not None:
            current.next = current.next.next

    # Convert back to list
    result = []
    current = head
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
    pos = int(input().strip())
    print(solve(arr, pos))
