package ch11.practice;

import java.util.*;

/**
 * Warmup 1: Frequency Count
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given an integer array, return a list of {value, count} pairs
 *          representing the frequency of each element.
 *          The result should be sorted by value in ascending order.
 *
 * EXAMPLES:
 *   solve([1,2,2,3,3,3]) -> [[1,1],[2,2],[3,3]]
 *   solve([5])            -> [[5,1]]
 *   solve([])             -> []
 *   solve([3,1,2,1])      -> [[1,2],[2,1],[3,1]]
 *
 * CONSTRAINTS:
 *   - 0 <= arr.length <= 10^5
 *   - -10^9 <= arr[i] <= 10^9
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup01FrequencyCount {
    public static List<int[]> solve(int[] arr) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        List<int[]> result = solve(arr);
        for (int[] pair : result) {
            System.out.println(pair[0] + " " + pair[1]);
        }
        sc.close();
    }
}
