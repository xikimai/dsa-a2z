package ch21.learn;

/**
 * Example 02: Slow/Fast Pointer Techniques
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * Demonstrates: Floyd's cycle detection, finding the middle node,
 * and finding the start of a cycle.
 */
public class Example02SlowFastPointers {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    static ListNode buildList(int[] arr) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        for (int v : arr) {
            current.next = new ListNode(v);
            current = current.next;
        }
        return dummy.next;
    }

    static ListNode buildListWithCycle(int[] arr, int cyclePos) {
        if (arr.length == 0) return null;
        ListNode[] nodes = new ListNode[arr.length];
        for (int i = 0; i < arr.length; i++) {
            nodes[i] = new ListNode(arr[i]);
        }
        for (int i = 0; i < arr.length - 1; i++) {
            nodes[i].next = nodes[i + 1];
        }
        if (cyclePos >= 0) {
            nodes[arr.length - 1].next = nodes[cyclePos];
        }
        return nodes[0];
    }

    static boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }

    static int findMiddle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow.val;
    }

    public static void main(String[] args) {
        System.out.println("=== Finding the Middle Node ===");
        ListNode head = buildList(new int[]{1, 2, 3, 4, 5});
        System.out.println("List: [1,2,3,4,5] -> Middle: " + findMiddle(head));

        head = buildList(new int[]{1, 2, 3, 4});
        System.out.println("List: [1,2,3,4] -> Middle (second): " + findMiddle(head));

        System.out.println("\n=== Cycle Detection ===");
        ListNode noCycle = buildListWithCycle(new int[]{1, 2, 3, 4, 5}, -1);
        System.out.println("[1,2,3,4,5] no cycle: " + hasCycle(noCycle));

        ListNode withCycle = buildListWithCycle(new int[]{1, 2, 3, 4, 5}, 2);
        System.out.println("[1,2,3,4,5] tail->node 2: " + hasCycle(withCycle));
    }
}
