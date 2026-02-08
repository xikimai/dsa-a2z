package ch10.practice;

import java.util.*;

/**
 * Challenge 02: Generate All Permutations
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given an array of distinct integers, return all possible permutations
 *          sorted in lexicographic order.
 *
 * ALGORITHM: Backtracking — at each position, try every unused element.
 *
 * EXAMPLES:
 *   solve(new int[]{1,2,3}) = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 *   solve(new int[]{1})     = [[1]]
 *
 * CONSTRAINTS: 1 <= nums.length <= 8, all elements are distinct
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge02GeneratePermutations {
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
        for (List<Integer> perm : result) {
            System.out.println(perm);
        }
        sc.close();
    }
}
