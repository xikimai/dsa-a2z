package ch03.practice;

import java.util.*;

/**
 * Warmup 04: Count Down
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given a positive integer n, return a list counting down from n to 1.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one positive integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the numbers from n down to 1, space-separated.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 1000
 *
 * EXAMPLES
 * --------
 * Input:  5
 * Output: 5 4 3 2 1
 *
 * Input:  1
 * Output: 1
 *
 * Input:  3
 * Output: 3 2 1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of the solve() method with your solution.
 * Return a List of integers from n down to 1.
 * Hint: Use a for loop that starts at n and counts down.
 * The main method handles input/output -- don't change it.
 */
public class Warmup04CountDown {

    /**
     * Return a list counting down from n to 1.
     *
     * @param n starting value (positive integer)
     * @return list [n, n-1, ..., 2, 1]
     */
    public static List<Integer> solve(int n) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<Integer> result = solve(n);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            if (i > 0) sb.append(" ");
            sb.append(result.get(i));
        }
        System.out.println(sb.toString());
        scanner.close();
    }
}
