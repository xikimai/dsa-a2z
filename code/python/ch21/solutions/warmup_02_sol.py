"""
Solution for Warmup 2: Insert at Position
===========================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
Build a linked list, walk to position pos-1, rewire pointers
to insert the new node. Handle pos=0 as a special case.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int], val: int, pos: int) -> list[int]:
    """Insert val at pos in the linked list built from arr, return as list."""
    # Build linked list
    dummy = ListNode(0)
    current = dummy
    for v in arr:
        current.next = ListNode(v)
        current = current.next
    head = dummy.next

    # Insert at position
    new_node = ListNode(val)
    if pos == 0:
        new_node.next = head
        head = new_node
    else:
        current = head
        for _ in range(pos - 1):
            if current is None:
                break
            current = current.next
        if current is not None:
            new_node.next = current.next
            current.next = new_node

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
    parts = input().strip().split()
    val, pos = int(parts[0]), int(parts[1])
    print(solve(arr, val, pos))
