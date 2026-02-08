package ch10.practice;

import java.util.*;

/**
 * Challenge 04: Subset Sum
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given an array of non-negative integers and a target sum,
 *          return true if any subset of the array sums to the target.
 *          The empty subset has sum 0.
 *
 * ALGORITHM: Backtracking — at each element, include it or exclude it.
 *            If remaining == 0, return true. If past end or remaining < 0,
 *            return false.
 *
 * EXAMPLES:
 *   solve(new int[]{3,34,4,12,5,2}, 9)  = true   (4+5=9)
 *   solve(new int[]{3,34,4,12,5,2}, 30) = false
 *   solve(new int[]{}, 0)               = true    (empty subset)
 *
 * CONSTRAINTS: 0 <= nums.length <= 20, 0 <= nums[i] <= 1000, 0 <= target <= 10^4
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge04SubsetSum {
    public static boolean solve(int[] nums, int target) {
        // TODO: Replace this with your solution
        return false;
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
        int target = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(nums, target));
        sc.close();
    }
}
