package ch15.practice;

import java.util.*;

/**
 * Practice 4: Subarray Sum Equals K (Sliding Window)
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Count subarrays with sum == k (positive integers only).
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04SubarraySumEqualsK {
    public static int solve(int[] arr, int k) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] arr = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        int k = sc.nextInt();
        System.out.println(solve(arr, k));
        sc.close();
    }
}
