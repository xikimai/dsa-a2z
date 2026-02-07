package ch09.tests;

import java.util.*;

/**
 * Tests for Chapter 9: Finding Needles — The Power of Searching
 *
 * Build and run:
 *   cd code/java
 *   javac ch09/tests/TestCh09.java
 *   java -ea ch09.tests.TestCh09
 */
public class TestCh09 {

    // ── Helper methods ───────────────────────────────────────────────

    static void assertEquals(int expected, int actual, String msg) {
        assert expected == actual
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

    static boolean isPeak(int[] arr, int idx) {
        if (idx < 0 || idx >= arr.length) return false;
        boolean leftOk = (idx == 0) || (arr[idx] > arr[idx - 1]);
        boolean rightOk = (idx == arr.length - 1) || (arr[idx] > arr[idx + 1]);
        return leftOk && rightOk;
    }

    // ── Reference solutions ─────────────────────────────────────────

    // W1: Linear Search
    static int solveLinearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) return i;
        }
        return -1;
    }

    // W2: Binary Search
    static int solveBinarySearch(int[] arr, int target) {
        int lo = 0, hi = arr.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }

    // W3: First Occurrence
    static int solveFirstOccurrence(int[] arr, int target) {
        int lo = 0, hi = arr.length - 1, result = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) { result = mid; hi = mid - 1; }
            else if (arr[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return result;
    }

    // W4: Last Occurrence
    static int solveLastOccurrence(int[] arr, int target) {
        int lo = 0, hi = arr.length - 1, result = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) { result = mid; lo = mid + 1; }
            else if (arr[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return result;
    }

    // W5: Count Occurrences
    static int solveCountOccurrences(int[] arr, int target) {
        int first = solveFirstOccurrence(arr, target);
        if (first == -1) return 0;
        int last = solveLastOccurrence(arr, target);
        return last - first + 1;
    }

    // P1: Lower Bound
    static int solveLowerBound(int[] arr, int target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] >= target) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    // P2: Upper Bound
    static int solveUpperBound(int[] arr, int target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] > target) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    // P3: Floor and Ceil
    static int[] solveFloorAndCeil(int[] arr, int target) {
        int n = arr.length;
        int lo = 0, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] >= target) hi = mid;
            else lo = mid + 1;
        }
        int lb = lo;
        int ceil = (lb < n) ? arr[lb] : -1;
        int floor;
        if (lb < n && arr[lb] == target) {
            floor = target;
        } else if (lb > 0) {
            floor = arr[lb - 1];
        } else {
            floor = -1;
        }
        return new int[]{floor, ceil};
    }

    // P4: Search in Rotated Array
    static int solveSearchRotated(int[] arr, int target) {
        int lo = 0, hi = arr.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) return mid;
            if (arr[lo] <= arr[mid]) {
                if (arr[lo] <= target && target < arr[mid]) hi = mid - 1;
                else lo = mid + 1;
            } else {
                if (arr[mid] < target && target <= arr[hi]) lo = mid + 1;
                else hi = mid - 1;
            }
        }
        return -1;
    }

    // P5: Find Min in Rotated
    static int solveMinInRotated(int[] arr) {
        int lo = 0, hi = arr.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] > arr[hi]) lo = mid + 1;
            else hi = mid;
        }
        return arr[lo];
    }

    // C1: Find Peak — Linear
    static int solvePeakLinear(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            boolean leftOk = (i == 0) || (arr[i] > arr[i - 1]);
            boolean rightOk = (i == n - 1) || (arr[i] > arr[i + 1]);
            if (leftOk && rightOk) return i;
        }
        return 0;
    }

    // C1: Find Peak — Binary
    static int solvePeakBinary(int[] arr) {
        int lo = 0, hi = arr.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] < arr[mid + 1]) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    // C2: Single Element
    static int solveSingleElement(int[] arr) {
        int lo = 0, hi = arr.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (mid % 2 == 1) mid--;
            if (arr[mid] == arr[mid + 1]) lo = mid + 2;
            else hi = mid;
        }
        return arr[lo];
    }

    // C3: Search Rotated II (with duplicates)
    static boolean solveRotatedSearchII(int[] arr, int target) {
        int lo = 0, hi = arr.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) return true;
            if (arr[lo] == arr[mid] && arr[mid] == arr[hi]) {
                lo++; hi--;
            } else if (arr[lo] <= arr[mid]) {
                if (arr[lo] <= target && target < arr[mid]) hi = mid - 1;
                else lo = mid + 1;
            } else {
                if (arr[mid] < target && target <= arr[hi]) lo = mid + 1;
                else hi = mid - 1;
            }
        }
        return false;
    }

    // ── Warmup 01: Linear Search ─────────────────────────────────────

    static void testLinearSearch() {
        System.out.println("=== Warmup 01: Linear Search ===");
        assertEquals(2, solveLinearSearch(new int[]{1,3,5,7,9}, 5), "linear found");
        System.out.println("  test_linear_found................ PASS");

        assertEquals(-1, solveLinearSearch(new int[]{1,3,5,7,9}, 4), "linear not found");
        System.out.println("  test_linear_not_found............ PASS");

        assertEquals(0, solveLinearSearch(new int[]{2,2,2,2}, 2), "linear first dup");
        System.out.println("  test_linear_first_dup............ PASS");

        assertEquals(-1, solveLinearSearch(new int[]{}, 1), "linear empty");
        System.out.println("  test_linear_empty................ PASS");

        assertEquals(0, solveLinearSearch(new int[]{7}, 7), "linear single");
        System.out.println("  test_linear_single............... PASS");
        System.out.println();
    }

    // ── Warmup 02: Binary Search ─────────────────────────────────────

    static void testBinarySearch() {
        System.out.println("=== Warmup 02: Binary Search ===");
        assertEquals(3, solveBinarySearch(new int[]{1,3,5,7,9,11}, 7), "bs found mid");
        System.out.println("  test_bs_found_mid................ PASS");

        assertEquals(-1, solveBinarySearch(new int[]{1,3,5,7,9,11}, 4), "bs not found");
        System.out.println("  test_bs_not_found................ PASS");

        assertEquals(0, solveBinarySearch(new int[]{2,4,6,8,10}, 2), "bs found first");
        System.out.println("  test_bs_found_first.............. PASS");

        assertEquals(4, solveBinarySearch(new int[]{2,4,6,8,10}, 10), "bs found last");
        System.out.println("  test_bs_found_last............... PASS");

        assertEquals(-1, solveBinarySearch(new int[]{}, 5), "bs empty");
        System.out.println("  test_bs_empty.................... PASS");

        assertEquals(0, solveBinarySearch(new int[]{1}, 1), "bs single");
        System.out.println("  test_bs_single................... PASS");
        System.out.println();
    }

    // ── Warmup 03: First Occurrence ──────────────────────────────────

    static void testFirstOccurrence() {
        System.out.println("=== Warmup 03: First Occurrence ===");
        assertEquals(1, solveFirstOccurrence(new int[]{1,2,2,2,3,4}, 2), "first middle");
        System.out.println("  test_first_middle................ PASS");

        assertEquals(0, solveFirstOccurrence(new int[]{1,1,1,1,1}, 1), "first all same");
        System.out.println("  test_first_all_same.............. PASS");

        assertEquals(2, solveFirstOccurrence(new int[]{1,3,5,7}, 5), "first unique");
        System.out.println("  test_first_unique................ PASS");

        assertEquals(-1, solveFirstOccurrence(new int[]{1,3,5,7}, 4), "first not found");
        System.out.println("  test_first_not_found............. PASS");

        assertEquals(-1, solveFirstOccurrence(new int[]{}, 1), "first empty");
        System.out.println("  test_first_empty................. PASS");
        System.out.println();
    }

    // ── Warmup 04: Last Occurrence ───────────────────────────────────

    static void testLastOccurrence() {
        System.out.println("=== Warmup 04: Last Occurrence ===");
        assertEquals(3, solveLastOccurrence(new int[]{1,2,2,2,3,4}, 2), "last middle");
        System.out.println("  test_last_middle................. PASS");

        assertEquals(4, solveLastOccurrence(new int[]{1,1,1,1,1}, 1), "last all same");
        System.out.println("  test_last_all_same............... PASS");

        assertEquals(2, solveLastOccurrence(new int[]{1,3,5,7}, 5), "last unique");
        System.out.println("  test_last_unique................. PASS");

        assertEquals(-1, solveLastOccurrence(new int[]{1,3,5,7}, 4), "last not found");
        System.out.println("  test_last_not_found.............. PASS");

        assertEquals(-1, solveLastOccurrence(new int[]{}, 1), "last empty");
        System.out.println("  test_last_empty.................. PASS");
        System.out.println();
    }

    // ── Warmup 05: Count Occurrences ─────────────────────────────────

    static void testCountOccurrences() {
        System.out.println("=== Warmup 05: Count Occurrences ===");
        assertEquals(3, solveCountOccurrences(new int[]{1,2,2,2,3,4}, 2), "count three");
        System.out.println("  test_count_three................. PASS");

        assertEquals(5, solveCountOccurrences(new int[]{1,1,1,1,1}, 1), "count all");
        System.out.println("  test_count_all................... PASS");

        assertEquals(1, solveCountOccurrences(new int[]{1,3,5,7}, 5), "count one");
        System.out.println("  test_count_one................... PASS");

        assertEquals(0, solveCountOccurrences(new int[]{1,3,5,7}, 4), "count zero");
        System.out.println("  test_count_zero.................. PASS");

        assertEquals(0, solveCountOccurrences(new int[]{}, 1), "count empty");
        System.out.println("  test_count_empty................. PASS");
        System.out.println();
    }

    // ── Practice 01: Lower Bound ─────────────────────────────────────

    static void testLowerBound() {
        System.out.println("=== Practice 01: Lower Bound ===");
        assertEquals(2, solveLowerBound(new int[]{1,3,5,7,9}, 5), "lb exact");
        System.out.println("  test_lb_exact.................... PASS");

        assertEquals(2, solveLowerBound(new int[]{1,3,5,7,9}, 4), "lb between");
        System.out.println("  test_lb_between.................. PASS");

        assertEquals(0, solveLowerBound(new int[]{1,3,5,7,9}, 1), "lb first");
        System.out.println("  test_lb_first.................... PASS");

        assertEquals(5, solveLowerBound(new int[]{1,3,5,7,9}, 10), "lb beyond");
        System.out.println("  test_lb_beyond................... PASS");

        assertEquals(0, solveLowerBound(new int[]{2,2,2,2}, 2), "lb all same");
        System.out.println("  test_lb_all_same................. PASS");

        assertEquals(0, solveLowerBound(new int[]{}, 5), "lb empty");
        System.out.println("  test_lb_empty.................... PASS");
        System.out.println();
    }

    // ── Practice 02: Upper Bound ─────────────────────────────────────

    static void testUpperBound() {
        System.out.println("=== Practice 02: Upper Bound ===");
        assertEquals(3, solveUpperBound(new int[]{1,3,5,7,9}, 5), "ub exact");
        System.out.println("  test_ub_exact.................... PASS");

        assertEquals(2, solveUpperBound(new int[]{1,3,5,7,9}, 4), "ub between");
        System.out.println("  test_ub_between.................. PASS");

        assertEquals(0, solveUpperBound(new int[]{1,3,5,7,9}, 0), "ub before all");
        System.out.println("  test_ub_before_all............... PASS");

        assertEquals(5, solveUpperBound(new int[]{1,3,5,7,9}, 9), "ub after last");
        System.out.println("  test_ub_after_last............... PASS");

        assertEquals(4, solveUpperBound(new int[]{2,2,2,2}, 2), "ub all same");
        System.out.println("  test_ub_all_same................. PASS");

        assertEquals(0, solveUpperBound(new int[]{}, 5), "ub empty");
        System.out.println("  test_ub_empty.................... PASS");
        System.out.println();
    }

    // ── Practice 03: Floor and Ceil ──────────────────────────────────

    static void testFloorAndCeil() {
        System.out.println("=== Practice 03: Floor and Ceil ===");
        assertArrayEquals(new int[]{5,5},
            solveFloorAndCeil(new int[]{1,3,5,7,9}, 5), "fc exact");
        System.out.println("  test_fc_exact.................... PASS");

        assertArrayEquals(new int[]{3,5},
            solveFloorAndCeil(new int[]{1,3,5,7,9}, 4), "fc between");
        System.out.println("  test_fc_between.................. PASS");

        assertArrayEquals(new int[]{-1,1},
            solveFloorAndCeil(new int[]{1,3,5,7,9}, 0), "fc below all");
        System.out.println("  test_fc_below_all................ PASS");

        assertArrayEquals(new int[]{9,-1},
            solveFloorAndCeil(new int[]{1,3,5,7,9}, 10), "fc above all");
        System.out.println("  test_fc_above_all................ PASS");

        assertArrayEquals(new int[]{1,1},
            solveFloorAndCeil(new int[]{1}, 1), "fc single exact");
        System.out.println("  test_fc_single_exact............. PASS");
        System.out.println();
    }

    // ── Practice 04: Search in Rotated Array ─────────────────────────

    static void testSearchRotated() {
        System.out.println("=== Practice 04: Search in Rotated Array ===");
        assertEquals(4, solveSearchRotated(new int[]{4,5,6,7,0,1,2}, 0), "rotated found");
        System.out.println("  test_rotated_found............... PASS");

        assertEquals(-1, solveSearchRotated(new int[]{4,5,6,7,0,1,2}, 3), "rotated not found");
        System.out.println("  test_rotated_not_found........... PASS");

        assertEquals(0, solveSearchRotated(new int[]{1}, 1), "rotated single");
        System.out.println("  test_rotated_single.............. PASS");

        assertEquals(1, solveSearchRotated(new int[]{3,1,2}, 1), "rotated small");
        System.out.println("  test_rotated_small............... PASS");

        assertEquals(2, solveSearchRotated(new int[]{1,2,3,4,5}, 3), "rotated not rotated");
        System.out.println("  test_rotated_not_rotated......... PASS");
        System.out.println();
    }

    // ── Practice 05: Find Min in Rotated ─────────────────────────────

    static void testMinInRotated() {
        System.out.println("=== Practice 05: Find Min in Rotated ===");
        assertEquals(1, solveMinInRotated(new int[]{3,4,5,1,2}), "min rotated");
        System.out.println("  test_min_rotated................. PASS");

        assertEquals(0, solveMinInRotated(new int[]{4,5,6,7,0,1,2}), "min rotated large");
        System.out.println("  test_min_rotated_large........... PASS");

        assertEquals(1, solveMinInRotated(new int[]{1}), "min single");
        System.out.println("  test_min_single.................. PASS");

        assertEquals(1, solveMinInRotated(new int[]{2,1}), "min pair");
        System.out.println("  test_min_pair.................... PASS");

        assertEquals(1, solveMinInRotated(new int[]{1,2,3,4,5}), "min not rotated");
        System.out.println("  test_min_not_rotated............. PASS");
        System.out.println();
    }

    // ── Challenge 01: Find Peak ──────────────────────────────────────

    static void testFindPeak() {
        System.out.println("=== Challenge 01: Find Peak ===");

        int[] a1 = {1,2,3,1};
        int peakL1 = solvePeakLinear(a1);
        int peakB1 = solvePeakBinary(a1);
        assert isPeak(a1, peakL1) : "peak linear {1,2,3,1} — index " + peakL1 + " is not a peak";
        assert isPeak(a1, peakB1) : "peak binary {1,2,3,1} — index " + peakB1 + " is not a peak";
        System.out.println("  test_peak_basic.................. PASS");

        int[] a2 = {1,2,1,3,5,6,4};
        int peakL2 = solvePeakLinear(a2);
        int peakB2 = solvePeakBinary(a2);
        assert isPeak(a2, peakL2) : "peak linear {1,2,1,3,5,6,4} — index " + peakL2 + " is not a peak";
        assert isPeak(a2, peakB2) : "peak binary {1,2,1,3,5,6,4} — index " + peakB2 + " is not a peak";
        System.out.println("  test_peak_multiple............... PASS");

        int[] a3 = {1};
        int peakL3 = solvePeakLinear(a3);
        int peakB3 = solvePeakBinary(a3);
        assert isPeak(a3, peakL3) : "peak linear {1} — index " + peakL3 + " is not a peak";
        assert isPeak(a3, peakB3) : "peak binary {1} — index " + peakB3 + " is not a peak";
        System.out.println("  test_peak_single................. PASS");

        int[] a4 = {3,2,1};
        int peakL4 = solvePeakLinear(a4);
        int peakB4 = solvePeakBinary(a4);
        assert isPeak(a4, peakL4) : "peak linear {3,2,1} — index " + peakL4 + " is not a peak";
        assert isPeak(a4, peakB4) : "peak binary {3,2,1} — index " + peakB4 + " is not a peak";
        System.out.println("  test_peak_descending............. PASS");

        int[] a5 = {1,2,3};
        int peakL5 = solvePeakLinear(a5);
        int peakB5 = solvePeakBinary(a5);
        assert isPeak(a5, peakL5) : "peak linear {1,2,3} — index " + peakL5 + " is not a peak";
        assert isPeak(a5, peakB5) : "peak binary {1,2,3} — index " + peakB5 + " is not a peak";
        System.out.println("  test_peak_ascending.............. PASS");

        int[] a6 = {5,10,20,15,7,3};
        int peakL6 = solvePeakLinear(a6);
        int peakB6 = solvePeakBinary(a6);
        assert isPeak(a6, peakL6) : "peak linear {5,10,20,15,7,3} — index " + peakL6 + " is not a peak";
        assert isPeak(a6, peakB6) : "peak binary {5,10,20,15,7,3} — index " + peakB6 + " is not a peak";
        System.out.println("  test_peak_mountain............... PASS");
        System.out.println();
    }

    // ── Challenge 02: Single Element ─────────────────────────────────

    static void testSingleElement() {
        System.out.println("=== Challenge 02: Single Element ===");
        assertEquals(2, solveSingleElement(new int[]{1,1,2,3,3,4,4,8,8}), "single middle");
        System.out.println("  test_single_middle............... PASS");

        assertEquals(10, solveSingleElement(new int[]{3,3,7,7,10,11,11}), "single late");
        System.out.println("  test_single_late................. PASS");

        assertEquals(1, solveSingleElement(new int[]{1}), "single only");
        System.out.println("  test_single_only................. PASS");

        assertEquals(2, solveSingleElement(new int[]{1,1,2}), "single at end");
        System.out.println("  test_single_at_end............... PASS");

        assertEquals(1, solveSingleElement(new int[]{1,2,2}), "single at start");
        System.out.println("  test_single_at_start............. PASS");
        System.out.println();
    }

    // ── Challenge 03: Search Rotated II (with duplicates) ────────────

    static void testRotatedSearchII() {
        System.out.println("=== Challenge 03: Rotated Search II ===");
        assertBoolEquals(true, solveRotatedSearchII(new int[]{2,5,6,0,0,1,2}, 0), "rsII found");
        System.out.println("  test_rsII_found.................. PASS");

        assertBoolEquals(false, solveRotatedSearchII(new int[]{2,5,6,0,0,1,2}, 3), "rsII not found");
        System.out.println("  test_rsII_not_found.............. PASS");

        assertBoolEquals(true, solveRotatedSearchII(new int[]{1,0,1,1,1}, 0), "rsII tricky dups");
        System.out.println("  test_rsII_tricky_dups............ PASS");

        assertBoolEquals(false, solveRotatedSearchII(new int[]{1,1,1,1,1}, 2), "rsII all same");
        System.out.println("  test_rsII_all_same............... PASS");

        assertBoolEquals(true, solveRotatedSearchII(new int[]{1}, 1), "rsII single");
        System.out.println("  test_rsII_single................. PASS");

        assertBoolEquals(true, solveRotatedSearchII(new int[]{1,3}, 3), "rsII pair");
        System.out.println("  test_rsII_pair................... PASS");
        System.out.println();
    }

    // ── Runner ───────────────────────────────────────────────────────

    public static void main(String[] args) {

        System.out.println("Testing Chapter 9...\n");

        System.out.println("--- Warmup Problems ---");
        testLinearSearch();
        testBinarySearch();
        testFirstOccurrence();
        testLastOccurrence();
        testCountOccurrences();

        System.out.println("--- Practice Problems ---");
        testLowerBound();
        testUpperBound();
        testFloorAndCeil();
        testSearchRotated();
        testMinInRotated();

        System.out.println("--- Challenge Problems ---");
        testFindPeak();
        testSingleElement();
        testRotatedSearchII();

        System.out.println("All tests passed!");
    }
}
