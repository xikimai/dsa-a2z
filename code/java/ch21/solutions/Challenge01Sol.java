package ch21.solutions;

import java.util.*;

/**
 * Solution for Challenge 1: Find Cycle Start
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(n)  SPACE: O(n)
 */
public class Challenge01Sol {
    static class ListNode {
        int val; ListNode next;
        ListNode(int v) { val = v; }
    }

    public static int solve(int[] arr, int cyclePos) {
        if (arr.length == 0) return -1;
        ListNode[] nodes = new ListNode[arr.length];
        for (int i = 0; i < arr.length; i++) nodes[i] = new ListNode(arr[i]);
        for (int i = 0; i < arr.length - 1; i++) nodes[i].next = nodes[i + 1];
        if (cyclePos >= 0) nodes[arr.length - 1].next = nodes[cyclePos];

        ListNode slow = nodes[0], fast = nodes[0];
        boolean hasCycle = false;
        while (fast != null && fast.next != null) {
            slow = slow.next; fast = fast.next.next;
            if (slow == fast) { hasCycle = true; break; }
        }
        if (!hasCycle) return -1;

        slow = nodes[0];
        while (slow != fast) { slow = slow.next; fast = fast.next; }

        ListNode cur = nodes[0];
        int index = 0;
        while (cur != slow) { cur = cur.next; index++; }
        return index;
    }
}
