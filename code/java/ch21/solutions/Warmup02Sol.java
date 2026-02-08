package ch21.solutions;

import java.util.*;

/**
 * Solution for Warmup 2: Insert at Position
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(n)  SPACE: O(n)
 */
public class Warmup02Sol {
    static class ListNode {
        int val; ListNode next;
        ListNode(int v) { val = v; }
    }

    public static int[] solve(int[] arr, int val, int pos) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : arr) { cur.next = new ListNode(v); cur = cur.next; }
        ListNode head = dummy.next;

        ListNode newNode = new ListNode(val);
        if (pos == 0) {
            newNode.next = head;
            head = newNode;
        } else {
            cur = head;
            for (int i = 0; i < pos - 1 && cur != null; i++) cur = cur.next;
            if (cur != null) { newNode.next = cur.next; cur.next = newNode; }
        }

        List<Integer> res = new ArrayList<>();
        cur = head;
        while (cur != null) { res.add(cur.val); cur = cur.next; }
        return res.stream().mapToInt(i -> i).toArray();
    }
}
