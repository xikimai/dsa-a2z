package ch02.practice;

import java.util.Scanner;

/**
 * Practice 01: Circle Properties
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given the radius of a circle, compute its area and circumference.
 *   area = Math.PI * radius * radius
 *   circumference = 2 * Math.PI * radius
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one double: the radius.
 *
 * OUTPUT FORMAT
 * -------------
 * Print two doubles on separate lines — the area, then the circumference.
 *
 * CONSTRAINTS
 * -----------
 * 0 < radius <= 10^6
 *
 * EXAMPLES
 * --------
 * Input:  1.0
 * Output: 3.141592653589793
 *         6.283185307179586
 *
 * Input:  5.0
 * Output: 78.53981633974483
 *         31.41592653589793
 *
 * Input:  0.5
 * Output: 0.7853981633974483
 *         3.141592653589793
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of the solve() method with your solution.
 * Return a double array with two elements: {area, circumference}.
 * The main method handles input/output — don't change it.
 */
public class Practice01Circle {

    /**
     * Compute the area and circumference of a circle.
     *
     * @param radius the radius of the circle
     * @return a double array {area, circumference}
     */
    public static double[] solve(double radius) {
        // TODO: Replace this with your solution
        return new double[]{0.0, 0.0};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double radius = scanner.nextDouble();
        double[] result = solve(radius);
        System.out.println(result[0]);
        System.out.println(result[1]);
        scanner.close();
    }
}
