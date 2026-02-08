package ch23.tests;

import java.util.*;

/**
 * Tests for Chapter 23: Dynamic Programming I — The Foundation
 *
 * Build and run:
 *   cd code/java
 *   javac ch23/tests/TestCh23.java
 *   java -ea ch23.tests.TestCh23
 */
public class TestCh23 {

    static int passed = 0;
    static int failed = 0;

    static void assertEquals(int expected, int actual, String msg) {
        if (expected == actual) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual);
        }
    }

    // ── Reference solutions ─────────────────────────────────────────

    // W1: Climbing Stairs
    static int refClimbingStairs(int n) {
        if (n <= 2) return n;
        int prev2 = 1, prev1 = 2;
        for (int i = 3; i <= n; i++) { int c = prev1 + prev2; prev2 = prev1; prev1 = c; }
        return prev1;
    }

    // W2: Fibonacci
    static int refFibonacci(int n) {
        if (n <= 1) return n;
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) { int c = a + b; a = b; b = c; }
        return b;
    }

    // W3: Min Cost Climbing Stairs
    static int refMinCostClimbing(int[] cost) {
        int n = cost.length;
        int prev2 = 0, prev1 = 0;
        for (int i = 2; i <= n; i++) {
            int c = Math.min(prev1 + cost[i - 1], prev2 + cost[i - 2]);
            prev2 = prev1; prev1 = c;
        }
        return prev1;
    }

    // W4: House Robber
    static int refHouseRobber(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        int prev2 = nums[0], prev1 = Math.max(nums[0], nums[1]);
        for (int i = 2; i < nums.length; i++) {
            int c = Math.max(prev1, prev2 + nums[i]); prev2 = prev1; prev1 = c;
        }
        return prev1;
    }

    // W5: Max Subarray (Kadane)
    static int refMaxSubarray(int[] nums) {
        int cur = nums[0], best = nums[0];
        for (int i = 1; i < nums.length; i++) {
            cur = Math.max(cur + nums[i], nums[i]);
            best = Math.max(best, cur);
        }
        return best;
    }

    // P1: Frog Jump K
    static int refFrogJumpK(int[] costs, int k) {
        int n = costs.length;
        if (n <= 1) return n == 1 ? costs[0] : 0;
        int[] dp = new int[n];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = costs[0];
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= Math.min(k, i); j++) dp[i] = Math.min(dp[i], dp[i - j]);
            dp[i] += costs[i];
        }
        return dp[n - 1];
    }

    // P2: House Robber II
    static int refHouseRobberII(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);
        return Math.max(robRange(nums, 0, n - 2), robRange(nums, 1, n - 1));
    }
    static int robRange(int[] nums, int lo, int hi) {
        int p2 = nums[lo], p1 = Math.max(nums[lo], nums[lo + 1]);
        for (int i = lo + 2; i <= hi; i++) { int c = Math.max(p1, p2 + nums[i]); p2 = p1; p1 = c; }
        return p1;
    }

    // P3: Decode Ways
    static int refDecodeWays(String s) {
        if (s.isEmpty() || s.charAt(0) == '0') return 0;
        int p2 = 1, p1 = 1;
        for (int i = 2; i <= s.length(); i++) {
            int c = 0;
            if (s.charAt(i - 1) != '0') c += p1;
            int td = Integer.parseInt(s.substring(i - 2, i));
            if (td >= 10 && td <= 26) c += p2;
            p2 = p1; p1 = c;
        }
        return p1;
    }

    // P4: Stock I
    static int refStockI(int[] prices) {
        if (prices.length == 0) return 0;
        int min = prices[0], profit = 0;
        for (int i = 1; i < prices.length; i++) {
            profit = Math.max(profit, prices[i] - min);
            min = Math.min(min, prices[i]);
        }
        return profit;
    }

    // P5: Stock II
    static int refStockII(int[] prices) {
        int profit = 0;
        for (int i = 1; i < prices.length; i++)
            if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
        return profit;
    }

    // P6: Tribonacci
    static int refTribonacci(int n) {
        if (n == 0) return 0;
        if (n <= 2) return 1;
        int a = 0, b = 1, c = 1;
        for (int i = 3; i <= n; i++) { int next = a + b + c; a = b; b = c; c = next; }
        return c;
    }

    // C1: Stock III
    static int refStockIII(int[] prices) {
        if (prices.length == 0) return 0;
        int b1 = -prices[0], s1 = 0, b2 = -prices[0], s2 = 0;
        for (int i = 1; i < prices.length; i++) {
            b1 = Math.max(b1, -prices[i]);
            s1 = Math.max(s1, b1 + prices[i]);
            b2 = Math.max(b2, s1 - prices[i]);
            s2 = Math.max(s2, b2 + prices[i]);
        }
        return s2;
    }

    // C2: Stock Cooldown
    static int refStockCooldown(int[] prices) {
        if (prices.length == 0) return 0;
        int held = -prices[0], sold = 0, rest = 0;
        for (int i = 1; i < prices.length; i++) {
            int ph = held;
            held = Math.max(held, rest - prices[i]);
            rest = Math.max(rest, sold);
            sold = ph + prices[i];
        }
        return Math.max(sold, rest);
    }

    // C3: Stock Fee
    static int refStockFee(int[] prices, int fee) {
        if (prices.length == 0) return 0;
        int cash = 0, hold = -prices[0];
        for (int i = 1; i < prices.length; i++) {
            cash = Math.max(cash, hold + prices[i] - fee);
            hold = Math.max(hold, cash - prices[i]);
        }
        return cash;
    }

    // C4: House Robber III
    static int refHouseRobberIII(int[] tree) {
        if (tree.length == 0) return 0;
        int[] r = dfsTree(tree, 0);
        return Math.max(r[0], r[1]);
    }
    static int[] dfsTree(int[] tree, int idx) {
        if (idx >= tree.length || tree[idx] == -1) return new int[]{0, 0};
        int[] l = dfsTree(tree, 2 * idx + 1);
        int[] r = dfsTree(tree, 2 * idx + 2);
        int rob = tree[idx] + l[1] + r[1];
        int skip = Math.max(l[0], l[1]) + Math.max(r[0], r[1]);
        return new int[]{rob, skip};
    }

    // C5: LIS
    static int refLIS(int[] nums) {
        if (nums.length == 0) return 0;
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        int best = 1;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++)
                if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
            best = Math.max(best, dp[i]);
        }
        return best;
    }

    // ── Tests ───────────────────────────────────────────────────────

    static void testW1() {
        assertEquals(1, refClimbingStairs(1), "W1: n=1");
        assertEquals(2, refClimbingStairs(2), "W1: n=2");
        assertEquals(3, refClimbingStairs(3), "W1: n=3");
        assertEquals(8, refClimbingStairs(5), "W1: n=5");
        assertEquals(89, refClimbingStairs(10), "W1: n=10");
    }

    static void testW2() {
        assertEquals(0, refFibonacci(0), "W2: n=0");
        assertEquals(1, refFibonacci(1), "W2: n=1");
        assertEquals(1, refFibonacci(2), "W2: n=2");
        assertEquals(55, refFibonacci(10), "W2: n=10");
        assertEquals(6765, refFibonacci(20), "W2: n=20");
    }

    static void testW3() {
        assertEquals(15, refMinCostClimbing(new int[]{10, 15, 20}), "W3: [10,15,20]");
        assertEquals(6, refMinCostClimbing(new int[]{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}), "W3: long");
        assertEquals(10, refMinCostClimbing(new int[]{10, 15}), "W3: [10,15]");
        assertEquals(10, refMinCostClimbing(new int[]{5, 5, 5, 5}), "W3: [5,5,5,5]");
        assertEquals(6, refMinCostClimbing(new int[]{1, 2, 3, 4, 5}), "W3: [1,2,3,4,5]");
    }

    static void testW4() {
        assertEquals(4, refHouseRobber(new int[]{1, 2, 3, 1}), "W4: [1,2,3,1]");
        assertEquals(12, refHouseRobber(new int[]{2, 7, 9, 3, 1}), "W4: [2,7,9,3,1]");
        assertEquals(5, refHouseRobber(new int[]{5}), "W4: [5]");
        assertEquals(2, refHouseRobber(new int[]{1, 2}), "W4: [1,2]");
        assertEquals(4, refHouseRobber(new int[]{2, 1, 1, 2}), "W4: [2,1,1,2]");
    }

    static void testW5() {
        assertEquals(6, refMaxSubarray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}), "W5: mixed");
        assertEquals(1, refMaxSubarray(new int[]{1}), "W5: [1]");
        assertEquals(23, refMaxSubarray(new int[]{5, 4, -1, 7, 8}), "W5: all positive");
        assertEquals(-1, refMaxSubarray(new int[]{-1, -2, -3}), "W5: all negative");
    }

    static void testP1() {
        assertEquals(3, refFrogJumpK(new int[]{0, 3, 2, 6, 1}, 2), "P1: k=2");
        assertEquals(20, refFrogJumpK(new int[]{10, 20, 30, 10}, 3), "P1: k=3");
        assertEquals(5, refFrogJumpK(new int[]{5}, 1), "P1: single");
        assertEquals(100, refFrogJumpK(new int[]{10, 30, 40, 20}, 1), "P1: k=1");
        assertEquals(60, refFrogJumpK(new int[]{10, 30, 40, 20}, 2), "P1: k=2 v2");
    }

    static void testP2() {
        assertEquals(3, refHouseRobberII(new int[]{2, 3, 2}), "P2: [2,3,2]");
        assertEquals(4, refHouseRobberII(new int[]{1, 2, 3, 1}), "P2: [1,2,3,1]");
        assertEquals(3, refHouseRobberII(new int[]{1, 2, 3}), "P2: [1,2,3]");
        assertEquals(5, refHouseRobberII(new int[]{5}), "P2: [5]");
        assertEquals(2, refHouseRobberII(new int[]{1, 2}), "P2: [1,2]");
        assertEquals(103, refHouseRobberII(new int[]{1, 3, 1, 3, 100}), "P2: [1,3,1,3,100]");
    }

    static void testP3() {
        assertEquals(2, refDecodeWays("12"), "P3: 12");
        assertEquals(3, refDecodeWays("226"), "P3: 226");
        assertEquals(0, refDecodeWays("06"), "P3: 06");
        assertEquals(1, refDecodeWays("1"), "P3: 1");
        assertEquals(1, refDecodeWays("10"), "P3: 10");
        assertEquals(1, refDecodeWays("27"), "P3: 27");
        assertEquals(3, refDecodeWays("1234"), "P3: 1234");
    }

    static void testP4() {
        assertEquals(5, refStockI(new int[]{7, 1, 5, 3, 6, 4}), "P4: basic");
        assertEquals(0, refStockI(new int[]{7, 6, 4, 3, 1}), "P4: decreasing");
        assertEquals(0, refStockI(new int[]{1}), "P4: single");
        assertEquals(1, refStockI(new int[]{1, 2}), "P4: [1,2]");
    }

    static void testP5() {
        assertEquals(7, refStockII(new int[]{7, 1, 5, 3, 6, 4}), "P5: basic");
        assertEquals(4, refStockII(new int[]{1, 2, 3, 4, 5}), "P5: increasing");
        assertEquals(0, refStockII(new int[]{7, 6, 4, 3, 1}), "P5: decreasing");
        assertEquals(0, refStockII(new int[]{5}), "P5: single");
    }

    static void testP6() {
        assertEquals(0, refTribonacci(0), "P6: n=0");
        assertEquals(1, refTribonacci(1), "P6: n=1");
        assertEquals(1, refTribonacci(2), "P6: n=2");
        assertEquals(4, refTribonacci(4), "P6: n=4");
        assertEquals(1389537, refTribonacci(25), "P6: n=25");
    }

    static void testC1() {
        assertEquals(6, refStockIII(new int[]{3, 3, 5, 0, 0, 3, 1, 4}), "C1: basic");
        assertEquals(4, refStockIII(new int[]{1, 2, 3, 4, 5}), "C1: increasing");
        assertEquals(0, refStockIII(new int[]{7, 6, 4, 3, 1}), "C1: decreasing");
        assertEquals(0, refStockIII(new int[]{1}), "C1: single");
    }

    static void testC2() {
        assertEquals(3, refStockCooldown(new int[]{1, 2, 3, 0, 2}), "C2: basic");
        assertEquals(0, refStockCooldown(new int[]{1}), "C2: single");
        assertEquals(1, refStockCooldown(new int[]{1, 2}), "C2: [1,2]");
        assertEquals(0, refStockCooldown(new int[]{5, 4, 3, 2, 1}), "C2: decreasing");
        assertEquals(6, refStockCooldown(new int[]{1, 4, 2, 7}), "C2: alternating");
    }

    static void testC3() {
        assertEquals(8, refStockFee(new int[]{1, 3, 2, 8, 4, 9}, 2), "C3: basic");
        assertEquals(6, refStockFee(new int[]{1, 3, 7, 5, 10, 3}, 3), "C3: basic2");
        assertEquals(0, refStockFee(new int[]{5}, 1), "C3: single");
        assertEquals(0, refStockFee(new int[]{7, 6, 4, 3, 1}, 2), "C3: no profit");
        assertEquals(4, refStockFee(new int[]{1, 2, 3, 4, 5}, 0), "C3: zero fee");
    }

    static void testC4() {
        assertEquals(7, refHouseRobberIII(new int[]{3, 2, 3, -1, 3, -1, 1}), "C4: basic");
        assertEquals(9, refHouseRobberIII(new int[]{3, 4, 5, 1, 3, -1, 1}), "C4: basic2");
        assertEquals(1, refHouseRobberIII(new int[]{1}), "C4: single");
        assertEquals(5, refHouseRobberIII(new int[]{1, 2, 3}), "C4: two levels");
    }

    static void testC5() {
        assertEquals(4, refLIS(new int[]{10, 9, 2, 5, 3, 7, 101, 18}), "C5: basic");
        assertEquals(4, refLIS(new int[]{0, 1, 0, 3, 2, 3}), "C5: mixed");
        assertEquals(1, refLIS(new int[]{7, 7, 7, 7}), "C5: all same");
        assertEquals(5, refLIS(new int[]{1, 2, 3, 4, 5}), "C5: increasing");
        assertEquals(1, refLIS(new int[]{5, 4, 3, 2, 1}), "C5: decreasing");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 23: Dynamic Programming I — The Foundation");
        System.out.println("====================================================\n");

        testW1(); testW2(); testW3(); testW4(); testW5();
        testP1(); testP2(); testP3(); testP4(); testP5(); testP6();
        testC1(); testC2(); testC3(); testC4(); testC5();

        System.out.println();
        if (failed == 0) {
            System.out.println("All " + passed + " tests passed!");
        } else {
            System.out.println(passed + " passed, " + failed + " failed.");
            System.exit(1);
        }
    }
}
