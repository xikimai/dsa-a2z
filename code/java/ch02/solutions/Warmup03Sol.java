package ch02.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 03: Celsius to Fahrenheit
 * ===============================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Apply the conversion formula: F = C * 9.0 / 5.0 + 32.0
 * Important: Use 9.0 and 5.0 (not 9 and 5) to avoid integer division.
 * If you wrote 9/5 instead of 9.0/5.0, you'd get 1 instead of 1.8!
 *
 * TIME COMPLEXITY:  O(1) — just arithmetic
 * SPACE COMPLEXITY: O(1) — no extra memory used
 */
public class Warmup03Sol {

    /**
     * Convert Celsius to Fahrenheit.
     *
     * @param celsius the temperature in Celsius
     * @return the temperature in Fahrenheit
     */
    public static double solve(double celsius) {
        return celsius * 9.0 / 5.0 + 32.0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double celsius = scanner.nextDouble();
        System.out.println(solve(celsius));
        scanner.close();
    }
}
