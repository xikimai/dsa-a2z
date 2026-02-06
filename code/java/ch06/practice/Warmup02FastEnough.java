package ch06.practice;

import java.util.*;

/**
 * Warmup 02: Is It Fast Enough?
 * ==============================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM
 * -------
 * Given an input size n and a complexity class, determine whether
 * the algorithm would finish within the typical 1-second time limit
 * (approximately 10^8 operations).
 *
 * Complexity classes and their operation counts:
 *   "1"       -> 1
 *   "log_n"   -> floor(log2(n)), min 1
 *   "n"       -> n
 *   "n_log_n" -> n * floor(log2(n)), min n
 *   "n^2"     -> n * n
 *   "n^3"     -> n * n * n
 *   "2^n"     -> 2^n  (if n > 30, automatically too slow)
 *
 * Return true if ops < 100,000,000 (strictly less than 10^8).
 *
 * INPUT FORMAT
 * ------------
 * A single line: "n complexity"
 *
 * OUTPUT FORMAT
 * -------------
 * Print true or false.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 10^9
 *
 * EXAMPLES
 * --------
 * Input:  1000 n^2      Output: true     (1,000,000 < 10^8)
 * Input:  100000 n^2    Output: false    (10^10 >= 10^8)
 * Input:  20 2^n        Output: true     (1,048,576 < 10^8)
 * Input:  30 2^n        Output: false    (1,073,741,824 >= 10^8)
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return false;" in solve() with your solution.
 * Use long for operations to avoid integer overflow!
 * The main method handles input/output -- don't change it.
 */
public class Warmup02FastEnough {

    /**
     * Determine if the algorithm is fast enough for input size n.
     *
     * @param n          the input size
     * @param complexity the complexity class string
     * @return true if the number of operations is less than 10^8
     */
    public static boolean solve(int n, String complexity) {
        // TODO: Replace this with your solution
        return false;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        String complexity = parts[1];
        System.out.println(solve(n, complexity));
        sc.close();
    }
}
