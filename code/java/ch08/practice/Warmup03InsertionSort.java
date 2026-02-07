package ch08.practice;

import java.util.*;

/**
 * Warmup 03: Insertion Sort
 * ==============================
 * Chapter 8: The Art of Sorting
 *
 * PROBLEM: Implement insertion sort. Given an array of integers,
 *          return a new array sorted in ascending order using the
 *          insertion sort algorithm.
 *
 * ALGORITHM: For each element starting from index 1, insert it into
 *            its correct position among the already-sorted elements
 *            to its left.
 *
 * EXAMPLES:
 *   solve([12, 11, 13, 5, 6]) = [5, 6, 11, 12, 13]
 *   solve([1, 2, 3])          = [1, 2, 3]
 *   solve([3, 2, 1])          = [1, 2, 3]
 *
 * CONSTRAINTS:
 *   0 <= arr.length <= 10^4
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup03InsertionSort {
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
