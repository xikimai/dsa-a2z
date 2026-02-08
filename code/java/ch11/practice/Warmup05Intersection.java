package ch11.practice;

import java.util.*;

/**
 * Warmup 5: Intersection of Two Arrays
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given two integer arrays, return a sorted list of their unique
 *          common elements (the intersection).
 *
 * EXAMPLES:
 *   solve([1,2,2,1], [2,2])          -> [2]
 *   solve([4,9,5], [9,4,9,8,4])      -> [4,9]
 *   solve([1,2,3], [4,5,6])          -> []
 *   solve([], [1,2])                 -> []
 *   solve([1,1,1], [1])              -> [1]
 *
 * CONSTRAINTS:
 *   - 0 <= a.length, b.length <= 10^5
 *   - -10^9 <= a[i], b[i] <= 10^9
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup05Intersection {
    public static List<Integer> solve(int[] a, int[] b) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        int m = sc.nextInt();
        int[] b = new int[m];
        for (int i = 0; i < m; i++) b[i] = sc.nextInt();
        System.out.println(solve(a, b));
        sc.close();
    }
}
