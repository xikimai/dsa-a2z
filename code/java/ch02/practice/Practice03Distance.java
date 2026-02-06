package ch02.practice;

import java.util.Scanner;

/**
 * Practice 03: Distance Between Two Points
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given two points (x1, y1) and (x2, y2) on a 2D plane, compute the
 * Euclidean distance between them.
 *   distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
 *
 * INPUT FORMAT
 * ------------
 * A single line containing four space-separated doubles: x1 y1 x2 y2
 *
 * OUTPUT FORMAT
 * -------------
 * Print a single double — the Euclidean distance.
 *
 * CONSTRAINTS
 * -----------
 * -10^6 <= x1, y1, x2, y2 <= 10^6
 *
 * EXAMPLES
 * --------
 * Input:  0.0 0.0 3.0 4.0
 * Output: 5.0
 *
 * Input:  1.0 1.0 1.0 1.0
 * Output: 0.0
 *
 * Input:  -1.0 -1.0 2.0 3.0
 * Output: 5.0
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0.0;" in the solve() method with your solution.
 * Hint: Use Math.sqrt() and Math.pow().
 * The main method handles input/output — don't change it.
 */
public class Practice03Distance {

    /**
     * Compute the Euclidean distance between two points.
     *
     * @param x1 x-coordinate of the first point
     * @param y1 y-coordinate of the first point
     * @param x2 x-coordinate of the second point
     * @param y2 y-coordinate of the second point
     * @return the Euclidean distance
     */
    public static double solve(double x1, double y1, double x2, double y2) {
        // TODO: Replace this with your solution
        return 0.0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double x1 = scanner.nextDouble();
        double y1 = scanner.nextDouble();
        double x2 = scanner.nextDouble();
        double y2 = scanner.nextDouble();
        System.out.println(solve(x1, y1, x2, y2));
        scanner.close();
    }
}
