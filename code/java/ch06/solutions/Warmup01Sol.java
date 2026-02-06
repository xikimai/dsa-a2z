package ch06.solutions;

import java.util.*;

/**
 * Solution for Warmup 01: Count the Steps
 * =========================================
 * Chapter 6: How Fast Is Your Code?
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Simple switch/if-else on the code_id string. Each pattern maps to a
 * well-known formula for the number of operations.
 *
 * TIME COMPLEXITY:  O(1)
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup01Sol {

    public static int solve(String codeId, int n) {
        switch (codeId) {
            case "single_loop":    return n;
            case "double_loop":    return n * n;
            case "half_loop":      return n / 2;
            case "dependent_loop": return n * (n + 1) / 2;
            case "log_loop":
                if (n < 2) return 0;
                return (int) (Math.log(n) / Math.log(2));
            default:
                return 0;
        }
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String codeId = sc.nextLine().trim();
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(codeId, n));
        sc.close();
    }
}
