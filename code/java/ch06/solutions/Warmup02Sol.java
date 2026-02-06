package ch06.solutions;

import java.util.*;

/**
 * Solution for Warmup 02: Is It Fast Enough?
 * ============================================
 * Chapter 6: How Fast Is Your Code?
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Map each complexity string to the number of operations, then check
 * if ops < 10^8. Use long to avoid overflow. For 2^n, short-circuit
 * when n > 30 since 2^31 overflows int and is already > 10^8.
 *
 * TIME COMPLEXITY:  O(1)
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup02Sol {

    public static boolean solve(int n, String complexity) {
        long ops;
        long limit = 100_000_000L;

        switch (complexity) {
            case "1":
                ops = 1;
                break;
            case "log_n":
                ops = Math.max(1, (long) (Math.log(n) / Math.log(2)));
                break;
            case "n":
                ops = n;
                break;
            case "n_log_n":
                ops = Math.max(n, (long) n * (long) Math.max(1, (int) (Math.log(n) / Math.log(2))));
                break;
            case "n^2":
                ops = (long) n * n;
                break;
            case "n^3":
                ops = (long) n * n * n;
                break;
            case "2^n":
                if (n > 30) return false;
                ops = 1L << n;
                break;
            default:
                ops = Long.MAX_VALUE;
        }

        return ops < limit;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        String complexity = parts[1];
        System.out.println(solve(n, complexity));
        sc.close();
    }
}
