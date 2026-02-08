package ch11.practice;

import java.util.*;

/**
 * Practice 4: Count Subarrays with Sum K
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given an integer array and a target sum k, count the total number
 *          of contiguous subarrays whose elements sum to k.
 *          Use prefix sum + frequency hash map. Initialize map with {0: 1}.
 *
 * EXAMPLES:
 *   solve([1,1,1], 2)   -> 2
 *   solve([1,2,3], 3)   -> 2
 *   solve([1], 0)       -> 0
 *   solve([1,-1,0], 0)  -> 3
 *   solve([0,0,0], 0)   -> 6
 *   solve([1], 1)       -> 1
 *
 * CONSTRAINTS:
 *   - 1 <= arr.length <= 2 * 10^4
 *   - -1000 <= arr[i] <= 1000
 *   - -10^7 <= k <= 10^7
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04CountSubarraysSumK {
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
