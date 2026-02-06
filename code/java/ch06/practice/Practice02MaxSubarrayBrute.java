package ch06.practice;

import java.util.*;

/**
 * Practice 02: Max Subarray Sum (Brute Force)
 * =============================================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM
 * -------
 * Given an integer array nums, find the contiguous subarray (containing
 * at least one number) which has the largest sum and return that sum.
 * Use the brute-force O(n^2) approach: try every possible start and end.
 *
 * For an empty array, return 0.
 *
 * INPUT FORMAT
 * ------------
 * A single line of space-separated integers (may be empty).
 *
 * OUTPUT FORMAT
 * -------------
 * Print the maximum subarray sum.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= nums.length <= 10^4
 * -10^4 <= nums[i] <= 10^4
 *
 * EXAMPLES
 * --------
 * Input:  -2 1 -3 4 -1 2 1 -5 4    Output: 6   (subarray [4,-1,2,1])
 * Input:  1                          Output: 1
 * Input:  -1 -2 -3                   Output: -1
 * Input:  5 4 -1 7 8                 Output: 23
 *
 * HINT
 * ----
 * For each starting index i, compute the running sum as you extend to
 * each ending index j. Track the maximum sum seen.
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in solve() with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Practice02MaxSubarrayBrute {

    /**
     * Find the maximum subarray sum using brute force.
     *
     * @param nums the input array
     * @return maximum subarray sum, or 0 for empty array
     */
    public static int solve(int[] nums) {
        // TODO: Replace this with your solution
        return 0;
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
