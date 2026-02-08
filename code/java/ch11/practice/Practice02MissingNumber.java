package ch11.practice;

import java.util.*;

/**
 * Practice 2: Missing Number
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
 *          find the one number in the range that is missing from the array.
 *          Use a hash set approach.
 *
 * EXAMPLES:
 *   solve([3,0,1])                 -> 2
 *   solve([0,1])                   -> 2
 *   solve([9,6,4,2,3,5,7,0,1])    -> 8
 *   solve([0])                     -> 1
 *   solve([1])                     -> 0
 *
 * CONSTRAINTS:
 *   - 1 <= nums.length <= 10^4
 *   - 0 <= nums[i] <= nums.length
 *   - All numbers in nums are unique
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice02MissingNumber {
    public static int solve(int[] nums) {
        // TODO: Replace this with your solution
        return -1;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        System.out.println(solve(nums));
        sc.close();
    }
}
