package ch11.practice;

import java.util.*;

/**
 * Challenge 3: Repeating and Missing Number
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given an array of n integers where each integer is in the range [1, n].
 *          Exactly one number appears twice and exactly one number is missing.
 *          Find both and return {repeating, missing}.
 *
 * EXAMPLES:
 *   solve([3,1,2,5,3])    -> [3,4]
 *   solve([1,1])          -> [1,2]
 *   solve([2,2])          -> [2,1]
 *   solve([4,3,6,2,1,1])  -> [1,5]
 *   solve([1,2,3,4,4])    -> [4,5]
 *
 * CONSTRAINTS:
 *   - 2 <= nums.length <= 10^4
 *   - 1 <= nums[i] <= nums.length
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge03RepeatingMissing {
    public static int[] solve(int[] nums) {
        // TODO: Replace this with your solution
        return new int[]{0, 0};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        int[] result = solve(nums);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
