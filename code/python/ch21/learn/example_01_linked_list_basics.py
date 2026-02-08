"""
Example 01: Linked List Basics
================================
Chapter 21: Linked Lists — Pointers and Connections

Demonstrates:
- Creating a ListNode class
- Building a linked list from an array
- Traversing and printing a linked list
- Inserting at head, tail, and a given position
- Deleting a node at a given position
- Searching for a value
"""


class ListNode:
    """A node in a singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


# ── Build a linked list from a Python list ──────────────────────────

def build_list(arr):
    """Build a singly linked list from a Python list."""
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def to_list(head):
    """Convert a linked list back to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def print_list(head):
    """Print a linked list in a readable format."""
    parts = []
    current = head
    while current:
        parts.append(str(current.val))
        current = current.next
    parts.append("null")
    print(" -> ".join(parts))


# ── Insert operations ───────────────────────────────────────────────

def insert_at_head(head, val):
    """Insert a new node at the head. Returns new head."""
    new_node = ListNode(val)
    new_node.next = head
    return new_node


def insert_at_tail(head, val):
    """Insert a new node at the tail. Returns head."""
    new_node = ListNode(val)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


def insert_at_position(head, val, pos):
    """Insert val at 0-indexed position. Returns head."""
    new_node = ListNode(val)
    if pos == 0:
        new_node.next = head
        return new_node
    current = head
    for _ in range(pos - 1):
        if current is None:
            return head
        current = current.next
    if current is None:
        return head
    new_node.next = current.next
    current.next = new_node
    return head


# ── Delete operation ────────────────────────────────────────────────

def delete_at_position(head, pos):
    """Delete node at 0-indexed position. Returns head."""
    if head is None:
        return None
    if pos == 0:
        return head.next
    current = head
    for _ in range(pos - 1):
        if current.next is None:
            return head
        current = current.next
    if current.next is not None:
        current.next = current.next.next
    return head


# ── Search ──────────────────────────────────────────────────────────

def search(head, target):
    """Return True if target exists in the list."""
    current = head
    while current:
        if current.val == target:
            return True
        current = current.next
    return False


# ── Demo ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Building a linked list ===")
    head = build_list([10, 20, 30, 40, 50])
    print_list(head)
    print(f"As Python list: {to_list(head)}")

    print("\n=== Insert at head (5) ===")
    head = insert_at_head(head, 5)
    print_list(head)

    print("\n=== Insert at tail (60) ===")
    head = insert_at_tail(head, 60)
    print_list(head)

    print("\n=== Insert 25 at position 3 ===")
    head = insert_at_position(head, 25, 3)
    print_list(head)

    print("\n=== Delete at position 0 (head) ===")
    head = delete_at_position(head, 0)
    print_list(head)

    print("\n=== Delete at position 3 ===")
    head = delete_at_position(head, 3)
    print_list(head)

    print("\n=== Search ===")
    print(f"Search for 30: {search(head, 30)}")
    print(f"Search for 99: {search(head, 99)}")
