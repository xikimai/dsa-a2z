package ch21.solutions;

import java.util.*;

/**
 * Solution for Practice 4: Remove Nth Node From End
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(n)  SPACE: O(n)
 */
public class Practice04Sol {
    static class ListNode {
        int val; ListNode next;
        ListNode(int v) { val = v; }
    }

    public static int[] solve(int[] arr, int n) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : arr) { cur.next = new ListNode(v); cur = cur.next; }

        ListNode front = dummy, back = dummy;
        for (int i = 0; i <= n; i++) front = front.next;
        while (front != null) { front = front.next; back = back.next; }
        back.next = back.next.next;

        List<Integer> res = new ArrayList<>();
        cur = dummy.next;
        while (cur != null) { res.add(cur.val); cur = cur.next; }
        return res.stream().mapToInt(i -> i).toArray();
    }
}
