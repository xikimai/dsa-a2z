package ch08.practice;

import java.util.*;

/**
 * Practice 05: Merge Two Sorted Arrays
 * ==============================
 * Chapter 8: The Art of Sorting
 *
 * PROBLEM: Given two sorted arrays, merge them into one sorted array.
 *          Use the two-pointer technique (do NOT just concatenate and sort).
 *
 * EXAMPLES:
 *   solve([1,3,5], [2,4,6])   = [1,2,3,4,5,6]
 *   solve([1,2,3], [4,5,6])   = [1,2,3,4,5,6]
 *   solve([], [1,2,3])        = [1,2,3]
 *   solve([], [])             = []
 *   solve([1,1,1], [1,1])     = [1,1,1,1,1]
 *
 * CONSTRAINTS:
 *   0 <= arr1.length, arr2.length <= 10^5
 *   Both arrays are sorted in non-decreasing order
 *
 * TIME COMPLEXITY:  O(n + m)
 * SPACE COMPLEXITY: O(n + m)
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice05MergeTwoSorted {
    public static int[] solve(int[] arr1, int[] arr2) {
        // TODO: Replace this with your solution
        return new int[0];
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line1 = sc.nextLine().trim();
        String line2 = sc.nextLine().trim();
        int[] arr1 = line1.isEmpty() ? new int[0] : Arrays.stream(line1.split("\\s+")).mapToInt(Integer::parseInt).toArray();
        int[] arr2 = line2.isEmpty() ? new int[0] : Arrays.stream(line2.split("\\s+")).mapToInt(Integer::parseInt).toArray();
        int[] result = solve(arr1, arr2);
        StringJoiner sj = new StringJoiner(" ");
        for (int v : result) sj.add(String.valueOf(v));
        System.out.println(sj);
        sc.close();
    }
}
