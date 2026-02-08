package ch14.practice;

import java.util.*;

/**
 * Practice 2: Subarray Sum Equals K (Count)
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Count subarrays with sum equal to k.
 *
 * EXAMPLES:
 *   solve([1,1,1], 2)   -> 2
 *   solve([1,2,3], 3)   -> 2
 *   solve([1,-1,0], 0)  -> 3
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice02SubarraySumK {
    public static int solve(int[] arr, int k) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int k = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(arr, k));
        sc.close();
    }
}
