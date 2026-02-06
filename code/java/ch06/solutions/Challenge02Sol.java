package ch06.solutions;

import java.util.*;

/**
 * Solution for Challenge 02: Performance Showdown
 * =================================================
 * Chapter 6: How Fast Is Your Code?
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Compute the number of operations for each complexity class, then compare.
 * Use long to avoid overflow. For 2^n with n > 30, use Long.MAX_VALUE.
 *
 * TIME COMPLEXITY:  O(1)
 * SPACE COMPLEXITY: O(1)
 */
public class Challenge02Sol {

    static long computeOps(String complexity, int n) {
        switch (complexity) {
            case "1":       return 1;
            case "log_n":   return Math.max(1, (long) (Math.log(n) / Math.log(2)));
            case "n":       return n;
            case "n_log_n": return (long) n * Math.max(1, (long) (Math.log(n) / Math.log(2)));
            case "n^2":     return (long) n * n;
            case "n^3":     return (long) n * n * n;
            case "2^n":
                if (n > 30) return Long.MAX_VALUE;
                return 1L << n;
            default:        return Long.MAX_VALUE;
        }
    }

    public static String solve(String complexityA, String complexityB, int n) {
        long opsA = computeOps(complexityA, n);
        long opsB = computeOps(complexityB, n);

        if (opsA < opsB) return "A";
        if (opsB < opsA) return "B";
        return "TIE";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split("\\s+");
        String complexityA = parts[0];
        String complexityB = parts[1];
        int n = Integer.parseInt(parts[2]);
        System.out.println(solve(complexityA, complexityB, n));
        sc.close();
    }
}
