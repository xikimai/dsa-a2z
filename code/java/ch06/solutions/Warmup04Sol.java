package ch06.solutions;

import java.util.*;

/**
 * Solution for Warmup 04: Sum of 1 to N
 * =======================================
 * Chapter 6: How Fast Is Your Code?
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Three methods to compute 1 + 2 + ... + n:
 *   1. O(n) loop: accumulate in a variable
 *   2. O(1) formula: n * (n + 1) / 2
 *   3. O(n^2) nested: for each i from 1..n, for each j from 1..i, add 1
 *
 * All three produce the same answer — the point is to see the speed difference.
 */
public class Warmup04Sol {

    public static int[] solve(int n) {
        // Method 1: Loop — O(n)
        int loopResult = 0;
        for (int i = 1; i <= n; i++) {
            loopResult += i;
        }

        // Method 2: Formula — O(1)
        int formulaResult = n * (n + 1) / 2;

        // Method 3: Nested loops — O(n^2)
        int nestedResult = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                nestedResult++;
            }
        }

        return new int[]{loopResult, formulaResult, nestedResult};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        int[] result = solve(n);
        System.out.println(result[0] + " " + result[1] + " " + result[2]);
        sc.close();
    }
}
