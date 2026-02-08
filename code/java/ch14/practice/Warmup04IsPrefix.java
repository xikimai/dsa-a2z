package ch14.practice;

import java.util.*;

/**
 * Warmup 4: Is Array Prefix of Another
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Return true if arr1 is a prefix of arr2.
 *
 * EXAMPLES:
 *   solve([1,2,3], [1,2,3,4,5]) -> true
 *   solve([1,2,4], [1,2,3,4,5]) -> false
 *   solve([], [1,2,3])           -> true
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04IsPrefix {
    public static boolean solve(int[] arr1, int[] arr2) {
        // TODO: Replace this with your solution
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line1 = sc.nextLine().trim();
        String line2 = sc.nextLine().trim();
        int[] arr1 = line1.isEmpty() ? new int[]{} : Arrays.stream(line1.split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] arr2 = line2.isEmpty() ? new int[]{} : Arrays.stream(line2.split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(arr1, arr2));
        sc.close();
    }
}
