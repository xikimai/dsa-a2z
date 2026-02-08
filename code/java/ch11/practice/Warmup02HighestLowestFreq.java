package ch11.practice;

import java.util.*;

/**
 * Warmup 2: Highest and Lowest Frequency
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given an integer array, find the element with the highest frequency
 *          and the element with the lowest frequency.
 *          Return them as {highest_freq_element, lowest_freq_element}.
 *          Test inputs guarantee each element has a unique frequency.
 *
 * EXAMPLES:
 *   solve([1,2,2,3,3,3])       -> [3,1]
 *   solve([10,10,10,20,20,30]) -> [10,30]
 *   solve([5])                 -> [5,5]
 *
 * CONSTRAINTS:
 *   - 1 <= arr.length <= 10^5
 *   - Each element has a unique frequency in the test inputs
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup02HighestLowestFreq {
    public static int[] solve(int[] arr) {
        // TODO: Replace this with your solution
        return new int[]{0, 0};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int[] result = solve(arr);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
