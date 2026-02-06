package ch01.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 01: Sum of Two Numbers
 * ============================================
 * Chapter 1: The Coder's Toolkit
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Simply return a + b. No tricks needed for this one — the goal is to
 * practice the workflow: read input, compute, print output.
 *
 * TIME COMPLEXITY:  O(1) — just one addition
 * SPACE COMPLEXITY: O(1) — no extra memory used
 */
public class Warmup01Sol {

    /**
     * Return the sum of a and b.
     *
     * @param a the first integer
     * @param b the second integer
     * @return the sum of a and b
     */
    public static int solve(int a, int b) {
        return a + b;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        System.out.println(solve(a, b));
        scanner.close();
    }
}
