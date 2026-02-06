package ch06.solutions;

import java.util.*;

/**
 * Solution for Practice 02: Max Subarray Sum (Brute Force)
 * =========================================================
 * Chapter 6: How Fast Is Your Code?
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Try every starting index i. For each i, extend the subarray to j,
 * maintaining a running sum. Track the maximum sum seen across all
 * subarrays. Return 0 for empty input.
 *
 * TIME COMPLEXITY:  O(n^2)
 * SPACE COMPLEXITY: O(1)
 */
public class Practice02Sol {

    public static int solve(int[] nums) {
        if (nums.length == 0) return 0;

        int maxSum = nums[0];
        for (int i = 0; i < nums.length; i++) {
            int currentSum = 0;
            for (int j = i; j < nums.length; j++) {
                currentSum += nums[j];
                if (currentSum > maxSum) {
                    maxSum = currentSum;
                }
            }
        }
        return maxSum;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println(solve(new int[0]));
        } else {
            int[] nums = Arrays.stream(line.split("\\s+"))
                               .mapToInt(Integer::parseInt).toArray();
            System.out.println(solve(nums));
        }
        sc.close();
    }
}
