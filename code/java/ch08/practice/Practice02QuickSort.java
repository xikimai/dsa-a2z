package ch08.practice;

import java.util.*;

/**
 * Practice 02: Quick Sort
 * ==============================
 * Chapter 8: The Art of Sorting
 *
 * PROBLEM: Implement quick sort. Given an array of integers,
 *          return a new array sorted in ascending order using
 *          the quick sort algorithm with Lomuto partition.
 *
 * ALGORITHM: Choose the last element as pivot, partition the array
 *            so all elements <= pivot are on the left and > pivot on
 *            the right, then recurse on both halves.
 *
 * EXAMPLES:
 *   solve([10, 7, 8, 9, 1, 5]) = [1, 5, 7, 8, 9, 10]
 *   solve([3, 2, 1])           = [1, 2, 3]
 *   solve([1, 2, 3])           = [1, 2, 3]
 *
 * CONSTRAINTS:
 *   0 <= arr.length <= 10^5
 *
 * TIME COMPLEXITY:  O(n log n) average, O(n^2) worst
 * SPACE COMPLEXITY: O(log n) stack space
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice02QuickSort {
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
