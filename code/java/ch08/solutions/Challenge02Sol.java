package ch08.solutions;

import java.util.*;

/**
 * Solution for Challenge 02: Count Inversions
 * =========================================
 * Chapter 8: The Art of Sorting
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Modified merge sort: during the merge step, whenever we pick an element
 * from the right half (because it's smaller than the current left element),
 * that means ALL remaining elements in the left half form inversions with it.
 *
 * TIME COMPLEXITY:  O(n log n)
 * SPACE COMPLEXITY: O(n)
 */
public class Challenge02Sol {

    public static long solve(int[] arr) {
        if (arr.length <= 1) return 0L;
        int[] temp = arr.clone();
        return mergeSortCount(temp, 0, temp.length - 1);
    }

    private static long mergeSortCount(int[] arr, int lo, int hi) {
        if (lo >= hi) return 0L;
        int mid = lo + (hi - lo) / 2;
        long count = 0;
        count += mergeSortCount(arr, lo, mid);
        count += mergeSortCount(arr, mid + 1, hi);
        count += mergeCount(arr, lo, mid, hi);
        return count;
    }

    private static long mergeCount(int[] arr, int lo, int mid, int hi) {
        int[] left = Arrays.copyOfRange(arr, lo, mid + 1);
        int[] right = Arrays.copyOfRange(arr, mid + 1, hi + 1);
        int i = 0, j = 0, k = lo;
        long count = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                arr[k++] = left[i++];
            } else {
                // All remaining elements in left are > right[j]
                count += left.length - i;
                arr[k++] = right[j++];
            }
        }
        while (i < left.length) arr[k++] = left[i++];
        while (j < right.length) arr[k++] = right[j++];
        return count;
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
