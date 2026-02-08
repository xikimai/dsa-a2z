"""
Solution for Practice 2: Detect Cycle
=======================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
Build a linked list with the specified cycle, then use Floyd's
cycle detection (slow/fast pointers).

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for building the list, O(1) for detection
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int], cycle_pos: int) -> bool:
    """Return True if the linked list (with cycle at cycle_pos) has a cycle."""
    if not arr:
        return False

    # Build linked list with cycle
    nodes = []
    for val in arr:
        nodes.append(ListNode(val))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos >= 0:
        nodes[-1].next = nodes[cycle_pos]

    head = nodes[0]

    # Floyd's cycle detection
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    cycle_pos = int(input().strip())
    print(solve(arr, cycle_pos))
