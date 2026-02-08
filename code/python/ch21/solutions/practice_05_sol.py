"""
Solution for Practice 5: Palindrome Linked List
=================================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
1. Find the middle using slow/fast pointers
2. Reverse the second half
3. Compare first half with reversed second half

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for building, O(1) for the check
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int]) -> bool:
    """Return True if the linked list built from arr is a palindrome."""
    if len(arr) <= 1:
        return True

    # Build linked list
    dummy = ListNode(0)
    current = dummy
    for v in arr:
        current.next = ListNode(v)
        current = current.next
    head = dummy.next

    # Find middle (slow ends at second middle for even-length)
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half (starting from slow)
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Compare first half with reversed second half
    left = head
    right = prev  # head of reversed second half
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
