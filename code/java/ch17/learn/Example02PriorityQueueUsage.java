package ch17.learn;

import java.util.*;

/**
 * Example 02: Priority Queue Usage Patterns
 * ============================================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * Demonstrates practical usage patterns:
 *   Part 1 — Min-heap vs max-heap
 *   Part 2 — Custom comparators (ER triage simulation)
 *   Part 3 — Top-K elements using a heap
 *   Part 4 — Merging sorted streams
 */
public class Example02PriorityQueueUsage {

    public static void main(String[] args) {

        // ── Part 1: Min vs Max Heap ──────────────────────────────
        System.out.println("=== Part 1: Min-Heap vs Max-Heap ===");

        PriorityQueue<Integer> min = new PriorityQueue<>();
        PriorityQueue<Integer> max = new PriorityQueue<>(Collections.reverseOrder());

        int[] data = {5, 3, 8, 1, 2, 9, 4};
        for (int x : data) {
            min.add(x);
            max.add(x);
        }

        System.out.print("  Min-heap order: ");
        while (!min.isEmpty()) System.out.print(min.poll() + " ");
        System.out.println();

        System.out.print("  Max-heap order: ");
        while (!max.isEmpty()) System.out.print(max.poll() + " ");
        System.out.println();

        // ── Part 2: Custom Comparator (ER Triage) ────────────────
        System.out.println("\n=== Part 2: ER Triage with Custom Comparator ===");

        // Lower priority number = more urgent
        PriorityQueue<String[]> er = new PriorityQueue<>(
                (a, b) -> Integer.compare(Integer.parseInt(a[0]), Integer.parseInt(b[0]))
        );

        er.add(new String[]{"3", "scraped knee"});
        er.add(new String[]{"1", "chest pain"});
        er.add(new String[]{"5", "headache"});
        er.add(new String[]{"2", "broken arm"});
        er.add(new String[]{"1", "allergic reaction"});

        System.out.println("  Doctor sees patients:");
        while (!er.isEmpty()) {
            String[] patient = er.poll();
            System.out.println("    Priority " + patient[0] + ": " + patient[1]);
        }

        // ── Part 3: Top-K Elements ──────────────────────────────
        System.out.println("\n=== Part 3: Top-K Elements ===");

        int[] scores = {85, 92, 78, 95, 88, 76, 99, 82, 91, 73};
        int k = 3;

        // Min-heap of size k for top-k largest
        PriorityQueue<Integer> topK = new PriorityQueue<>();
        for (int s : scores) {
            topK.add(s);
            if (topK.size() > k) topK.poll();
        }

        System.out.print("  Top " + k + " scores: ");
        List<Integer> result = new ArrayList<>(topK);
        Collections.sort(result, Collections.reverseOrder());
        System.out.println(result);

        // ── Part 4: Merging Sorted Streams ──────────────────────
        System.out.println("\n=== Part 4: Merging 3 Sorted Arrays ===");

        int[][] arrays = {{1, 4, 7}, {2, 5, 8}, {3, 6, 9}};

        // (value, array_index, element_index)
        PriorityQueue<int[]> pq = new PriorityQueue<>(
                (a, b) -> Integer.compare(a[0], b[0])
        );

        for (int i = 0; i < arrays.length; i++) {
            if (arrays[i].length > 0) {
                pq.add(new int[]{arrays[i][0], i, 0});
            }
        }

        System.out.print("  Merged: ");
        while (!pq.isEmpty()) {
            int[] top = pq.poll();
            System.out.print(top[0] + " ");
            int arrIdx = top[1], elemIdx = top[2];
            if (elemIdx + 1 < arrays[arrIdx].length) {
                pq.add(new int[]{arrays[arrIdx][elemIdx + 1], arrIdx, elemIdx + 1});
            }
        }
        System.out.println();
    }
}
