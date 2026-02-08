package ch14.learn;

/**
 * Example 01: Prefix Sum Basics
 * ==============================
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * Demonstrates:
 *   Part 1 — Building a 1D prefix sum array
 *   Part 2 — Answering range sum queries in O(1)
 *   Part 3 — Difference array for range updates
 */
public class Example01PrefixSumBasics {

    public static void main(String[] args) {
        // ── Part 1: Building a Prefix Sum Array ──
        System.out.println("=== Part 1: Building a Prefix Sum Array ===");
        int[] arr = {3, 1, 4, 1, 5, 9, 2, 6};
        int n = arr.length;
        long[] prefix = new long[n + 1];

        System.out.print("  arr = [");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + (i < n - 1 ? ", " : ""));
        }
        System.out.println("]");

        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] + arr[i - 1];
            System.out.println("  prefix[" + i + "] = prefix[" + (i-1) + "] + arr[" + (i-1) + "] = "
                + prefix[i-1] + " + " + arr[i-1] + " = " + prefix[i]);
        }

        System.out.print("  prefix = [");
        for (int i = 0; i <= n; i++) {
            System.out.print(prefix[i] + (i < n ? ", " : ""));
        }
        System.out.println("]\n");

        // ── Part 2: Range Sum Queries ──
        System.out.println("=== Part 2: Range Sum Queries in O(1) ===");
        int[][] queries = {{0, 7}, {2, 5}, {0, 0}, {4, 7}, {3, 3}};
        for (int[] q : queries) {
            int l = q[0], r = q[1];
            long result = prefix[r + 1] - prefix[l];
            System.out.println("  sum(" + l + ", " + r + ") = prefix[" + (r+1)
                + "] - prefix[" + l + "] = " + prefix[r+1] + " - " + prefix[l] + " = " + result);
        }
        System.out.println();

        // ── Part 3: Difference Array ──
        System.out.println("=== Part 3: Difference Array for Range Updates ===");
        int size = 6;
        long[] diff = new long[size + 1];

        int[][] updates = {{1, 3, 5}, {2, 4, 3}};
        for (int[] u : updates) {
            int l = u[0], r = u[1], val = u[2];
            diff[l] += val;
            if (r + 1 < size) diff[r + 1] -= val;
            System.out.println("  Add " + val + " to [" + l + ", " + r + "]");
        }

        long[] result = new long[size];
        long running = 0;
        for (int i = 0; i < size; i++) {
            running += diff[i];
            result[i] = running;
        }

        System.out.print("  Final array: [");
        for (int i = 0; i < size; i++) {
            System.out.print(result[i] + (i < size - 1 ? ", " : ""));
        }
        System.out.println("]");
    }
}
