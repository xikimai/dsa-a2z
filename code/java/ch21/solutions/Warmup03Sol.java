package ch21.solutions;

import java.util.*;

/**
 * Solution for Warmup 3: Delete Node at Position
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(n)  SPACE: O(n)
 */
public class Warmup03Sol {
    static class ListNode {
        int val; ListNode next;
        ListNode(int v) { val = v; }
    }

    public static int[] solve(int[] arr, int pos) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : arr) { cur.next = new ListNode(v); cur = cur.next; }
        ListNode head = dummy.next;

        if (head == null) return new int[]{};
        if (pos == 0) head = head.next;
        else {
            cur = head;
            for (int i = 0; i < pos - 1 && cur.next != null; i++) cur = cur.next;
            if (cur.next != null) cur.next = cur.next.next;
        }

        List<Integer> res = new ArrayList<>();
        cur = head;
        while (cur != null) { res.add(cur.val); cur = cur.next; }
        return res.stream().mapToInt(i -> i).toArray();
    }
}
