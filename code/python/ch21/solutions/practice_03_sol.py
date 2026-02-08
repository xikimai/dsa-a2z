"""
Solution for Practice 3: Merge Two Sorted Lists
=================================================
Chapter 21: Linked Lists — Pointers and Connections

APPROACH
--------
Build two linked lists, merge them using a dummy node and comparing
heads. Append the remaining nodes when one list is exhausted.

TIME COMPLEXITY:  O(n + m)
SPACE COMPLEXITY: O(n + m) for building lists
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr1: list[int], arr2: list[int]) -> list[int]:
    """Merge two sorted linked lists and return the result as a list."""
    # Build linked lists
    def build(arr):
        dummy = ListNode(0)
        current = dummy
        for v in arr:
            current.next = ListNode(v)
            current = current.next
        return dummy.next

    head1 = build(arr1)
    head2 = build(arr2)

    # Merge
    dummy = ListNode(0)
    current = dummy
    while head1 and head2:
        if head1.val <= head2.val:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    current.next = head1 if head1 else head2

    # Collect result
    result = []
    current = dummy.next
    while current:
        result.append(current.val)
        current = current.next
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line1 = input().strip()
    arr1 = list(map(int, line1.split())) if line1 else []
    line2 = input().strip()
    arr2 = list(map(int, line2.split())) if line2 else []
    print(solve(arr1, arr2))
