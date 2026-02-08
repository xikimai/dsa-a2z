"""
Example 02: Slow/Fast Pointer Techniques
==========================================
Chapter 21: Linked Lists — Pointers and Connections

Demonstrates:
- Floyd's cycle detection (tortoise and hare)
- Finding the middle node
- Finding the start of a cycle
"""


class ListNode:
    """A node in a singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(arr):
    """Build a singly linked list from a Python list."""
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def build_list_with_cycle(arr, cycle_pos):
    """Build a linked list where the tail connects to node at cycle_pos.
    cycle_pos = -1 means no cycle.
    """
    if not arr:
        return None
    nodes = []
    for val in arr:
        nodes.append(ListNode(val))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos >= 0:
        nodes[-1].next = nodes[cycle_pos]
    return nodes[0]


# ── Floyd's Cycle Detection ─────────────────────────────────────────

def has_cycle(head):
    """Detect if the linked list has a cycle using slow/fast pointers."""
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# ── Find Middle Node ────────────────────────────────────────────────

def find_middle(head):
    """Find the middle node's value. For even-length, returns second middle."""
    if head is None:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val


# ── Find Cycle Start ────────────────────────────────────────────────

def find_cycle_start(head):
    """Find the value of the node where the cycle starts. Returns -1 if no cycle."""
    slow = head
    fast = head

    # Phase 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return -1  # No cycle

    # Phase 2: Find the start
    # Move one pointer to head, advance both one step at a time
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.val


# ── Demo ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Finding the Middle Node ===")
    head = build_list([1, 2, 3, 4, 5])
    print(f"List: [1, 2, 3, 4, 5]")
    print(f"Middle: {find_middle(head)}")  # 3

    head = build_list([1, 2, 3, 4])
    print(f"\nList: [1, 2, 3, 4]")
    print(f"Middle (second middle): {find_middle(head)}")  # 3

    print("\n=== Cycle Detection ===")
    head_no_cycle = build_list_with_cycle([1, 2, 3, 4, 5], -1)
    print(f"List [1,2,3,4,5] (no cycle): has_cycle = {has_cycle(head_no_cycle)}")

    head_with_cycle = build_list_with_cycle([1, 2, 3, 4, 5], 2)
    print(f"List [1,2,3,4,5] (tail->node 2): has_cycle = {has_cycle(head_with_cycle)}")

    print("\n=== Finding Cycle Start ===")
    head = build_list_with_cycle([3, 2, 0, -4], 1)
    print(f"List [3,2,0,-4] (tail->node 1): cycle starts at value {find_cycle_start(head)}")

    head = build_list_with_cycle([1, 2], -1)
    print(f"List [1,2] (no cycle): cycle starts at {find_cycle_start(head)}")
