package ch18.learn;

import java.util.*;

/**
 * Example 01: Greedy Basics — Activity Selection Step by Step
 * ============================================================
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * Demonstrates:
 *   Part 1 — Activity Selection: sort by end time, pick greedily
 *   Part 2 — Brute Force vs Greedy comparison
 *   Part 3 — When greedy fails: coin change counterexample
 */
public class Example01GreedyBasics {

    public static void main(String[] args) {
        // ── Part 1: Activity Selection ──
        System.out.println("=== Part 1: Activity Selection ===");
        int[][] activities = {{9,10},{9,12},{10,11},{11,14},{11,12},{13,15}};
        String[] names = {"A","B","C","D","E","F"};

        System.out.println("  Original activities:");
        for (int i = 0; i < activities.length; i++)
            System.out.println("    " + names[i] + ": [" + activities[i][0] + ", " + activities[i][1] + ")");

        // Sort by end time
        Integer[] idx = new Integer[activities.length];
        for (int i = 0; i < idx.length; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> activities[a][1] - activities[b][1]);

        System.out.println("\n  Sorted by end time:");
        for (int i : idx)
            System.out.println("    " + names[i] + ": [" + activities[i][0] + ", " + activities[i][1] + ")");

        System.out.println("\n  Greedy selection:");
        int lastEnd = 0;
        int count = 0;
        for (int i : idx) {
            if (activities[i][0] >= lastEnd) {
                System.out.println("    PICK " + names[i] + " [" + activities[i][0] + ", " + activities[i][1] + ")");
                lastEnd = activities[i][1];
                count++;
            } else {
                System.out.println("    SKIP " + names[i] + " [" + activities[i][0] + ", " + activities[i][1] + ")");
            }
        }
        System.out.println("  Selected: " + count + " activities\n");

        // ── Part 2: Coin Change — Greedy Fails ──
        System.out.println("=== Part 2: When Greedy Fails — Coin Change ===");
        int[] coins = {4, 3, 1};
        int target = 6;
        int rem = target;
        List<Integer> used = new ArrayList<>();
        for (int c : coins) {
            while (rem >= c) { used.add(c); rem -= c; }
        }
        System.out.println("  Coins: [4, 3, 1], target: " + target);
        System.out.println("  Greedy: " + used + " = " + used.size() + " coins");
        System.out.println("  Optimal: [3, 3] = 2 coins");
        System.out.println("  Greedy is WRONG!");
    }
}
