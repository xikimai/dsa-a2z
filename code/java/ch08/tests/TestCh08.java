package ch08.tests;

import java.util.*;

/**
 * Tests for Chapter 8: The Art of Sorting — Putting Things in Order
 *
 * Build and run:
 *   cd code/java
 *   javac ch08/tests/TestCh08.java
 *   java -ea ch08.tests.TestCh08
 */
public class TestCh08 {

    // ── Helper methods ───────────────────────────────────────────────

    static void assertEquals(Object expected, Object actual, String msg) {
        assert Objects.equals(expected, actual)
            : msg + " — expected " + expected + ", got " + actual;
    }

    static void assertArrayEquals(int[] expected, int[] actual, String msg) {
        assert Arrays.equals(expected, actual)
            : msg + " — expected " + Arrays.toString(expected)
              + ", got " + Arrays.toString(actual);
    }

    static void assertBoolEquals(boolean expected, boolean actual, String msg) {
        assert expected == actual
            : msg + " — expected " + expected + ", got " + actual;
    }

    static void assertStringArrayEquals(String[] expected, String[] actual, String msg) {
        assert Arrays.equals(expected, actual)
            : msg + " — expected " + Arrays.toString(expected)
              + ", got " + Arrays.toString(actual);
    }

    // ── Reference solutions ─────────────────────────────────────────

