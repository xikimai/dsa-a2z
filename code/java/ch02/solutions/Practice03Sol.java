package ch02.solutions;

import java.util.Scanner;

/**
 * Solution for Practice 03: Distance Between Two Points
 * =======================================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Apply the Euclidean distance formula:
 *   distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
 *
 * We use Math.pow(value, 2) to square each difference, then Math.sqrt()
 * for the square root. You could also write (dx * dx) instead of
 * Math.pow(dx, 2) — both work fine.
 *
 * TIME COMPLEXITY:  O(1) — just arithmetic and a square root
 * SPACE COMPLEXITY: O(1) — no extra memory used
 */
public class Practice03Sol {

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
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
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
