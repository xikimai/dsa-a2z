package ch18.learn;

import java.util.*;

/**
 * Example 02: Greedy vs DP — When Greedy Fails, DP Saves the Day
 * ===============================================================
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * Demonstrates:
 *   Part 1 — Fractional Knapsack (greedy works)
 *   Part 2 — 0/1 Knapsack counterexample (greedy fails)
 *   Part 3 — Exchange argument intuition
 */
public class Example02GreedyVsDp {

    public static void main(String[] args) {
        // ── Part 1: Fractional Knapsack ──
        System.out.println("=== Part 1: Fractional Knapsack (Greedy) ===");
        int[][] items = {{10, 60}, {20, 100}, {30, 120}};
        int capacity = 50;
        System.out.println("  Items: (weight, value) = (10,60), (20,100), (30,120)");
        System.out.println("  Capacity: " + capacity);

        // Sort by ratio descending
        Arrays.sort(items, (a, b) -> Double.compare(
            (double) b[1] / b[0], (double) a[1] / a[0]));

        double total = 0;
        int remaining = capacity;
        for (int[] item : items) {
            int take = Math.min(item[0], remaining);
            double value = take * ((double) item[1] / item[0]);
            total += value;
            remaining -= take;
            System.out.printf("  Take %d/%d of (w=%d,v=%d), value=%.1f%n",
                take, item[0], item[0], item[1], value);
        }
        System.out.printf("  Total value: %.1f%n%n", total);

        // ── Part 2: 0/1 Knapsack (Greedy Fails) ──
        System.out.println("=== Part 2: 0/1 Knapsack (Greedy Fails!) ===");
        System.out.println("  Items: (6,8), (5,5), (5,5). Capacity: 10");
        System.out.println("  Ratios: 1.33, 1.00, 1.00");
        System.out.println("  Greedy (by ratio): takes (6,8) -> value 8. Can't fit more.");
        System.out.println("  Optimal: takes (5,5)+(5,5) -> value 10");
        System.out.println("  Greedy is WRONG for 0/1 knapsack!\n");

        // ── Part 3: Exchange Argument ──
        System.out.println("=== Part 3: Exchange Argument Idea ===");
        System.out.println("  Activity Selection proof sketch:");
        System.out.println("  1. Greedy picks earliest-ending activity g1");
        System.out.println("  2. Optimal picks some o1 where end(o1) >= end(g1)");
        System.out.println("  3. Swap o1 with g1 — still valid, not worse");
        System.out.println("  4. Repeat until optimal = greedy");
        System.out.println("  Therefore greedy is optimal!");
    }
}
