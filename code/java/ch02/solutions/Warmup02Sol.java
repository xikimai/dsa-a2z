package ch02.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 02: Rectangle Area
 * ========================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Multiply length by width. That's it — the formula for a rectangle's area.
 *
 * TIME COMPLEXITY:  O(1) — just one multiplication
 * SPACE COMPLEXITY: O(1) — no extra memory used
 */
public class Warmup02Sol {

    /**
     * Return the area of a rectangle.
     *
     * @param length the length of the rectangle
     * @param width  the width of the rectangle
     * @return the area (length * width)
     */
    public static int solve(int length, int width) {
        return length * width;
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
