package ch06.practice;

import java.util.*;

/**
 * Warmup 01: Count the Steps
 * ==============================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM
 * -------
 * Given a code pattern identifier and a value n, calculate how many
 * steps that code pattern would take to run.
 *
 * Code patterns:
 *   "single_loop"    -> n steps           (one loop from 1 to n)
 *   "double_loop"    -> n * n steps       (nested loops, each 1 to n)
 *   "half_loop"      -> n / 2 steps       (integer division)
 *   "dependent_loop" -> n*(n+1)/2 steps   (inner loop depends on outer)
 *   "log_loop"       -> floor(log2(n))    (halving each iteration, 0 if n < 2)
 *
 * INPUT FORMAT
 * ------------
 * Line 1: code_id (string)
 * Line 2: n (integer)
 *
 * OUTPUT FORMAT
 * -------------
 * Print the number of steps.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= n <= 10^6
 * code_id is one of the five patterns listed above.
 *
 * EXAMPLES
 * --------
 * Input:      Output:
 * single_loop   100
 * 100
 *
 * Input:      Output:
 * double_loop   100
 * 10
 *
 * Input:      Output:
 * log_loop      4
 * 16
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in solve() with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Warmup01CountSteps {

    /**
     * Count the number of steps for the given code pattern.
     *
     * @param codeId the pattern identifier
     * @param n      the input size
     * @return number of steps
     */
    public static int solve(String codeId, int n) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String codeId = sc.nextLine().trim();
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(codeId, n));
        sc.close();
    }
}
