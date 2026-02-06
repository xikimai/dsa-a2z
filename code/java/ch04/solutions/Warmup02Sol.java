package ch04.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 02: Power
 * ==============================
 * Chapter 4: Functions
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Multiply base by itself exponent times using a loop.
 * Start with result = 1 and multiply by base each iteration.
 *
 * TIME COMPLEXITY:  O(exponent)
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup02Sol {

    public static long solve(int base, int exponent) {
        long result = 1;
        for (int i = 0; i < exponent; i++) {
            result *= base;
        }
        return result;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int base = sc.nextInt();
        int exponent = sc.nextInt();
        System.out.println(solve(base, exponent));
        sc.close();
    }
}
