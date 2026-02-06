package ch02.solutions;

import java.util.Scanner;

/**
 * Solution for Practice 02: Time Conversion
 * ============================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use integer division and modulo to break total seconds into h:m:s.
 *   hours   = totalSeconds / 3600       (how many full hours?)
 *   minutes = (totalSeconds % 3600) / 60 (leftover seconds -> how many full minutes?)
 *   seconds = totalSeconds % 60          (final leftover seconds)
 *
 * The key insight: % 3600 removes the hours portion, then / 60 extracts minutes.
 *
 * TIME COMPLEXITY:  O(1) — just arithmetic
 * SPACE COMPLEXITY: O(1) — a three-element array
 */
public class Practice02Sol {

    /**
     * Convert total seconds to hours, minutes, and seconds.
     *
     * @param totalSeconds the total number of seconds
     * @return an int array {hours, minutes, seconds}
     */
    public static int[] solve(int totalSeconds) {
        int hours = totalSeconds / 3600;
        int minutes = (totalSeconds % 3600) / 60;
        int seconds = totalSeconds % 60;
        return new int[]{hours, minutes, seconds};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalSeconds = scanner.nextInt();
        int[] result = solve(totalSeconds);
        System.out.println(result[0] + ":" + result[1] + ":" + result[2]);
        scanner.close();
    }
}
