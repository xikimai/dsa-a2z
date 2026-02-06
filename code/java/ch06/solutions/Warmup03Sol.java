package ch06.solutions;

import java.util.*;

/**
 * Solution for Warmup 03: Mystery Complexity
 * ============================================
 * Chapter 6: How Fast Is Your Code?
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Compare ratios of consecutive count values to ratios of consecutive
 * n values. If counts don't change -> O(1). If counts grow linearly
 * with n -> O(n). If counts grow quadratically -> O(n^2). Otherwise
 * -> O(log n).
 *
 * TIME COMPLEXITY:  O(k) where k is the length of the arrays
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup03Sol {

    public static String solve(int[] nValues, int[] counts) {
        boolean allConstant = true;
        boolean allLinear = true;
        boolean allQuadratic = true;

        for (int i = 1; i < nValues.length; i++) {
            double ratioN = (double) nValues[i] / nValues[i - 1];
            double ratioC = (double) counts[i] / counts[i - 1];

            if (Math.abs(ratioC - 1.0) > 0.3) {
                allConstant = false;
            }
            if (Math.abs(ratioC - ratioN) > ratioN * 0.3) {
                allLinear = false;
            }
            if (Math.abs(ratioC - ratioN * ratioN) > ratioN * ratioN * 0.3) {
                allQuadratic = false;
            }
        }

        if (allConstant) return "O(1)";
        if (allLinear) return "O(n)";
        if (allQuadratic) return "O(n^2)";
        return "O(log n)";
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
