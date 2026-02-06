package ch02.practice;

import java.util.Scanner;

/**
 * Practice 02: Time Conversion
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given a total number of seconds, convert it to hours, minutes, and seconds.
 *   hours   = totalSeconds / 3600
 *   minutes = (totalSeconds % 3600) / 60
 *   seconds = totalSeconds % 60
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one integer: totalSeconds.
 *
 * OUTPUT FORMAT
 * -------------
 * Print three integers separated by colons: H:M:S
 *
 * CONSTRAINTS
 * -----------
 * 0 <= totalSeconds <= 10^6
 *
 * EXAMPLES
 * --------
 * Input:  3661
 * Output: 1:1:1
 *
 * Input:  0
 * Output: 0:0:0
 *
 * Input:  7200
 * Output: 2:0:0
 *
 * Input:  90
 * Output: 0:1:30
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of the solve() method with your solution.
 * Return an int array with three elements: {hours, minutes, seconds}.
 * The main method handles input/output — don't change it.
 */
public class Practice02TimeConversion {

    /**
     * Convert total seconds to hours, minutes, and seconds.
     *
     * @param totalSeconds the total number of seconds
     * @return an int array {hours, minutes, seconds}
     */
    public static int[] solve(int totalSeconds) {
        // TODO: Replace this with your solution
        return new int[]{0, 0, 0};
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
