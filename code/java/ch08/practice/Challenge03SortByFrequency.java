package ch08.practice;

import java.util.*;

/**
 * Challenge 03: Sort By Frequency
 * ==============================
 * Chapter 8: The Art of Sorting
 *
 * PROBLEM: Given an array of integers, sort elements by decreasing
 *          frequency. If two elements have the same frequency, sort
 *          them by increasing value.
 *
 * EXAMPLES:
 *   solve([1, 1, 2, 2, 2, 3])    = [2, 2, 2, 1, 1, 3]
 *   solve([4, 4, 4, 5, 5, 6])    = [4, 4, 4, 5, 5, 6]
 *   solve([1, 2, 3])             = [1, 2, 3]
 *   solve([5])                   = [5]
 *   solve([3, 3, 1, 1, 2, 2])   = [1, 1, 2, 2, 3, 3]
 *
 * CONSTRAINTS:
 *   0 <= arr.length <= 10^5
 *
 * HINT: Build a frequency map, then sort with a custom comparator:
 *       primary key = -frequency (descending), secondary key = value (ascending).
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge03SortByFrequency {
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
