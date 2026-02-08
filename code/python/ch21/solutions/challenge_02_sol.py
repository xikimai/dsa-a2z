"""
Solution for Challenge 2: Intersection of Two Lists
=====================================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
Build two lists sharing actual node objects for the common suffix.
Use two-pointer technique: each pointer switches to the other list's
head when it reaches null. They meet at the intersection.

TIME COMPLEXITY:  O(n + m)
SPACE COMPLEXITY: O(n + m) for building, O(1) for detection
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr_a: list[int], arr_b: list[int], skip_a: int, skip_b: int) -> int:
    """Return the value at the intersection point, or -1."""
    if skip_a >= len(arr_a) or skip_b >= len(arr_b):
        return -1

    # Verify the suffix matches
    suffix_a = arr_a[skip_a:]
    suffix_b = arr_b[skip_b:]
    if suffix_a != suffix_b:
        return -1
    if not suffix_a:
        return -1

    # Build shared suffix nodes
    shared_nodes = []
    for val in suffix_a:
        shared_nodes.append(ListNode(val))
    for i in range(len(shared_nodes) - 1):
        shared_nodes[i].next = shared_nodes[i + 1]

    # Build list A prefix
    head_a = None
    if skip_a > 0:
        nodes_a = []
        for val in arr_a[:skip_a]:
            nodes_a.append(ListNode(val))
        for i in range(len(nodes_a) - 1):
            nodes_a[i].next = nodes_a[i + 1]
        nodes_a[-1].next = shared_nodes[0]
        head_a = nodes_a[0]
    else:
        head_a = shared_nodes[0]

    # Build list B prefix
    head_b = None
    if skip_b > 0:
        nodes_b = []
        for val in arr_b[:skip_b]:
            nodes_b.append(ListNode(val))
        for i in range(len(nodes_b) - 1):
            nodes_b[i].next = nodes_b[i + 1]
        nodes_b[-1].next = shared_nodes[0]
        head_b = nodes_b[0]
    else:
        head_b = shared_nodes[0]

    # Two-pointer technique
    a = head_a
    b = head_b
    while a != b:
        a = a.next if a else head_b
        b = b.next if b else head_a

    if a is None:
        return -1
    return a.val


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr_a = list(map(int, input().strip().split()))
    arr_b = list(map(int, input().strip().split()))
    parts = input().strip().split()
    skip_a, skip_b = int(parts[0]), int(parts[1])
    print(solve(arr_a, arr_b, skip_a, skip_b))
