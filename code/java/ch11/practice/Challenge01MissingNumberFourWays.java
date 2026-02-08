package ch11.practice;

import java.util.*;

/**
 * Challenge 1: Missing Number — Four Ways (AOPS Showcase)
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given an array of n distinct numbers from [0, n], find the missing
 *          number using FOUR different techniques:
 *            1. solveSort  — Sort and scan for the gap
 *            2. solveXor   — XOR all indices and values
 *            3. solveMath  — Use the sum formula n*(n+1)/2
 *            4. solveHash  — Use a HashSet
 *          The default solve() method should call solveMath.
 *
 * EXAMPLES:
 *   solve([3,0,1])                 -> 2
 *   solve([0,1])                   -> 2
 *   solve([9,6,4,2,3,5,7,0,1])    -> 8
 *   solve([1])                     -> 0
 *   solve([0])                     -> 1
 *
 * CONSTRAINTS:
 *   - 1 <= nums.length <= 10^4
 *   - 0 <= nums[i] <= nums.length
 *   - All numbers in nums are unique
 *
 * INSTRUCTIONS: Implement all four methods.
 */
public class Challenge01MissingNumberFourWays {
    public static int solveSort(int[] nums) {
        // TODO: Sort the array and find the gap
        return -1;
    }

    public static int solveXor(int[] nums) {
        // TODO: XOR all indices 0..n with all values
        return -1;
    }

    public static int solveMath(int[] nums) {
        // TODO: Use n*(n+1)/2 minus actual sum
        return -1;
    }

    public static int solveHash(int[] nums) {
        // TODO: Put all values in a HashSet and find the missing one
        return -1;
    }

    public static int solve(int[] nums) {
        // Default: delegate to solveMath
        return solveMath(nums);
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
