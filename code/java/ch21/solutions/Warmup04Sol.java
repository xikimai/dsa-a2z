package ch21.solutions;

import java.util.*;

/**
 * Solution for Warmup 4: Search in Linked List
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(n)  SPACE: O(n)
 */
public class Warmup04Sol {
    static class ListNode {
        int val; ListNode next;
        ListNode(int v) { val = v; }
    }

    public static boolean solve(int[] arr, int target) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : arr) { cur.next = new ListNode(v); cur = cur.next; }
        cur = dummy.next;
        while (cur != null) {
            if (cur.val == target) return true;
            cur = cur.next;
        }
        return false;
    }
}
