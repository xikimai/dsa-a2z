package ch13.learn;

import java.util.*;

/**
 * Example 02: Backtracking Patterns
 * ====================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * Demonstrates:
 *   Part 1 — N-Queens step-by-step
 *   Part 2 — Subset sum with pruning
 */
public class Example02BacktrackingPatterns {

    // ── Part 1: N-Queens ──
    static int nQueensCount;

    static void solveNQueens(int row, int n, Set<Integer> cols,
                             Set<Integer> diag1, Set<Integer> diag2) {
        if (row == n) { nQueensCount++; return; }
        for (int col = 0; col < n; col++) {
            if (cols.contains(col) || diag1.contains(row - col) || diag2.contains(row + col))
                continue;
            cols.add(col); diag1.add(row - col); diag2.add(row + col);
            solveNQueens(row + 1, n, cols, diag1, diag2);
            cols.remove(col); diag1.remove(row - col); diag2.remove(row + col);
        }
    }

    // ── Part 2: Subset Sum with Pruning ──
    static void subsetSum(int[] nums, int target, int index, int sum,
                          List<Integer> current, List<List<Integer>> results) {
        if (sum == target) { results.add(new ArrayList<>(current)); return; }
        if (sum > target) return;
        for (int i = index; i < nums.length; i++) {
            if (sum + nums[i] > target) break;
            current.add(nums[i]);
            subsetSum(nums, target, i + 1, sum + nums[i], current, results);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        // Part 1
        System.out.println("=== N-Queens Solution Counts ===");
        for (int n = 1; n <= 8; n++) {
            nQueensCount = 0;
            solveNQueens(0, n, new HashSet<>(), new HashSet<>(), new HashSet<>());
            System.out.println("  N=" + n + ": " + nQueensCount + " solutions");
        }

        // Part 2
        System.out.println("\n=== Subset Sum with Pruning ===");
        int[] nums = {1, 3, 4, 7, 8};
        int target = 11;
        Arrays.sort(nums);
        List<List<Integer>> results = new ArrayList<>();
        subsetSum(nums, target, 0, 0, new ArrayList<>(), results);
        System.out.println("Subsets of " + Arrays.toString(nums) + " summing to " + target + ":");
        for (List<Integer> r : results) System.out.println("  " + r);
    }
}
