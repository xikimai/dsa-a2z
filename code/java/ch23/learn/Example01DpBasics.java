package ch23.learn;

import java.util.*;

/**
 * Example 01: DP Basics — The Four Stages of Climbing Stairs
 * ===========================================================
 * Chapter 23: Dynamic Programming I — The Foundation
 *
 * Demonstrates: recursion -> memo -> tabulation -> space-optimized
 */
public class Example01DpBasics {

    // Stage 1: Pure Recursion O(2^n)
    static int climbRecursive(int n) {
        if (n <= 1) return 1;
        return climbRecursive(n - 1) + climbRecursive(n - 2);
    }

    // Stage 2: Memoization O(n)
    static int climbMemo(int n, HashMap<Integer, Integer> memo) {
        if (n <= 1) return 1;
        if (memo.containsKey(n)) return memo.get(n);
        int result = climbMemo(n - 1, memo) + climbMemo(n - 2, memo);
        memo.put(n, result);
        return result;
    }

    // Stage 3: Tabulation O(n) time, O(n) space
    static int climbTabulation(int n) {
        if (n <= 1) return 1;
        int[] dp = new int[n + 1];
        dp[0] = 1; dp[1] = 1;
        for (int i = 2; i <= n; i++) dp[i] = dp[i - 1] + dp[i - 2];
        return dp[n];
    }

    // Stage 4: Space-Optimized O(n) time, O(1) space
    static int climbOptimized(int n) {
        if (n <= 1) return 1;
        int prev2 = 1, prev1 = 1;
        for (int i = 2; i <= n; i++) {
            int current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }

    // House Robber
    static int houseRobber(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        int prev2 = nums[0];
        int prev1 = Math.max(nums[0], nums[1]);
        for (int i = 2; i < nums.length; i++) {
            int current = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }

    // Kadane's Algorithm
    static int maxSubarray(int[] nums) {
        int current = nums[0], best = nums[0];
        for (int i = 1; i < nums.length; i++) {
            current = Math.max(current + nums[i], nums[i]);
            best = Math.max(best, current);
        }
        return best;
    }

    public static void main(String[] args) {
        System.out.println("Climbing Stairs — Four Stages");
        for (int n : new int[]{1, 2, 3, 5, 10}) {
            System.out.printf("  n=%d: %d ways%n", n, climbOptimized(n));
        }

        System.out.println("\nHouse Robber");
        System.out.printf("  [1,2,3,1] -> %d%n", houseRobber(new int[]{1,2,3,1}));
        System.out.printf("  [2,7,9,3,1] -> %d%n", houseRobber(new int[]{2,7,9,3,1}));

        System.out.println("\nKadane's Algorithm");
        System.out.printf("  [-2,1,-3,4,-1,2,1,-5,4] -> %d%n",
            maxSubarray(new int[]{-2,1,-3,4,-1,2,1,-5,4}));
    }
}
