package ch14.practice;

import java.util.*;

/**
 * Warmup 1: Build Prefix Sum Array
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Given an integer array, build the prefix sum array.
 *          prefix[0] = 0, prefix[i] = arr[0] + ... + arr[i-1].
 *
 * EXAMPLES:
 *   solve([3,1,4,1,5]) -> [0, 3, 4, 8, 9, 14]
 *   solve([5])          -> [0, 5]
 *   solve([])           -> [0]
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup01BuildPrefixSum {
    public static long[] solve(int[] arr) {
        // TODO: Replace this with your solution
        return new long[]{0};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println(Arrays.toString(solve(new int[]{})));
        } else {
            int[] arr = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
            System.out.println(Arrays.toString(solve(arr)));
        }
        sc.close();
    }
}
