package ch05.practice;

import java.util.*;

/**
 * Practice 03: Two Sum
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given an array of integers and a target sum, return the indices
 * of the two numbers that add up to the target. If no such pair
 * exists, return [-1, -1].
 *
 * You may assume each input has at most one solution, and you
 * may not use the same element twice.
 *
 * INPUT FORMAT
 * ------------
 * First line: space-separated integers (the array).
 * Second line: a single integer (the target).
 *
 * OUTPUT FORMAT
 * -------------
 * Print two space-separated indices.
 *
 * CONSTRAINTS
 * -----------
 * 2 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * -10^9 <= target <= 10^9
 *
 * EXAMPLES
 * --------
 * Input:
 * 2 7 11 15
 * 9
 * Output: 0 1
 *
 * Input:
 * 3 3
 * 6
 * Output: 0 1
 *
 * Input:
 * 1 2 3
 * 10
 * Output: -1 -1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return new int[]{-1, -1};" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Practice03TwoSum {

    /**
     * Return indices of two numbers that add to target, or {-1, -1}.
     *
     * @param nums   the input array
     * @param target the target sum
     * @return int[2] with the two indices, or {-1, -1}
     */
    public static int[] solve(int[] nums, int target) {
        // TODO: Replace this with your solution
        return new int[]{-1, -1};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = Arrays.stream(sc.nextLine().trim().split("\\s+"))
                           .mapToInt(Integer::parseInt).toArray();
        int target = Integer.parseInt(sc.nextLine().trim());
        int[] result = solve(nums, target);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
