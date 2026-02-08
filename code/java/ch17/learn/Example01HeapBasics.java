package ch17.learn;

import java.util.*;

/**
 * Example 01: Heap Basics
 * ==========================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * Demonstrates fundamental heap operations in Java:
 *   Part 1 — PriorityQueue (min-heap) basics: add, peek, poll
 *   Part 2 — Max-heap with Collections.reverseOrder()
 *   Part 3 — Visualizing a heap as a tree (array indices)
 *   Part 4 — Building a heap manually with bubble-up
 */
public class Example01HeapBasics {

    public static void main(String[] args) {

        // ── Part 1: Min-Heap (default PriorityQueue) ──────────────
        System.out.println("=== Part 1: Min-Heap (default PriorityQueue) ===");

        PriorityQueue<Integer> minPQ = new PriorityQueue<>();
        int[] values = {9, 5, 6, 2, 3, 8, 1, 7, 4};
        for (int v : values) {
            minPQ.add(v);
            System.out.println("  add(" + v + ") -> peek = " + minPQ.peek());
        }

        System.out.println("\n  Polling all (comes out in sorted order):");
        StringBuilder sb = new StringBuilder("  ");
        while (!minPQ.isEmpty()) {
            sb.append(minPQ.poll()).append(" ");
        }
        System.out.println(sb.toString().trim());

        // ── Part 2: Max-Heap ──────────────────────────────────────
        System.out.println("\n=== Part 2: Max-Heap (reverseOrder) ===");

        PriorityQueue<Integer> maxPQ = new PriorityQueue<>(Collections.reverseOrder());
        for (int v : values) {
            maxPQ.add(v);
        }

        System.out.println("  Peek (maximum): " + maxPQ.peek());
        System.out.print("  Polling all: ");
        while (!maxPQ.isEmpty()) {
            System.out.print(maxPQ.poll() + " ");
        }
        System.out.println();

        // ── Part 3: Array Representation ──────────────────────────
        System.out.println("\n=== Part 3: Heap as Array ===");
        int[] heap = {1, 3, 2, 7, 6, 5, 4, 8};
        System.out.println("  Array: " + Arrays.toString(heap));
        System.out.println("  Parent-child relationships:");
        for (int i = 0; i < heap.length; i++) {
            int parent = (i > 0) ? (i - 1) / 2 : -1;
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            String parentStr = (parent >= 0) ? "parent=" + heap[parent] : "ROOT";
            String leftStr = (left < heap.length) ? "left=" + heap[left] : "none";
            String rightStr = (right < heap.length) ? "right=" + heap[right] : "none";
            System.out.printf("    node %d (idx %d): %s, %s, %s%n",
                    heap[i], i, parentStr, leftStr, rightStr);
        }

        // ── Part 4: Manual Bubble-Up ─────────────────────────────
        System.out.println("\n=== Part 4: Manual Bubble-Up ===");
        ArrayList<Integer> manual = new ArrayList<>();
        int[] pushValues = {5, 3, 8, 1, 2};

        for (int val : pushValues) {
            manual.add(val);
            int idx = manual.size() - 1;
            StringBuilder steps = new StringBuilder();
            while (idx > 0) {
                int parentIdx = (idx - 1) / 2;
                if (manual.get(idx) < manual.get(parentIdx)) {
                    steps.append("swap ").append(manual.get(idx))
                            .append(" with ").append(manual.get(parentIdx)).append("; ");
                    int tmp = manual.get(idx);
                    manual.set(idx, manual.get(parentIdx));
                    manual.set(parentIdx, tmp);
                    idx = parentIdx;
                } else {
                    break;
                }
            }
            if (steps.length() == 0) steps.append("no swaps");
            System.out.println("  Push " + val + ": " + steps + "-> " + manual);
        }
        System.out.println("  Final min-heap: " + manual);
    }
}
