package ch08.practice;

import java.util.*;

/**
 * Challenge 02: Count Inversions
 * ==============================
 * Chapter 8: The Art of Sorting
 *
 * PROBLEM: Given an array, count the number of inversions.
 *          An inversion is a pair (i, j) where i < j but arr[i] > arr[j].
 *          The inversion count measures how "far" an array is from sorted.
 *
 * EXAMPLES:
 *   solve([2, 4, 1, 3, 5]) = 3   (inversions: (2,1), (4,1), (4,3))
 *   solve([1, 2, 3, 4, 5]) = 0   (already sorted)
 *   solve([5, 4, 3, 2, 1]) = 10  (reverse sorted = max inversions)
 *   solve([1])              = 0
 *   solve([])               = 0
 *
 * CONSTRAINTS:
 *   0 <= arr.length <= 10^5
 *   Use long for the count (can be up to n*(n-1)/2)
 *
 * HINT: Modify merge sort to count inversions during the merge step.
 *       A brute-force O(n^2) approach works but is too slow for large n.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge02CountInversions {
    public static long solve(int[] arr) {
        // TODO: Replace this with your solution
        return 0L;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println(solve(new int[0]));
        } else {
            String[] parts = line.split("\\s+");
            int[] arr = new int[parts.length];
            for (int i = 0; i < parts.length; i++) arr[i] = Integer.parseInt(parts[i]);
            System.out.println(solve(arr));
        }
        sc.close();
    }
}
