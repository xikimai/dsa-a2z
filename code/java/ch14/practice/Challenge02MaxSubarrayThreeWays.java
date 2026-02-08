package ch14.practice;

import java.util.*;

/**
 * Challenge 2: Maximum Subarray Sum Three Ways (AOPS)
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Find max subarray sum using brute O(n^3), prefix O(n^2), Kadane's O(n).
 *
 * INSTRUCTIONS: Replace the body of each solve method with your solution.
 */
public class Challenge02MaxSubarrayThreeWays {
    public static long solveBrute(int[] arr) {
        // TODO: O(n^3) brute force
        return 0;
    }

    public static long solvePrefix(int[] arr) {
        // TODO: O(n^2) prefix sum
        return 0;
    }

    public static long solveKadane(int[] arr) {
        // TODO: O(n) Kadane's
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println("brute=" + solveBrute(arr) + " prefix=" + solvePrefix(arr)
            + " kadane=" + solveKadane(arr));
        sc.close();
    }
}
