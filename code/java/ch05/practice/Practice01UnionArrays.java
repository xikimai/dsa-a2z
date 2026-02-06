package ch05.practice;

import java.util.*;

/**
 * Practice 01: Union of Two Arrays
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given two arrays of integers, return a sorted array containing
 * the union of both arrays (all unique elements from both).
 *
 * INPUT FORMAT
 * ------------
 * Two lines, each containing space-separated integers.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the sorted union as space-separated integers.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= a.length, b.length <= 10^5
 *
 * EXAMPLES
 * --------
 * Input:
 * 1 2 3
 * 3 4 5
 * Output: 1 2 3 4 5
 *
 * Input:
 * 1 1 2
 * 2 3 3
 * Output: 1 2 3
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return new int[0];" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Practice01UnionArrays {

    /**
     * Return a sorted array containing the union of a and b.
     *
     * @param a first array
     * @param b second array
     * @return sorted array of unique elements from both
     */
    public static int[] solve(int[] a, int[] b) {
        // TODO: Replace this with your solution
        return new int[0];
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line1 = sc.nextLine().trim();
        String line2 = sc.nextLine().trim();
        int[] a = line1.isEmpty() ? new int[0]
            : Arrays.stream(line1.split("\\s+")).mapToInt(Integer::parseInt).toArray();
        int[] b = line2.isEmpty() ? new int[0]
            : Arrays.stream(line2.split("\\s+")).mapToInt(Integer::parseInt).toArray();
        int[] result = solve(a, b);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(" ");
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
