package ch08.solutions;

import java.util.*;

/**
 * Solution for Practice 02: Quick Sort
 * =========================================
 * Chapter 8: The Art of Sorting
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Lomuto partition scheme: use the last element as pivot. Partition
 * the array so elements <= pivot come before it, elements > pivot
 * come after. Recurse on both halves.
 *
 * TIME COMPLEXITY:  O(n log n) average, O(n^2) worst
 * SPACE COMPLEXITY: O(log n) stack space
 */
public class Practice02Sol {

    public static int[] solve(int[] arr) {
        int[] a = arr.clone();
        if (a.length > 1) quickSort(a, 0, a.length - 1);
        return a;
    }

    private static void quickSort(int[] arr, int lo, int hi) {
        if (lo < hi) {
            int pivotIdx = partition(arr, lo, hi);
            quickSort(arr, lo, pivotIdx - 1);
            quickSort(arr, pivotIdx + 1, hi);
        }
    }

    private static int partition(int[] arr, int lo, int hi) {
        int pivot = arr[hi];
        int i = lo - 1;
        for (int j = lo; j < hi; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[hi];
        arr[hi] = temp;
        return i + 1;
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
