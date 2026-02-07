package ch09.practice;

import java.util.*;

/**
 * Challenge 01: Find Peak Element
 * ==============================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * PROBLEM: A peak element is strictly greater than its neighbors.
 *          Boundary elements only need to beat their one neighbor.
 *          (Treat out-of-bounds as -infinity.)
 *          Return ANY valid peak index.
 *
 * ALGORITHM: Implement THREE methods:
 *   - solveLinear: O(n) scan
 *   - solveBinary: O(log n) binary search
 *   - solve: calls solveBinary (default)
 *
 * EXAMPLES:
 *   solve(new int[]{1,2,3,1})       = 2  (arr[2]=3 is a peak)
 *   solve(new int[]{1,2,1,3,5,6,4}) = 1 or 5  (multiple valid peaks)
 *   solve(new int[]{1})             = 0
 *
 * CONSTRAINTS: 1 <= arr.length <= 10^5
 *              arr[i] != arr[i+1] for all valid i
 *
 * INSTRUCTIONS: Replace the bodies of all three methods.
 */
public class Challenge01FindPeak {
    public static int solveLinear(int[] arr) {
        // TODO: Replace this with your O(n) solution
        return 0;
    }

    public static int solveBinary(int[] arr) {
        // TODO: Replace this with your O(log n) solution
        return 0;
    }

    public static int solve(int[] arr) {
        return solveBinary(arr);
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] arr;
        if (line.isEmpty()) {
            arr = new int[0];
        } else {
            String[] parts = line.split("\\s+");
            arr = new int[parts.length];
            for (int i = 0; i < parts.length; i++) arr[i] = Integer.parseInt(parts[i]);
        }
        System.out.println(solve(arr));
        sc.close();
    }
}
