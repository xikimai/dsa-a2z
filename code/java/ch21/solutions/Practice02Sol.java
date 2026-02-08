package ch21.solutions;

import java.util.*;

/**
 * Solution for Practice 2: Detect Cycle
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(n)  SPACE: O(n)
 */
public class Practice02Sol {
    static class ListNode {
        int val; ListNode next;
        ListNode(int v) { val = v; }
    }

    public static boolean solve(int[] arr, int cyclePos) {
        if (arr.length == 0) return false;
        ListNode[] nodes = new ListNode[arr.length];
        for (int i = 0; i < arr.length; i++) nodes[i] = new ListNode(arr[i]);
        for (int i = 0; i < arr.length - 1; i++) nodes[i].next = nodes[i + 1];
        if (cyclePos >= 0) nodes[arr.length - 1].next = nodes[cyclePos];

        ListNode slow = nodes[0], fast = nodes[0];
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
}
