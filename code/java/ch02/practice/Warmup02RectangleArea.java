package ch02.practice;

import java.util.Scanner;

/**
 * Warmup 02: Rectangle Area
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given the length and width of a rectangle, compute its area.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing two space-separated integers: length and width.
 *
 * OUTPUT FORMAT
 * -------------
 * Print a single integer — the area of the rectangle.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= length, width <= 10^4
 *
 * EXAMPLES
 * --------
 * Input:  5 3
 * Output: 15
 *
 * Input:  10 10
 * Output: 100
 *
 * Input:  1 1
 * Output: 1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in the solve() method with your solution.
 * The main method handles input/output — don't change it.
 */
public class Warmup02RectangleArea {

    /**
     * Return the area of a rectangle.
     *
     * @param length the length of the rectangle
     * @param width  the width of the rectangle
     * @return the area (length * width)
     */
    public static int solve(int length, int width) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int length = scanner.nextInt();
        int width = scanner.nextInt();
        System.out.println(solve(length, width));
        scanner.close();
    }
}
