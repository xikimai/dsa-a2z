package ch21.solutions;

import java.util.*;

/**
 * Solution for Warmup 1: Traverse Linked List
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(n)  SPACE: O(n)
 */
public class Warmup01Sol {
    static class ListNode {
        int val; ListNode next;
        ListNode(int v) { val = v; }
    }

    public static int[] solve(int[] arr) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : arr) { cur.next = new ListNode(v); cur = cur.next; }
        List<Integer> res = new ArrayList<>();
        cur = dummy.next;
        while (cur != null) { res.add(cur.val); cur = cur.next; }
        return res.stream().mapToInt(i -> i).toArray();
    }
}
