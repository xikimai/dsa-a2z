package ch11.practice;

import java.util.*;

/**
 * Practice 3: Longest Subarray with Sum K
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given an integer array and a target sum k, find the length of the
 *          longest contiguous subarray whose elements sum to k.
 *          Use prefix sum + hash map. Store the earliest index of each prefix sum.
 *
 * EXAMPLES:
 *   solve([1,2,3,1,1,1,1], 3) -> 3
 *   solve([-1,1,1], 1)        -> 3
 *   solve([1,2,3], 10)        -> 0
 *   solve([1,-1,1,-1,1], 0)   -> 4
 *   solve([2,0,0,3], 3)       -> 3
 *   solve([1], 1)             -> 1
 *
 * CONSTRAINTS:
 *   - 1 <= arr.length <= 10^5
 *   - -10^5 <= arr[i] <= 10^5
 *   - -10^9 <= k <= 10^9
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice03LongestSubarraySumK {
    public static int solve(int[] arr, int k) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        System.out.println(solve(arr, k));
        sc.close();
    }
}
