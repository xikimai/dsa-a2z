package ch21.solutions;

import java.util.*;

/**
 * Solution for Warmup 5: Reverse a Linked List
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(n)  SPACE: O(n) build + O(1) reversal
 */
public class Warmup05Sol {
    static class ListNode {
        int val; ListNode next;
        ListNode(int v) { val = v; }
    }

    public static int[] solve(int[] arr) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : arr) { cur.next = new ListNode(v); cur = cur.next; }
        ListNode head = dummy.next;

        ListNode prev = null;
        cur = head;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }

        List<Integer> res = new ArrayList<>();
        cur = prev;
        while (cur != null) { res.add(cur.val); cur = cur.next; }
        return res.stream().mapToInt(i -> i).toArray();
    }
}
