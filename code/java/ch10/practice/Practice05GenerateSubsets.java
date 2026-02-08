package ch10.practice;

import java.util.*;

/**
 * Practice 05: Generate All Subsets
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given an array of distinct integers, return all possible subsets.
 *          The result should be sorted: first by subset size, then lexicographically.
 *
 * ALGORITHM: Backtracking — at each element, include it or exclude it.
 *
 * EXAMPLES:
 *   solve(new int[]{})      = [[]]
 *   solve(new int[]{1})     = [[], [1]]
 *   solve(new int[]{1,2,3}) = [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
 *
 * CONSTRAINTS: 0 <= nums.length <= 15, all elements are distinct
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice05GenerateSubsets {
    public static List<List<Integer>> solve(int[] nums) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] nums;
        if (line.isEmpty()) {
            nums = new int[0];
        } else {
            String[] parts = line.split("\\s+");
            nums = new int[parts.length];
            for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);
        }
        List<List<Integer>> result = solve(nums);
        for (List<Integer> subset : result) {
            System.out.println(subset);
        }
        sc.close();
    }
}
