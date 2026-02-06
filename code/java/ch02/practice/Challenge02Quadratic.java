package ch02.practice;

import java.util.Scanner;

/**
 * Challenge 02: Quadratic Discriminant
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given the coefficients a, b, c of a quadratic equation ax^2 + bx + c = 0,
 * compute the discriminant and determine how many real roots the equation has.
 *   discriminant = b * b - 4 * a * c
 *   numRoots = 2 if discriminant > 0
 *            = 1 if discriminant == 0
 *            = 0 if discriminant < 0
 *
 * INPUT FORMAT
 * ------------
 * A single line containing three space-separated doubles: a b c
 *
 * OUTPUT FORMAT
 * -------------
 * Print two space-separated values: the discriminant and the number of real roots.
 *
 * CONSTRAINTS
 * -----------
 * -10^3 <= a, b, c <= 10^3
 * a != 0
 *
 * EXAMPLES
 * --------
 * Input:  1.0 -3.0 2.0
 * Output: 1.0 2.0
 *
 * Input:  1.0 2.0 1.0
 * Output: 0.0 1.0
 *
 * Input:  1.0 1.0 1.0
 * Output: -3.0 0.0
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of the solve() method with your solution.
 * Return a double array with two elements: {discriminant, numRoots}.
 * The main method handles input/output — don't change it.
 */
public class Challenge02Quadratic {

    /**
     * Compute the discriminant and number of real roots.
     *
     * @param a coefficient of x^2
     * @param b coefficient of x
     * @param c constant term
     * @return a double array {discriminant, numRoots}
     */
    public static double[] solve(double a, double b, double c) {
        // TODO: Replace this with your solution
        return new double[]{0.0, 0.0};
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
