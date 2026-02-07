package ch09.solutions;

import java.util.*;

/**
 * Solution for Challenge 01: Find Peak Element
 * =========================================
 * Chapter 9: Finding Needles — The Power of Searching
 *
 * APPROACH: Three methods provided.
 *   - solveLinear: O(n) scan checking each element against neighbors.
 *   - solveBinary: O(log n) — if arr[mid] < arr[mid+1], the peak is
 *     to the right; otherwise it's at mid or to the left.
 *   - solve: delegates to solveBinary.
 *
 * TIME COMPLEXITY:  O(log n) for solveBinary, O(n) for solveLinear
 * SPACE COMPLEXITY: O(1)
 */
public class Challenge01Sol {

    public static int solveLinear(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            boolean leftOk = (i == 0) || (arr[i] > arr[i - 1]);
            boolean rightOk = (i == n - 1) || (arr[i] > arr[i + 1]);
            if (leftOk && rightOk) return i;
        }
        return 0;  // should never reach here if input is valid
    }

    public static int solveBinary(int[] arr) {
        int lo = 0, hi = arr.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] < arr[mid + 1]) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
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
