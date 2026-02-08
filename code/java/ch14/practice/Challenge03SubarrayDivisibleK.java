package ch14.practice;

import java.util.*;

/**
 * Challenge 3: Subarray Sum Divisible by K
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Count subarrays with sum divisible by k.
 *
 * EXAMPLES:
 *   solve([4,5,0,-2,-3,1], 5) -> 7
 *   solve([5], 9)             -> 0
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge03SubarrayDivisibleK {
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
