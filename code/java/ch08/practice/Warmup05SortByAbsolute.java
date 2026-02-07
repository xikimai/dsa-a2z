package ch08.practice;

import java.util.*;

/**
 * Warmup 05: Sort By Absolute Value
 * ==============================
 * Chapter 8: The Art of Sorting
 *
 * PROBLEM: Given an array of integers, return a new array sorted by
 *          absolute value in ascending order. If two elements have the
 *          same absolute value, the one that appeared first in the
 *          original array should come first (stable sort).
 *
 * EXAMPLES:
 *   solve([3, -1, 2, -5, 4])  = [-1, 2, 3, 4, -5]
 *   solve([-10, 7, -3, 1])    = [1, -3, 7, -10]
 *   solve([0, -5, 3, -1, 8])  = [0, -1, 3, -5, 8]
 *
 * CONSTRAINTS:
 *   0 <= arr.length <= 10^4
 *
 * HINT: Use Integer[] with Arrays.sort and a Comparator.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup05SortByAbsolute {
    public static int[] solve(int[] arr) {
        // TODO: Replace this with your solution
        return new int[0];
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println();
        } else {
            String[] parts = line.split("\\s+");
            int[] arr = new int[parts.length];
            for (int i = 0; i < parts.length; i++) arr[i] = Integer.parseInt(parts[i]);
            int[] result = solve(arr);
            StringJoiner sj = new StringJoiner(" ");
            for (int v : result) sj.add(String.valueOf(v));
            System.out.println(sj);
        }
        sc.close();
    }
}
