package ch02.solutions;

import java.util.Scanner;

/**
 * Solution for Practice 01: Circle Properties
 * ==============================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use the built-in Math.PI constant for precision:
 *   area          = Math.PI * radius * radius
 *   circumference = 2 * Math.PI * radius
 *
 * Math.PI gives you 3.141592653589793, which is more precise than typing
 * 3.14 yourself. Always use the constant when you can!
 *
 * TIME COMPLEXITY:  O(1) — just arithmetic
 * SPACE COMPLEXITY: O(1) — a two-element array
 */
public class Practice01Sol {

    /**
     * Compute the area and circumference of a circle.
     *
     * @param radius the radius of the circle
     * @return a double array {area, circumference}
     */
    public static double[] solve(double radius) {
        double area = Math.PI * radius * radius;
        double circumference = 2 * Math.PI * radius;
        return new double[]{area, circumference};
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
