package ch14.practice;

import java.util.*;

/**
 * Warmup 3: Running Sum of Array
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Return the running sum where running_sum[i] = arr[0]+...+arr[i].
 *
 * EXAMPLES:
 *   solve([1,2,3,4]) -> [1, 3, 6, 10]
 *   solve([5])        -> [5]
 *   solve([])         -> []
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup03RunningSum {
    public static long[] solve(int[] arr) {
        // TODO: Replace this with your solution
        return new long[0];
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
