package ch14.practice;

import java.util.*;

/**
 * Practice 5: Maximum Subarray Sum (Kadane's Algorithm)
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Find the maximum contiguous subarray sum. Handle all-negative arrays.
 *
 * EXAMPLES:
 *   solve([-2,1,-3,4,-1,2,1,-5,4]) -> 6
 *   solve([-5,-3,-1,-4])           -> -1
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice05MaxSubarraySum {
    public static long solve(int[] arr) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(arr));
        sc.close();
    }
}
