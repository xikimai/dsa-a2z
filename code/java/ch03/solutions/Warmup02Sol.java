package ch03.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 02: Absolute Value
 * =======================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * If n is negative, negate it to make it positive. Otherwise, return as-is.
 * This is exactly what Math.abs() does internally, but the exercise is
 * about practicing if/else.
 *
 * TIME COMPLEXITY:  O(1) — one comparison and possibly one negation
 * SPACE COMPLEXITY: O(1) — no extra space
 */
public class Warmup02Sol {

    public static int solve(int n) {
        if (n < 0) {
            return -n;
        }
        return n;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(solve(n));
        scanner.close();
    }
}
