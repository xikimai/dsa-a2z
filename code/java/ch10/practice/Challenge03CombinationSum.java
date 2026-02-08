package ch10.practice;

import java.util.*;

/**
 * Challenge 03: Combination Sum
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given an array of distinct positive integers (candidates) and a
 *          target integer, return all unique combinations where the candidates
 *          sum to target. The same candidate may be used unlimited times.
 *          Each combination should be sorted, and the result sorted lexicographically.
 *
 * ALGORITHM: Backtracking with index to avoid duplicates. At each step,
 *            either reuse the current candidate or move to the next.
 *
 * EXAMPLES:
 *   solve(new int[]{2,3,6,7}, 7) = [[2,2,3], [7]]
 *   solve(new int[]{2}, 1)       = []
 *   solve(new int[]{1}, 1)       = [[1]]
 *
 * CONSTRAINTS: 1 <= candidates.length <= 30, 1 <= candidates[i] <= 200,
 *              1 <= target <= 500
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge03CombinationSum {
    public static List<List<Integer>> solve(int[] candidates, int target) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] candidates;
        if (line.isEmpty()) {
            candidates = new int[0];
        } else {
            String[] parts = line.split("\\s+");
            candidates = new int[parts.length];
            for (int i = 0; i < parts.length; i++) candidates[i] = Integer.parseInt(parts[i]);
        }
        int target = Integer.parseInt(sc.nextLine().trim());
        List<List<Integer>> result = solve(candidates, target);
        for (List<Integer> combo : result) {
            System.out.println(combo);
        }
        sc.close();
    }
}
