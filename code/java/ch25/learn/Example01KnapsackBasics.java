package ch25.learn;

import java.util.*;

/**
 * Example 01: Knapsack Basics — Step-by-Step 0/1 Knapsack
 * =========================================================
 * Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 *
 * Demonstrates 0/1 Knapsack: recursive, memoized, tabulated, space-optimized.
 */
public class Example01KnapsackBasics {

    // Recursive O(2^n)
    static int knapsackRecursive(int[] w, int[] v, int cap, int i) {
        if (i < 0 || cap <= 0) return 0;
        int skip = knapsackRecursive(w, v, cap, i - 1);
        int take = 0;
        if (w[i] <= cap)
            take = v[i] + knapsackRecursive(w, v, cap - w[i], i - 1);
        return Math.max(skip, take);
    }

    // Space-optimized O(n * cap)
    static int knapsackOptimized(int[] w, int[] v, int cap) {
        int[] dp = new int[cap + 1];
        for (int i = 0; i < w.length; i++)
            for (int c = cap; c >= w[i]; c--)
                dp[c] = Math.max(dp[c], dp[c - w[i]] + v[i]);
        return dp[cap];
    }

    public static void main(String[] args) {
        int[] w = {1, 3, 4, 5};
        int[] v = {1, 4, 5, 7};
        int cap = 7;
        System.out.println("0/1 Knapsack");
        System.out.printf("  Recursive: %d%n", knapsackRecursive(w, v, cap, w.length - 1));
        System.out.printf("  Optimized: %d%n", knapsackOptimized(w, v, cap));
    }
}
