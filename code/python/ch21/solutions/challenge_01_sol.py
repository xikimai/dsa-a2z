"""
Solution for Challenge 1: Find Cycle Start
============================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
1. Build linked list with cycle at cycle_pos
2. Floyd's algorithm Phase 1: detect cycle (slow/fast meet)
3. Phase 2: move one pointer to head, advance both one step
   at a time — they meet at cycle start
4. Walk from head to the meeting point to find the index

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for building, O(1) for detection
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int], cycle_pos: int) -> int:
    """Return the index where the cycle starts, or -1 if no cycle."""
    if not arr:
        return -1

    # Build linked list with cycle
    nodes = []
    for val in arr:
        nodes.append(ListNode(val))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos >= 0:
        nodes[-1].next = nodes[cycle_pos]

    head = nodes[0]

    # Phase 1: Detect cycle
    slow = head
    fast = head
    has_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return -1

    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Find index of the cycle start node
    current = head
    index = 0
    while current != slow:
        current = current.next
        index += 1
    return index


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    cycle_pos = int(input().strip())
    print(solve(arr, cycle_pos))
