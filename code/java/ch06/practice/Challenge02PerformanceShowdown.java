package ch06.practice;

import java.util.*;

/**
 * Challenge 02: Performance Showdown
 * ====================================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM
 * -------
 * Two algorithms A and B have known complexity classes. Given an input
 * size n, determine which algorithm would be faster (fewer operations).
 *
 * Complexity classes and operation counts:
 *   "1"       -> 1
 *   "log_n"   -> floor(log2(n)), min 1
 *   "n"       -> n
 *   "n_log_n" -> n * floor(log2(n)), min n
 *   "n^2"     -> n * n
 *   "n^3"     -> n * n * n
 *   "2^n"     -> 2^n (cap: if n > 30, treat as Long.MAX_VALUE)
 *
 * Return "A" if A is faster, "B" if B is faster, "TIE" if equal.
 * "Faster" means fewer operations.
 *
 * INPUT FORMAT
 * ------------
 * A single line: "complexityA complexityB n"
 *
 * OUTPUT FORMAT
 * -------------
 * Print A, B, or TIE.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 10^6
 *
 * EXAMPLES
 * --------
 * Input:  n^2 n_log_n 1000    Output: B
 * Input:  n n 100              Output: TIE
 * Input:  1 log_n 1000000      Output: A
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return \"\";" in solve() with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Challenge02PerformanceShowdown {

    /**
     * Determine which algorithm is faster for input size n.
     *
     * @param complexityA complexity class of algorithm A
     * @param complexityB complexity class of algorithm B
     * @param n           the input size
     * @return "A", "B", or "TIE"
     */
    public static String solve(String complexityA, String complexityB, int n) {
        // TODO: Replace this with your solution
        return "";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split("\\s+");
        String complexityA = parts[0];
        String complexityB = parts[1];
        int n = Integer.parseInt(parts[2]);
        System.out.println(solve(complexityA, complexityB, n));
        sc.close();
    }
}
