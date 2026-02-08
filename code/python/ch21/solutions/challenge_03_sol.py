"""
Solution for Challenge 3: Add Two Numbers
===========================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
Build two linked lists from arrays, walk both simultaneously adding
digits with carry. Build result list as we go.

TIME COMPLEXITY:  O(max(n, m))
SPACE COMPLEXITY: O(max(n, m))
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr1: list[int], arr2: list[int]) -> list[int]:
    """Add two numbers (in reverse-digit linked list form) and return result."""
    # Build linked lists
    def build(arr):
        dummy = ListNode(0)
        current = dummy
        for v in arr:
            current.next = ListNode(v)
            current = current.next
        return dummy.next

    l1 = build(arr1)
    l2 = build(arr2)

    # Add digits
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # Collect result
    result = []
    current = dummy.next
    while current:
        result.append(current.val)
        current = current.next
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr1 = list(map(int, input().strip().split()))
    arr2 = list(map(int, input().strip().split()))
    print(solve(arr1, arr2))
