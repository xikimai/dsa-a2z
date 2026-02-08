package ch21.solutions;

import java.util.*;

/**
 * Solution for Practice 3: Merge Two Sorted Lists
 * Chapter 21: Linked Lists — Pointers and Connections
 * TIME: O(n+m)  SPACE: O(n+m)
 */
public class Practice03Sol {
    static class ListNode {
        int val; ListNode next;
        ListNode(int v) { val = v; }
    }

    static ListNode build(int[] arr) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : arr) { cur.next = new ListNode(v); cur = cur.next; }
        return dummy.next;
    }

    public static int[] solve(int[] arr1, int[] arr2) {
        ListNode h1 = build(arr1), h2 = build(arr2);
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        while (h1 != null && h2 != null) {
            if (h1.val <= h2.val) { cur.next = h1; h1 = h1.next; }
            else { cur.next = h2; h2 = h2.next; }
            cur = cur.next;
        }
        cur.next = (h1 != null) ? h1 : h2;

        List<Integer> res = new ArrayList<>();
        cur = dummy.next;
        while (cur != null) { res.add(cur.val); cur = cur.next; }
        return res.stream().mapToInt(i -> i).toArray();
    }
}
