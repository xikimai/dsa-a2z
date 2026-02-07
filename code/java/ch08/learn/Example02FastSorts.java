package ch08.learn;

import java.util.*;

/**
 * Example 02: Fast Sorts — Merge Sort and Quick Sort
 * ====================================================
 * Chapter 8: The Art of Sorting
 *
 * This file demonstrates two O(n log n) divide-and-conquer sorting
 * algorithms with step-by-step visuals and a timing comparison against
 * the basic O(n^2) sorts.
 *
 * Build and run:
 *   cd code/java
 *   javac ch08/learn/Example02FastSorts.java
 *   java ch08.learn.Example02FastSorts
 */
public class Example02FastSorts {

    // ── Helper: print array ─────────────────────────────────────────
    static void printArray(int[] arr, String label) {
        StringBuilder sb = new StringBuilder("  " + label + "[");
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) sb.append(", ");
            sb.append(arr[i]);
        }
        sb.append("]");
        System.out.println(sb);
    }

    // ── 1. Merge Sort ───────────────────────────────────────────────
    // Split the array in half, sort each half, merge them back.

    static int[] mergeSort(int[] arr) {
        if (arr.length <= 1) return arr.clone();
        int mid = arr.length / 2;
        int[] left = mergeSort(Arrays.copyOfRange(arr, 0, mid));
        int[] right = mergeSort(Arrays.copyOfRange(arr, mid, arr.length));
        return merge(left, right);
    }

    static int[] merge(int[] left, int[] right) {
        int[] result = new int[left.length + right.length];
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) result[k++] = left[i++];
            else result[k++] = right[j++];
        }
        while (i < left.length) result[k++] = left[i++];
        while (j < right.length) result[k++] = right[j++];
        return result;
    }

    static void demoMergeSort() {
        System.out.println("=== Part 1: Merge Sort ===");
        System.out.println("Idea: Split in half, sort each half, merge the sorted halves.\n");

        int[] arr = {38, 27, 43, 3, 9, 82, 10};
        printArray(arr, "Start:    ");
        System.out.println();

        // Show the split/merge visually
        System.out.println("  Splitting:");
        System.out.println("    [38, 27, 43, 3, 9, 82, 10]");
        System.out.println("    [38, 27, 43]          [3, 9, 82, 10]");
        System.out.println("    [38] [27, 43]         [3, 9] [82, 10]");
        System.out.println("    [38] [27] [43]        [3] [9] [82] [10]");
        System.out.println();
        System.out.println("  Merging back:");
        System.out.println("    [38] [27] -> [27, 38]     [3] [9] -> [3, 9]");
        System.out.println("    [27, 38] [43] -> [27, 38, 43]");
        System.out.println("    [82] [10] -> [10, 82]");
        System.out.println("    [3, 9] [10, 82] -> [3, 9, 10, 82]");
        System.out.println("    [27, 38, 43] [3, 9, 10, 82] -> [3, 9, 10, 27, 38, 43, 82]");
        System.out.println();

        int[] sorted = mergeSort(arr);
        printArray(sorted, "Result:   ");
        System.out.println("\n  Time: O(n log n) always | Space: O(n) | Stable\n");
    }

    // ── 2. Quick Sort ───────────────────────────────────────────────
    // Pick a pivot, partition into < pivot and > pivot, recurse.

    static void quickSort(int[] arr, int lo, int hi) {
        if (lo < hi) {
            int pivotIdx = partition(arr, lo, hi);
            quickSort(arr, lo, pivotIdx - 1);
            quickSort(arr, pivotIdx + 1, hi);
        }
    }

    static int partition(int[] arr, int lo, int hi) {
        int pivot = arr[hi]; // Lomuto: pivot is last element
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

    static int[] quickSortCopy(int[] arr) {
        int[] a = arr.clone();
        if (a.length > 1) quickSort(a, 0, a.length - 1);
        return a;
    }

    static void demoQuickSort() {
        System.out.println("=== Part 2: Quick Sort ===");
        System.out.println("Idea: Pick a pivot, move smaller elements left, larger right, recurse.\n");

        int[] arr = {10, 7, 8, 9, 1, 5};
        printArray(arr, "Start:    ");
        System.out.println();

        // Show one partition step
        System.out.println("  First partition (pivot = 5, last element):");
        System.out.println("    Scan: 10>5 skip, 7>5 skip, 8>5 skip, 9>5 skip, 1<=5 swap");
        System.out.println("    After partition: [1, 5, 8, 9, 10, 7]  (pivot 5 at index 1)");
        System.out.println("    Left of pivot: [1]  Right of pivot: [8, 9, 10, 7]");
        System.out.println("    Recurse on both halves...\n");

        int[] sorted = quickSortCopy(arr);
        printArray(sorted, "Result:   ");
        System.out.println("\n  Time: O(n log n) avg, O(n^2) worst | Space: O(log n) | NOT stable\n");
    }

    // ── 3. Timing Comparison ────────────────────────────────────────

    static int[] insertionSort(int[] arr) {
        int[] a = arr.clone();
        for (int i = 1; i < a.length; i++) {
            int key = a[i];
            int j = i - 1;
            while (j >= 0 && a[j] > key) {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = key;
        }
        return a;
    }

    static void demoTiming() {
        System.out.println("=== Part 3: Timing Comparison ===\n");

        int[] sizes = {1000, 5000, 10000, 20000};
        Random rng = new Random(42);

        System.out.printf("  %-8s  %12s  %12s  %12s  %12s%n",
            "Size", "Insertion", "Merge Sort", "Quick Sort", "Arrays.sort");
        System.out.println("  " + "-".repeat(62));

        for (int size : sizes) {
            int[] data = new int[size];
            for (int i = 0; i < size; i++) data[i] = rng.nextInt(size * 10);

            // Insertion sort
            long start = System.nanoTime();
            insertionSort(data);
            long insertTime = System.nanoTime() - start;

            // Merge sort
            start = System.nanoTime();
            mergeSort(data);
            long mergeTime = System.nanoTime() - start;

            // Quick sort
            start = System.nanoTime();
            quickSortCopy(data);
            long quickTime = System.nanoTime() - start;

            // Arrays.sort (built-in)
            start = System.nanoTime();
            int[] copy = data.clone();
            Arrays.sort(copy);
            long builtinTime = System.nanoTime() - start;

            System.out.printf("  %-8d  %,12d  %,12d  %,12d  %,12d  (ns)%n",
                size, insertTime, mergeTime, quickTime, builtinTime);
        }

        System.out.println("\n  Notice: Merge/Quick/Built-in scale WAY better than Insertion!");
        System.out.println("  That's the power of O(n log n) vs O(n^2).\n");
    }

    // ── Main ────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 8: Fast Sorts — Merge Sort and Quick Sort");
        System.out.println("==================================================\n");

        demoMergeSort();
        demoQuickSort();
        demoTiming();

        System.out.println("KEY TAKEAWAYS:");
        System.out.println("  1. Merge sort: always O(n log n), stable, but uses O(n) extra space");
        System.out.println("  2. Quick sort: O(n log n) average, in-place, but O(n^2) worst case");
        System.out.println("  3. Java's Arrays.sort uses dual-pivot quicksort for primitives");
        System.out.println("     and TimSort (merge sort variant) for objects");
        System.out.println("  4. For contests, just use Arrays.sort() — but know HOW it works!");
    }
}
