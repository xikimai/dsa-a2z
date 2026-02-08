package ch14.practice;

import java.util.*;

/**
 * Practice 3: Product of Array Except Self
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Return array where result[i] = product of all elements except arr[i].
 *          Do NOT use division.
 *
 * EXAMPLES:
 *   solve([1,2,3,4])      -> [24, 12, 8, 6]
 *   solve([-1,1,0,-3,3])  -> [0, 0, 9, 0, 0]
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice03ProductExceptSelf {
    public static long[] solve(int[] arr) {
        // TODO: Replace this with your solution
        return new long[arr.length];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(Arrays.toString(solve(arr)));
        sc.close();
    }
}
