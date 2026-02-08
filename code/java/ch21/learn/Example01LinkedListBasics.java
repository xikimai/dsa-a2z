package ch21.learn;

/**
 * Example 01: Linked List Basics
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * Demonstrates: Building, traversing, inserting, deleting, and searching
 * in a singly linked list.
 */
public class Example01LinkedListBasics {

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

    static void printList(ListNode head) {
        StringBuilder sb = new StringBuilder();
        ListNode current = head;
        while (current != null) {
            sb.append(current.val).append(" -> ");
            current = current.next;
        }
        sb.append("null");
        System.out.println(sb.toString());
    }

    static ListNode insertAtHead(ListNode head, int val) {
        ListNode newNode = new ListNode(val);
        newNode.next = head;
        return newNode;
    }

    static ListNode insertAtPosition(ListNode head, int val, int pos) {
        ListNode newNode = new ListNode(val);
        if (pos == 0) {
            newNode.next = head;
            return newNode;
        }
        ListNode current = head;
        for (int i = 0; i < pos - 1 && current != null; i++) {
            current = current.next;
        }
        if (current != null) {
            newNode.next = current.next;
            current.next = newNode;
        }
        return head;
    }

    static ListNode deleteAtPosition(ListNode head, int pos) {
        if (head == null) return null;
        if (pos == 0) return head.next;
        ListNode current = head;
        for (int i = 0; i < pos - 1 && current.next != null; i++) {
            current = current.next;
        }
        if (current.next != null) {
            current.next = current.next.next;
        }
        return head;
    }

    static boolean search(ListNode head, int target) {
        ListNode current = head;
        while (current != null) {
            if (current.val == target) return true;
            current = current.next;
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println("=== Building a linked list ===");
        ListNode head = buildList(new int[]{10, 20, 30, 40, 50});
        printList(head);

        System.out.println("\n=== Insert 5 at head ===");
        head = insertAtHead(head, 5);
        printList(head);

        System.out.println("\n=== Insert 25 at position 3 ===");
        head = insertAtPosition(head, 25, 3);
        printList(head);

        System.out.println("\n=== Delete at position 0 ===");
        head = deleteAtPosition(head, 0);
        printList(head);

        System.out.println("\n=== Search ===");
        System.out.println("Search for 30: " + search(head, 30));
        System.out.println("Search for 99: " + search(head, 99));
    }
}
