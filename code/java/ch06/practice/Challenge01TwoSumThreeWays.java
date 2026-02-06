package ch06.practice;

import java.util.*;

/**
 * Challenge 01: Two Sum — Three Ways
 * ====================================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM
 * -------
 * Given an array of integers and a target sum, find two indices i and j
 * (i < j) such that nums[i] + nums[j] == target.
 *
 * Implement THREE different approaches:
 *   1. solveBrute: O(n^2) — try every pair
 *   2. solveSort:  O(n log n) — sort + two pointers (track original indices)
 *   3. solveHash:  O(n) — hash map lookup
 *
 * Return {i, j} where i < j, or {-1, -1} if no solution exists.
 * The solve() method should call solveHash (the fastest one).
 *
 * INPUT FORMAT
 * ------------
 * Line 1: space-separated integers (nums)
 * Line 2: target integer
 *
 * OUTPUT FORMAT
 * -------------
 * Print two space-separated integers: i j
 *
 * CONSTRAINTS
 * -----------
 * 2 <= nums.length <= 10^4
 * -10^9 <= nums[i] <= 10^9
 * At most one valid answer exists.
 *
 * EXAMPLES
 * --------
 * Input:       Output:
 * 2 7 11 15    0 1
 * 9
 *
 * Input:       Output:
 * 3 3          0 1
 * 6
 *
 * Input:       Output:
 * 1 2 3        -1 -1
 * 10
 *
 * INSTRUCTIONS
 * ------------
 * Implement all three methods. The main method calls solve() which should
 * use the hash approach. Don't change the main method.
 */
public class Challenge01TwoSumThreeWays {

    /**
     * Brute force: O(n^2) — try every pair.
     */
    public static int[] solveBrute(int[] nums, int target) {
        // TODO: Replace this with your solution
        return new int[]{-1, -1};
    }

    /**
     * Sort + two pointers: O(n log n).
     * Remember to return original indices, not sorted indices!
     */
    public static int[] solveSort(int[] nums, int target) {
        // TODO: Replace this with your solution
        return new int[]{-1, -1};
    }

    /**
     * Hash map: O(n) — the fastest approach.
     */
    public static int[] solveHash(int[] nums, int target) {
        // TODO: Replace this with your solution
        return new int[]{-1, -1};
    }

    /**
     * Default solve uses the hash approach.
     */
    public static int[] solve(int[] nums, int target) {
        return solveHash(nums, target);
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
