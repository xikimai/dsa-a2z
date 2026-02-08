package ch21.solutions;

import java.util.*;

/**
 * Solution for Challenge 3: Add Two Numbers
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(max(n,m))  SPACE: O(max(n,m))
 */
public class Challenge03Sol {
    static class ListNode {
        int val; ListNode next;
        ListNode(int v) { val = v; }
    }

    static ListNode build(int[] arr) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : arr) { cur.next = new ListNode(v); cur = cur.next; }
        return dummy.next;
    }

    public static int[] solve(int[] arr1, int[] arr2) {
        ListNode l1 = build(arr1), l2 = build(arr2);
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int v1 = (l1 != null) ? l1.val : 0;
            int v2 = (l2 != null) ? l2.val : 0;
            int total = v1 + v2 + carry;
            carry = total / 10;
            cur.next = new ListNode(total % 10);
            cur = cur.next;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
        List<Integer> res = new ArrayList<>();
        cur = dummy.next;
        while (cur != null) { res.add(cur.val); cur = cur.next; }
        return res.stream().mapToInt(i -> i).toArray();
    }
}
