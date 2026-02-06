package ch03.practice;

import java.util.*;

/**
 * Warmup 06: Multiplication Table
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given an integer n, return the multiplication table for n from 1 to 10.
 * Each entry should be a string in the format "i x n = result".
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print 10 lines, each in the format "i x n = result" for i = 1 to 10.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 1000
 *
 * EXAMPLES
 * --------
 * Input:  7
 * Output:
 *   1 x 7 = 7
 *   2 x 7 = 14
 *   3 x 7 = 21
 *   ...
 *   10 x 7 = 70
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of the solve() method with your solution.
 * Return a list of 10 strings in the format shown above.
 * Hint: Use a for loop from 1 to 10.
 * The main method handles input/output -- don't change it.
 */
public class Warmup06MultiplicationTable {

    /**
     * Return the multiplication table for n as a list of formatted strings.
     *
     * @param n the number to build the table for
     * @return list of 10 strings like "1 x 7 = 7", "2 x 7 = 14", ...
     */
    public static List<String> solve(int n) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<String> table = solve(n);
        for (String line : table) {
            System.out.println(line);
        }
        scanner.close();
    }
}
