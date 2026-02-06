package ch02.solutions;

import java.util.Scanner;

/**
 * Solution for Challenge 02: Quadratic Discriminant
 * ====================================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * For ax^2 + bx + c = 0:
 *   discriminant = b^2 - 4ac
 *
 * The discriminant tells you how many real roots exist:
 *   disc > 0  -> 2 distinct real roots
 *   disc == 0 -> 1 repeated real root (the parabola just touches the x-axis)
 *   disc < 0  -> 0 real roots (the parabola doesn't cross the x-axis)
 *
 * This is a preview of how math connects to programming — you'll see
 * this formula again when we study more advanced algorithms!
 *
 * TIME COMPLEXITY:  O(1) — just arithmetic
 * SPACE COMPLEXITY: O(1) — a two-element array
 */
public class Challenge02Sol {

    /**
     * Compute the discriminant and number of real roots.
     *
     * @param a coefficient of x^2
     * @param b coefficient of x
     * @param c constant term
     * @return a double array {discriminant, numRoots}
     */
    public static double[] solve(double a, double b, double c) {
        double disc = b * b - 4 * a * c;
        double numRoots;
        if (disc > 0) {
            numRoots = 2.0;
        } else if (disc == 0) {
            numRoots = 1.0;
        } else {
            numRoots = 0.0;
        }
        return new double[]{disc, numRoots};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();
        double[] result = solve(a, b, c);
        System.out.println(result[0] + " " + result[1]);
        scanner.close();
    }
}
