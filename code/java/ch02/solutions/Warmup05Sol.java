package ch02.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 05: Last Digit
 * ====================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use Math.abs(n) to handle negative numbers, then use % 10 to get
 * the last digit. For example: Math.abs(-567) gives 567, and 567 % 10 gives 7.
 *
 * Why Math.abs? In Java, -567 % 10 gives -7 (not 7), because Java's modulo
 * preserves the sign of the dividend. We want the digit itself (always positive).
 *
 * TIME COMPLEXITY:  O(1) — just one abs and one modulo
 * SPACE COMPLEXITY: O(1) — no extra memory used
 */
public class Warmup05Sol {

    /**
     * Return the last digit of n (always non-negative).
     *
     * @param n the input integer
     * @return the last digit of n
     */
    public static int solve(int n) {
        return Math.abs(n) % 10;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(solve(n));
        scanner.close();
    }
}
