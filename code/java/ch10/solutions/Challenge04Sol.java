package ch10.solutions;

import java.util.*;

/**
 * Solution for Challenge 04: Subset Sum
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Backtracking. At each index, either include the element
 *           (subtract from remaining) or exclude it. Return true if
 *           remaining reaches 0; false if past end or remaining < 0.
 *
 * TIME COMPLEXITY:  O(2^n)
 * SPACE COMPLEXITY: O(n) — call stack depth
 */
public class Challenge04Sol {

    public static boolean solve(int[] nums, int target) {
        return helper(nums, 0, target);
    }

    private static boolean helper(int[] nums, int idx, int remaining) {
        if (remaining == 0) return true;
        if (idx == nums.length || remaining < 0) return false;
        // Include nums[idx] or exclude it
        return helper(nums, idx + 1, remaining - nums[idx])
            || helper(nums, idx + 1, remaining);
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
