package ch06.practice;

import java.util.*;

/**
 * Warmup 03: Mystery Complexity
 * ==============================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM
 * -------
 * You ran a mystery function with several input sizes and recorded how
 * many operations it performed. Determine the time complexity by analyzing
 * the pattern in the data.
 *
 * Given arrays nValues and counts (same length), check how the count
 * grows relative to n:
 *   - If count stays roughly the same:            "O(1)"
 *   - If count roughly doubles when n doubles:    "O(n)"
 *   - If count roughly quadruples when n doubles: "O(n^2)"
 *   - Otherwise (grows but slower than linear):   "O(log n)"
 *
 * Strategy: look at ratios of consecutive counts vs ratios of consecutive n.
 *   ratio_n = nValues[i] / nValues[i-1]
 *   ratio_c = counts[i] / counts[i-1]
 *   If all ratio_c are ~1:              "O(1)"
 *   If ratio_c ~ ratio_n:              "O(n)"
 *   If ratio_c ~ ratio_n^2:            "O(n^2)"
 *   Otherwise:                          "O(log n)"
 *
 * INPUT FORMAT
 * ------------
 * Line 1: space-separated integers (nValues)
 * Line 2: space-separated integers (counts)
 *
 * OUTPUT FORMAT
 * -------------
 * Print the complexity string.
 *
 * CONSTRAINTS
 * -----------
 * 2 <= length <= 10
 * All values > 0
 *
 * EXAMPLES
 * --------
 * Input:                    Output:
 * 1 10 100 1000            O(1)
 * 5 5 5 5
 *
 * Input:                    Output:
 * 100 200 400 800          O(n)
 * 100 200 400 800
 *
 * Input:                    Output:
 * 10 20 40 80              O(n^2)
 * 100 400 1600 6400
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return \"\";" in solve() with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Warmup03MysteryComplexity {

    /**
     * Determine the time complexity from empirical data.
     *
     * @param nValues array of input sizes
     * @param counts  array of operation counts
     * @return complexity string like "O(1)", "O(log n)", "O(n)", or "O(n^2)"
     */
    public static String solve(int[] nValues, int[] counts) {
        // TODO: Replace this with your solution
        return "";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nValues = Arrays.stream(sc.nextLine().trim().split("\\s+"))
                              .mapToInt(Integer::parseInt).toArray();
        int[] counts = Arrays.stream(sc.nextLine().trim().split("\\s+"))
                             .mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(nValues, counts));
        sc.close();
    }
}