    // W1: Selection Sort
    static int[] solveSelectionSort(int[] arr) {
        int[] a = arr.clone();
        for (int i = 0; i < a.length; i++) {
            int minIdx = i;
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < a[minIdx]) minIdx = j;
            }
            int temp = a[i]; a[i] = a[minIdx]; a[minIdx] = temp;
        }
        return a;
    }

    // W2: Bubble Sort
    static int[] solveBubbleSort(int[] arr) {
        int[] a = arr.clone();
        int n = a.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - 1 - i; j++) {
                if (a[j] > a[j + 1]) {
                    int temp = a[j]; a[j] = a[j + 1]; a[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
        return a;
    }

    // W3: Insertion Sort
    static int[] solveInsertionSort(int[] arr) {
        int[] a = arr.clone();
        for (int i = 1; i < a.length; i++) {
            int key = a[i];
            int j = i - 1;
            while (j >= 0 && a[j] > key) { a[j + 1] = a[j]; j--; }
            a[j + 1] = key;
        }
        return a;
    }

    // W4: Check If Sorted
    static boolean solveCheckIfSorted(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) return false;
        }
        return true;
    }

    // W5: Sort By Absolute
    static int[] solveSortByAbsolute(int[] arr) {
        Integer[] boxed = new Integer[arr.length];
        for (int i = 0; i < arr.length; i++) boxed[i] = arr[i];
        Arrays.sort(boxed, Comparator.comparingInt(Math::abs));
        int[] result = new int[arr.length];
        for (int i = 0; i < arr.length; i++) result[i] = boxed[i];
        return result;
    }

    // P1: Merge Sort
    static int[] solveMergeSort(int[] arr) {
        if (arr.length <= 1) return arr.clone();
        int mid = arr.length / 2;
        int[] left = solveMergeSort(Arrays.copyOfRange(arr, 0, mid));
        int[] right = solveMergeSort(Arrays.copyOfRange(arr, mid, arr.length));
        return mergeHelper(left, right);
    }

    static int[] mergeHelper(int[] left, int[] right) {
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

    // P2: Quick Sort
    static int[] solveQuickSort(int[] arr) {
        int[] a = arr.clone();
        if (a.length > 1) qsHelper(a, 0, a.length - 1);
        return a;
    }

    static void qsHelper(int[] arr, int lo, int hi) {
        if (lo < hi) {
            int pivot = arr[hi], i = lo - 1;
            for (int j = lo; j < hi; j++) {
                if (arr[j] <= pivot) {
                    i++;
                    int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
                }
            }
            int temp = arr[i + 1]; arr[i + 1] = arr[hi]; arr[hi] = temp;
            int pi = i + 1;
            qsHelper(arr, lo, pi - 1);
            qsHelper(arr, pi + 1, hi);
        }
    }

    // P3: Dutch National Flag
    static int[] solveDutchFlag(int[] arr) {
        int[] a = arr.clone();
        int lo = 0, mid = 0, hi = a.length - 1;
        while (mid <= hi) {
            if (a[mid] == 0) {
                int temp = a[lo]; a[lo] = a[mid]; a[mid] = temp;
                lo++; mid++;
            } else if (a[mid] == 1) {
                mid++;
            } else {
                int temp = a[mid]; a[mid] = a[hi]; a[hi] = temp;
                hi--;
            }
        }
        return a;
    }

    // P4: Custom Comparator
    static String[] solveCustomComparator(String[] words) {
        String[] result = words.clone();
        Arrays.sort(result, Comparator.comparingInt(String::length)
                                      .thenComparing(Comparator.naturalOrder()));
        return result;
    }

    // P5: Merge Two Sorted
    static int[] solveMergeTwoSorted(int[] arr1, int[] arr2) {
        int[] result = new int[arr1.length + arr2.length];
        int i = 0, j = 0, k = 0;
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] <= arr2[j]) result[k++] = arr1[i++];
            else result[k++] = arr2[j++];
        }
        while (i < arr1.length) result[k++] = arr1[i++];
        while (j < arr2.length) result[k++] = arr2[j++];
        return result;
    }

    // C1: Sort Three Ways — Bubble
    static int[] solveStwBubble(int[] arr) {
        int[] a = arr.clone();
        int n = a.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - 1 - i; j++) {
                if (a[j] > a[j + 1]) {
                    int temp = a[j]; a[j] = a[j + 1]; a[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
        return a;
    }

    // C1: Sort Three Ways — Merge
    static int[] solveStwMerge(int[] arr) {
        return solveMergeSort(arr);
    }

    // C1: Sort Three Ways — Builtin
    static int[] solveStwBuiltin(int[] arr) {
        int[] a = arr.clone();
        Arrays.sort(a);
        return a;
    }

    // C2: Count Inversions
    static long solveCountInversions(int[] arr) {
        if (arr.length <= 1) return 0L;
        int[] temp = arr.clone();
        return mergeSortCount(temp, 0, temp.length - 1);
    }

    static long mergeSortCount(int[] arr, int lo, int hi) {
        if (lo >= hi) return 0L;
        int mid = lo + (hi - lo) / 2;
        long count = 0;
        count += mergeSortCount(arr, lo, mid);
        count += mergeSortCount(arr, mid + 1, hi);
        count += mergeCount(arr, lo, mid, hi);
        return count;
    }

    static long mergeCount(int[] arr, int lo, int mid, int hi) {
        int[] left = Arrays.copyOfRange(arr, lo, mid + 1);
        int[] right = Arrays.copyOfRange(arr, mid + 1, hi + 1);
        int i = 0, j = 0, k = lo;
        long count = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                arr[k++] = left[i++];
            } else {
                count += left.length - i;
                arr[k++] = right[j++];
            }
        }
        while (i < left.length) arr[k++] = left[i++];
        while (j < right.length) arr[k++] = right[j++];
        return count;
    }

    // C3: Sort By Frequency
    static int[] solveSortByFrequency(int[] arr) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int v : arr) freq.merge(v, 1, Integer::sum);
        Integer[] boxed = new Integer[arr.length];
        for (int i = 0; i < arr.length; i++) boxed[i] = arr[i];
        Arrays.sort(boxed, (a, b) -> {
            int fa = freq.get(a), fb = freq.get(b);
            if (fa != fb) return fb - fa;
            return a - b;
        });
        int[] result = new int[arr.length];
        for (int i = 0; i < arr.length; i++) result[i] = boxed[i];
        return result;
    }

    // ── Warmup 01: Selection Sort ──────────────────────────────────

    static void testSelectionSort() {
        System.out.println("=== Warmup 01: Selection Sort ===");
        assertArrayEquals(new int[]{11,12,22,25,64},
            solveSelectionSort(new int[]{64,25,12,22,11}), "selection basic");
        System.out.println("  test_selection_basic............. PASS");

        assertArrayEquals(new int[]{1,2,3,4,5},
            solveSelectionSort(new int[]{1,2,3,4,5}), "selection already sorted");
        System.out.println("  test_selection_sorted............ PASS");

        assertArrayEquals(new int[]{1,2,3,4,5},
            solveSelectionSort(new int[]{5,4,3,2,1}), "selection reverse");
        System.out.println("  test_selection_reverse........... PASS");

        assertArrayEquals(new int[]{1},
            solveSelectionSort(new int[]{1}), "selection single");
        System.out.println("  test_selection_single............ PASS");

        assertArrayEquals(new int[]{1,1,2,3,3},
            solveSelectionSort(new int[]{3,3,1,1,2}), "selection duplicates");
        System.out.println("  test_selection_duplicates........ PASS");
        System.out.println();
    }

    // ── Warmup 02: Bubble Sort ─────────────────────────────────────

    static void testBubbleSort() {
        System.out.println("=== Warmup 02: Bubble Sort ===");
        assertArrayEquals(new int[]{11,12,22,25,34,64,90},
            solveBubbleSort(new int[]{64,34,25,12,22,11,90}), "bubble basic");
        System.out.println("  test_bubble_basic................ PASS");

        assertArrayEquals(new int[]{1,2,3,4},
            solveBubbleSort(new int[]{1,2,3,4}), "bubble already sorted");
        System.out.println("  test_bubble_sorted............... PASS");

        assertArrayEquals(new int[]{1,2},
            solveBubbleSort(new int[]{2,1}), "bubble pair");
        System.out.println("  test_bubble_pair................. PASS");

        assertArrayEquals(new int[]{},
            solveBubbleSort(new int[]{}), "bubble empty");
        System.out.println("  test_bubble_empty................ PASS");

        assertArrayEquals(new int[]{5,5,5},
            solveBubbleSort(new int[]{5,5,5}), "bubble all same");
        System.out.println("  test_bubble_all_same............. PASS");
        System.out.println();
    }

    // ── Warmup 03: Insertion Sort ──────────────────────────────────

    static void testInsertionSort() {
        System.out.println("=== Warmup 03: Insertion Sort ===");
        assertArrayEquals(new int[]{5,6,11,12,13},
            solveInsertionSort(new int[]{12,11,13,5,6}), "insertion basic");
        System.out.println("  test_insertion_basic............. PASS");

        assertArrayEquals(new int[]{1,2,3},
            solveInsertionSort(new int[]{1,2,3}), "insertion already sorted");
        System.out.println("  test_insertion_sorted............ PASS");

        assertArrayEquals(new int[]{1,2,3},
            solveInsertionSort(new int[]{3,2,1}), "insertion reverse");
        System.out.println("  test_insertion_reverse........... PASS");

        assertArrayEquals(new int[]{7},
            solveInsertionSort(new int[]{7}), "insertion single");
        System.out.println("  test_insertion_single............ PASS");

        assertArrayEquals(new int[]{1,2,2,4,4},
            solveInsertionSort(new int[]{4,2,4,1,2}), "insertion duplicates");
        System.out.println("  test_insertion_duplicates........ PASS");
        System.out.println();
    }

    // ── Warmup 04: Check If Sorted ─────────────────────────────────

    static void testCheckIfSorted() {
        System.out.println("=== Warmup 04: Check If Sorted ===");
        assertBoolEquals(true,
            solveCheckIfSorted(new int[]{1,2,3,4,5}), "sorted ascending");
        System.out.println("  test_sorted_ascending............ PASS");

        assertBoolEquals(false,
            solveCheckIfSorted(new int[]{1,3,2,4,5}), "sorted disorder");
        System.out.println("  test_sorted_disorder............. PASS");

        assertBoolEquals(true,
            solveCheckIfSorted(new int[]{}), "sorted empty");
        System.out.println("  test_sorted_empty................ PASS");

        assertBoolEquals(true,
            solveCheckIfSorted(new int[]{7}), "sorted single");
        System.out.println("  test_sorted_single............... PASS");

        assertBoolEquals(true,
            solveCheckIfSorted(new int[]{1,1,1}), "sorted equal");
        System.out.println("  test_sorted_equal................ PASS");
        System.out.println();
    }

    // ── Warmup 05: Sort By Absolute ────────────────────────────────

    static void testSortByAbsolute() {
        System.out.println("=== Warmup 05: Sort By Absolute ===");
        assertArrayEquals(new int[]{-1,2,3,4,-5},
            solveSortByAbsolute(new int[]{3,-1,2,-5,4}), "abs basic");
        System.out.println("  test_abs_basic................... PASS");

        assertArrayEquals(new int[]{1,-3,7,-10},
            solveSortByAbsolute(new int[]{-10,7,-3,1}), "abs mixed");
        System.out.println("  test_abs_mixed................... PASS");

        assertArrayEquals(new int[]{0,-1,3,-5,8},
            solveSortByAbsolute(new int[]{0,-5,3,-1,8}), "abs with zero");
        System.out.println("  test_abs_with_zero............... PASS");

        assertArrayEquals(new int[]{1,2,3},
            solveSortByAbsolute(new int[]{1,2,3}), "abs positive only");
        System.out.println("  test_abs_positive................ PASS");

        assertArrayEquals(new int[]{-1},
            solveSortByAbsolute(new int[]{-1}), "abs single neg");
        System.out.println("  test_abs_single_neg.............. PASS");
        System.out.println();
    }

    // ── Practice 01: Merge Sort ────────────────────────────────────

    static void testMergeSort() {
        System.out.println("=== Practice 01: Merge Sort ===");
        assertArrayEquals(new int[]{3,9,10,27,38,43,82},
            solveMergeSort(new int[]{38,27,43,3,9,82,10}), "merge basic");
        System.out.println("  test_merge_basic................. PASS");

        assertArrayEquals(new int[]{1,2,3,4,5},
            solveMergeSort(new int[]{5,4,3,2,1}), "merge reverse");
        System.out.println("  test_merge_reverse............... PASS");

        assertArrayEquals(new int[]{1},
            solveMergeSort(new int[]{1}), "merge single");
        System.out.println("  test_merge_single................ PASS");

        assertArrayEquals(new int[]{},
            solveMergeSort(new int[]{}), "merge empty");
        System.out.println("  test_merge_empty................. PASS");

        assertArrayEquals(new int[]{1,1,2,2,2},
            solveMergeSort(new int[]{2,1,2,1,2}), "merge duplicates");
        System.out.println("  test_merge_duplicates............ PASS");
        System.out.println();
    }

    // ── Practice 02: Quick Sort ────────────────────────────────────

    static void testQuickSort() {
        System.out.println("=== Practice 02: Quick Sort ===");
        assertArrayEquals(new int[]{1,5,7,8,9,10},
            solveQuickSort(new int[]{10,7,8,9,1,5}), "quick basic");
        System.out.println("  test_quick_basic................. PASS");

        assertArrayEquals(new int[]{1,2,3},
            solveQuickSort(new int[]{3,2,1}), "quick reverse");
        System.out.println("  test_quick_reverse............... PASS");

        assertArrayEquals(new int[]{1,2,3},
            solveQuickSort(new int[]{1,2,3}), "quick sorted");
        System.out.println("  test_quick_sorted................ PASS");

        assertArrayEquals(new int[]{},
            solveQuickSort(new int[]{}), "quick empty");
        System.out.println("  test_quick_empty................. PASS");

        assertArrayEquals(new int[]{4,4,4,4},
            solveQuickSort(new int[]{4,4,4,4}), "quick all same");
        System.out.println("  test_quick_all_same.............. PASS");
        System.out.println();
    }

    // ── Practice 03: Dutch National Flag ───────────────────────────

    static void testDutchNationalFlag() {
        System.out.println("=== Practice 03: Dutch National Flag ===");
        assertArrayEquals(new int[]{0,0,1,1,2,2},
            solveDutchFlag(new int[]{2,0,2,1,1,0}), "dnf basic");
        System.out.println("  test_dnf_basic................... PASS");

        assertArrayEquals(new int[]{0},
            solveDutchFlag(new int[]{0}), "dnf single");
        System.out.println("  test_dnf_single.................. PASS");

        assertArrayEquals(new int[]{0,1,2},
            solveDutchFlag(new int[]{2,1,0}), "dnf reverse");
        System.out.println("  test_dnf_reverse................. PASS");

        assertArrayEquals(new int[]{0,0,0},
            solveDutchFlag(new int[]{0,0,0}), "dnf all zeros");
        System.out.println("  test_dnf_all_zeros............... PASS");

        assertArrayEquals(new int[]{0,0,1,1,1,2,2},
            solveDutchFlag(new int[]{1,0,2,1,0,2,1}), "dnf mixed");
        System.out.println("  test_dnf_mixed................... PASS");
        System.out.println();
    }

    // ── Practice 04: Custom Comparator ─────────────────────────────

    static void testCustomComparator() {
        System.out.println("=== Practice 04: Custom Comparator ===");
        assertStringArrayEquals(
            new String[]{"fig","kiwi","apple","banana","cherry"},
            solveCustomComparator(new String[]{"banana","apple","kiwi","cherry","fig"}),
            "comparator fruits");
        System.out.println("  test_comparator_fruits........... PASS");

        assertStringArrayEquals(
            new String[]{"ant","bat","cat"},
            solveCustomComparator(new String[]{"cat","bat","ant"}),
            "comparator same length");
        System.out.println("  test_comparator_same_length...... PASS");

        assertStringArrayEquals(
            new String[]{"a","bb","dd","ccc"},
            solveCustomComparator(new String[]{"a","bb","ccc","dd"}),
            "comparator mixed lengths");
        System.out.println("  test_comparator_mixed............ PASS");

        assertStringArrayEquals(
            new String[]{"hello"},
            solveCustomComparator(new String[]{"hello"}),
            "comparator single");
        System.out.println("  test_comparator_single........... PASS");

        assertStringArrayEquals(
            new String[]{},
            solveCustomComparator(new String[]{}),
            "comparator empty");
        System.out.println("  test_comparator_empty............ PASS");
        System.out.println();
    }

    // ── Practice 05: Merge Two Sorted ──────────────────────────────

    static void testMergeTwoSorted() {
        System.out.println("=== Practice 05: Merge Two Sorted ===");
        assertArrayEquals(new int[]{1,2,3,4,5,6},
            solveMergeTwoSorted(new int[]{1,3,5}, new int[]{2,4,6}), "merge two interleaved");
        System.out.println("  test_merge_two_interleaved....... PASS");

        assertArrayEquals(new int[]{1,2,3,4,5,6},
            solveMergeTwoSorted(new int[]{1,2,3}, new int[]{4,5,6}), "merge two sequential");
        System.out.println("  test_merge_two_sequential........ PASS");

        assertArrayEquals(new int[]{1,2,3},
            solveMergeTwoSorted(new int[]{}, new int[]{1,2,3}), "merge two one empty");
        System.out.println("  test_merge_two_one_empty......... PASS");

        assertArrayEquals(new int[]{},
            solveMergeTwoSorted(new int[]{}, new int[]{}), "merge two both empty");
        System.out.println("  test_merge_two_both_empty........ PASS");

        assertArrayEquals(new int[]{1,1,1,1,1},
            solveMergeTwoSorted(new int[]{1,1,1}, new int[]{1,1}), "merge two all same");
        System.out.println("  test_merge_two_all_same.......... PASS");
        System.out.println();
    }

    // ── Challenge 01: Sort Three Ways ──────────────────────────────

    static void testSortThreeWays() {
        System.out.println("=== Challenge 01: Sort Three Ways ===");

        int[] input1 = {5,3,8,1,2};
        int[] expected1 = {1,2,3,5,8};
        assertArrayEquals(expected1, solveStwBubble(input1), "stw bubble basic");
        assertArrayEquals(expected1, solveStwMerge(input1), "stw merge basic");
        assertArrayEquals(expected1, solveStwBuiltin(input1), "stw builtin basic");
        assertArrayEquals(expected1, solveStwMerge(input1), "stw solve basic");
        System.out.println("  test_stw_basic................... PASS");

        int[] input2 = {1};
        int[] expected2 = {1};
        assertArrayEquals(expected2, solveStwBubble(input2), "stw bubble single");
        assertArrayEquals(expected2, solveStwMerge(input2), "stw merge single");
        assertArrayEquals(expected2, solveStwBuiltin(input2), "stw builtin single");
        assertArrayEquals(expected2, solveStwMerge(input2), "stw solve single");
        System.out.println("  test_stw_single.................. PASS");

        int[] input3 = {3,1,2,3,1};
        int[] expected3 = {1,1,2,3,3};
        assertArrayEquals(expected3, solveStwBubble(input3), "stw bubble dups");
        assertArrayEquals(expected3, solveStwMerge(input3), "stw merge dups");
        assertArrayEquals(expected3, solveStwBuiltin(input3), "stw builtin dups");
        assertArrayEquals(expected3, solveStwMerge(input3), "stw solve dups");
        System.out.println("  test_stw_duplicates.............. PASS");

        int[] input4 = {};
        int[] expected4 = {};
        assertArrayEquals(expected4, solveStwBubble(input4), "stw bubble empty");
        assertArrayEquals(expected4, solveStwMerge(input4), "stw merge empty");
        assertArrayEquals(expected4, solveStwBuiltin(input4), "stw builtin empty");
        assertArrayEquals(expected4, solveStwMerge(input4), "stw solve empty");
        System.out.println("  test_stw_empty................... PASS");

        int[] input5 = {10,9,8,7,6,5,4,3,2,1};
        int[] expected5 = {1,2,3,4,5,6,7,8,9,10};
        assertArrayEquals(expected5, solveStwBubble(input5), "stw bubble large");
        assertArrayEquals(expected5, solveStwMerge(input5), "stw merge large");
        assertArrayEquals(expected5, solveStwBuiltin(input5), "stw builtin large");
        assertArrayEquals(expected5, solveStwMerge(input5), "stw solve large");
        System.out.println("  test_stw_large_reverse........... PASS");
        System.out.println();
    }

    // ── Challenge 02: Count Inversions ─────────────────────────────

    static void testCountInversions() {
        System.out.println("=== Challenge 02: Count Inversions ===");
        assertEquals(3L, solveCountInversions(new int[]{2,4,1,3,5}), "inversions mixed");
        System.out.println("  test_inversions_mixed............ PASS");

        assertEquals(0L, solveCountInversions(new int[]{1,2,3,4,5}), "inversions sorted");
        System.out.println("  test_inversions_sorted........... PASS");

        assertEquals(10L, solveCountInversions(new int[]{5,4,3,2,1}), "inversions reverse");
        System.out.println("  test_inversions_reverse.......... PASS");

        assertEquals(0L, solveCountInversions(new int[]{1}), "inversions single");
        System.out.println("  test_inversions_single........... PASS");

        assertEquals(0L, solveCountInversions(new int[]{}), "inversions empty");
        System.out.println("  test_inversions_empty............ PASS");

        assertEquals(0L, solveCountInversions(new int[]{1,1,1}), "inversions all same");
        System.out.println("  test_inversions_all_same......... PASS");
        System.out.println();
    }

    // ── Challenge 03: Sort By Frequency ────────────────────────────

    static void testSortByFrequency() {
        System.out.println("=== Challenge 03: Sort By Frequency ===");
        assertArrayEquals(new int[]{2,2,2,1,1,3},
            solveSortByFrequency(new int[]{1,1,2,2,2,3}), "freq basic");
        System.out.println("  test_freq_basic.................. PASS");

        assertArrayEquals(new int[]{4,4,4,5,5,6},
            solveSortByFrequency(new int[]{4,4,4,5,5,6}), "freq already ordered");
        System.out.println("  test_freq_ordered................ PASS");

        assertArrayEquals(new int[]{1,2,3},
            solveSortByFrequency(new int[]{1,2,3}), "freq all unique");
        System.out.println("  test_freq_unique................. PASS");

        assertArrayEquals(new int[]{5},
            solveSortByFrequency(new int[]{5}), "freq single");
        System.out.println("  test_freq_single................. PASS");

        assertArrayEquals(new int[]{1,1,2,2,3,3},
            solveSortByFrequency(new int[]{3,3,1,1,2,2}), "freq tie by value");
        System.out.println("  test_freq_tie.................... PASS");
        System.out.println();
    }

    // ── Runner ───────────────────────────────────────────────────────

    public static void main(String[] args) {

        System.out.println("Testing Chapter 8...\n");

        System.out.println("--- Warmup Problems ---");
        testSelectionSort();
        testBubbleSort();
        testInsertionSort();
        testCheckIfSorted();
        testSortByAbsolute();

        System.out.println("--- Practice Problems ---");
        testMergeSort();
        testQuickSort();
        testDutchNationalFlag();
        testCustomComparator();
        testMergeTwoSorted();

        System.out.println("--- Challenge Problems ---");
        testSortThreeWays();
        testCountInversions();
        testSortByFrequency();

        System.out.println("All tests passed!");
    }
}
