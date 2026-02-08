package ch21.solutions;

import java.util.*;

/**
 * Solution for Practice 5: Palindrome Linked List
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(n)  SPACE: O(n)
 */
public class Practice05Sol {
    static class ListNode {
        int val; ListNode next;
        ListNode(int v) { val = v; }
    }

    public static boolean solve(int[] arr) {
        if (arr.length <= 1) return true;
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : arr) { cur.next = new ListNode(v); cur = cur.next; }
        ListNode head = dummy.next;

        // Find middle
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next; fast = fast.next.next;
        }
        // Reverse second half
        ListNode prev = null;
        cur = slow;
        while (cur != null) {
            ListNode next = cur.next; cur.next = prev; prev = cur; cur = next;
        }
        // Compare
        ListNode left = head, right = prev;
        while (right != null) {
            if (left.val != right.val) return false;
            left = left.next; right = right.next;
        }
        return true;
    }
}
