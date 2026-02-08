package ch21.solutions;

import java.util.*;

/**
 * Solution for Challenge 2: Intersection of Two Lists
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(n+m)  SPACE: O(n+m)
 */
public class Challenge02Sol {
    static class ListNode {
        int val; ListNode next;
        ListNode(int v) { val = v; }
    }

    public static int solve(int[] arrA, int[] arrB, int skipA, int skipB) {
        if (skipA >= arrA.length || skipB >= arrB.length) return -1;
        // Verify suffix matches
        int lenSuffix = arrA.length - skipA;
        if (arrB.length - skipB != lenSuffix) return -1;
        for (int i = 0; i < lenSuffix; i++) {
            if (arrA[skipA + i] != arrB[skipB + i]) return -1;
        }
        if (lenSuffix == 0) return -1;

        // Build shared suffix
        ListNode[] shared = new ListNode[lenSuffix];
        for (int i = 0; i < lenSuffix; i++) shared[i] = new ListNode(arrA[skipA + i]);
        for (int i = 0; i < lenSuffix - 1; i++) shared[i].next = shared[i + 1];

        // Build list A
        ListNode headA;
        if (skipA > 0) {
            ListNode[] prefA = new ListNode[skipA];
            for (int i = 0; i < skipA; i++) prefA[i] = new ListNode(arrA[i]);
            for (int i = 0; i < skipA - 1; i++) prefA[i].next = prefA[i + 1];
            prefA[skipA - 1].next = shared[0];
            headA = prefA[0];
        } else {
            headA = shared[0];
        }

        // Build list B
        ListNode headB;
        if (skipB > 0) {
            ListNode[] prefB = new ListNode[skipB];
            for (int i = 0; i < skipB; i++) prefB[i] = new ListNode(arrB[i]);
            for (int i = 0; i < skipB - 1; i++) prefB[i].next = prefB[i + 1];
            prefB[skipB - 1].next = shared[0];
            headB = prefB[0];
        } else {
            headB = shared[0];
        }

        // Two-pointer
        ListNode a = headA, b = headB;
        while (a != b) {
            a = (a != null) ? a.next : headB;
            b = (b != null) ? b.next : headA;
        }
        return (a != null) ? a.val : -1;
    }
}
