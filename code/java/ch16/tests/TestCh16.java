package ch16.tests;

import java.util.*;
import ch16.solutions.*;

/**
 * Tests for Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * Build and run:
 *   cd code/java
 *   javac -cp . ch16/tests/TestCh16.java ch16/solutions/*.java
 *   java -ea ch16.tests.TestCh16
 */
public class TestCh16 {

    static int passed = 0;
    static int failed = 0;

    static void assertEquals(int expected, int actual, String msg) {
        if (expected == actual) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertDoubleEquals(double expected, double actual, String msg) {
        if (Math.abs(expected - actual) < 1e-6) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertArrayEquals(int[] expected, int[] actual, String msg) {
        if (Arrays.equals(expected, actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected) + ", got " + Arrays.toString(actual)); }
    }

    static void assertTrue(boolean condition, String msg) {
        if (condition) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg); }
    }

    static boolean isPeak(int[] arr, int idx) {
        if (idx < 0 || idx >= arr.length) return false;
        boolean leftOk = (idx == 0) || (arr[idx] > arr[idx - 1]);
        boolean rightOk = (idx == arr.length - 1) || (arr[idx] > arr[idx + 1]);
        return leftOk && rightOk;
    }

    // ── W1: Square Root ────────────────────────────────────────────

    static void testW1() {
        assertEquals(4, Warmup01Sol.solve(16), "W1: perfect square 16");
        assertEquals(2, Warmup01Sol.solve(8), "W1: non-perfect 8");
        assertEquals(0, Warmup01Sol.solve(0), "W1: zero");
        assertEquals(1, Warmup01Sol.solve(1), "W1: one");
        assertEquals(10, Warmup01Sol.solve(100), "W1: 100");
        assertEquals(9, Warmup01Sol.solve(99), "W1: 99");
        assertEquals(1, Warmup01Sol.solve(2), "W1: two");
        assertEquals(7, Warmup01Sol.solve(49), "W1: 49");
    }

    // ── W2: First and Last Position ────────────────────────────────

    static void testW2() {
        assertArrayEquals(new int[]{3, 4}, Warmup02Sol.solve(new int[]{5,7,7,8,8,10}, 8), "W2: basic");
        assertArrayEquals(new int[]{-1, -1}, Warmup02Sol.solve(new int[]{5,7,7,8,8,10}, 6), "W2: not found");
        assertArrayEquals(new int[]{2, 2}, Warmup02Sol.solve(new int[]{1,2,3,4,5}, 3), "W2: single");
        assertArrayEquals(new int[]{0, 3}, Warmup02Sol.solve(new int[]{2,2,2,2}, 2), "W2: all same");
        assertArrayEquals(new int[]{-1, -1}, Warmup02Sol.solve(new int[]{}, 1), "W2: empty");
        assertArrayEquals(new int[]{0, 0}, Warmup02Sol.solve(new int[]{5}, 5), "W2: single found");
        assertArrayEquals(new int[]{-1, -1}, Warmup02Sol.solve(new int[]{5}, 3), "W2: single not found");
        assertArrayEquals(new int[]{0, 1}, Warmup02Sol.solve(new int[]{1,1,3,5,5}, 1), "W2: boundary left");
        assertArrayEquals(new int[]{3, 4}, Warmup02Sol.solve(new int[]{1,1,3,5,5}, 5), "W2: boundary right");
    }

    // ── W3: Search in Rotated Sorted Array ─────────────────────────

    static void testW3() {
        assertEquals(4, Warmup03Sol.solve(new int[]{4,5,6,7,0,1,2}, 0), "W3: basic");
        assertEquals(-1, Warmup03Sol.solve(new int[]{4,5,6,7,0,1,2}, 3), "W3: not found");
        assertEquals(0, Warmup03Sol.solve(new int[]{1}, 1), "W3: single");
        assertEquals(2, Warmup03Sol.solve(new int[]{1,2,3,4,5}, 3), "W3: not rotated");
        assertEquals(-1, Warmup03Sol.solve(new int[]{}, 5), "W3: empty");
        assertEquals(2, Warmup03Sol.solve(new int[]{3,4,5,1,2}, 5), "W3: at pivot");
        assertEquals(1, Warmup03Sol.solve(new int[]{2,1}, 1), "W3: two elements");
        assertEquals(0, Warmup03Sol.solve(new int[]{4,5,6,7,0,1,2}, 4), "W3: first element");
    }

    // ── W4: Peak Element ───────────────────────────────────────────

    static void testW4() {
        assertTrue(isPeak(new int[]{1,2,3,1}, Warmup04Sol.solve(new int[]{1,2,3,1})), "W4: basic");
        assertTrue(isPeak(new int[]{1,2,1,3,5,6,4}, Warmup04Sol.solve(new int[]{1,2,1,3,5,6,4})), "W4: multiple peaks");
        assertEquals(0, Warmup04Sol.solve(new int[]{1}), "W4: single");
        assertTrue(isPeak(new int[]{1,2,3,4,5}, Warmup04Sol.solve(new int[]{1,2,3,4,5})), "W4: ascending");
        assertTrue(isPeak(new int[]{5,4,3,2,1}, Warmup04Sol.solve(new int[]{5,4,3,2,1})), "W4: descending");
        assertTrue(isPeak(new int[]{1,2}, Warmup04Sol.solve(new int[]{1,2})), "W4: two asc");
        assertTrue(isPeak(new int[]{2,1}, Warmup04Sol.solve(new int[]{2,1})), "W4: two desc");
    }

    // ── P1: Koko Eating Bananas ────────────────────────────────────

    static void testP1() {
        assertEquals(4, Practice01Sol.solve(new int[]{3,6,7,11}, 8), "P1: basic");
        assertEquals(10, Practice01Sol.solve(new int[]{30}, 3), "P1: single pile");
        assertEquals(5, Practice01Sol.solve(new int[]{5,5,5,5}, 4), "P1: equal piles");
        assertEquals(2, Practice01Sol.solve(new int[]{3,6,7,11}, 20), "P1: generous time");
        assertEquals(30, Practice01Sol.solve(new int[]{30,11,23,4,20}, 5), "P1: tight time");
        assertEquals(10, Practice01Sol.solve(new int[]{10,10,10}, 3), "P1: exact fit");
        assertEquals(7, Practice01Sol.solve(new int[]{7}, 1), "P1: one pile one hour");
    }

    // ── P2: Ship Packages ──────────────────────────────────────────

    static void testP2() {
        assertEquals(15, Practice02Sol.solve(new int[]{1,2,3,4,5,6,7,8,9,10}, 5), "P2: basic");
        assertEquals(16, Practice02Sol.solve(new int[]{3,2,2,4,1,4}, 1), "P2: one day");
        assertEquals(4, Practice02Sol.solve(new int[]{3,2,2,4,1,4}, 6), "P2: many days");
        assertEquals(10, Practice02Sol.solve(new int[]{10}, 1), "P2: single");
        assertEquals(10, Practice02Sol.solve(new int[]{5,5,5,5}, 2), "P2: equal");
        assertEquals(3, Practice02Sol.solve(new int[]{1,2,3,1,1}, 4), "P2: heavy last");
        assertEquals(6, Practice02Sol.solve(new int[]{3,2,2,4,1,4}, 3), "P2: three days");
    }

    // ── P3: Search in 2D Matrix ────────────────────────────────────

    static void testP3() {
        int[][] m1 = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
        assertArrayEquals(new int[]{0, 1}, Practice03Sol.solve(m1, 3), "P3: basic");
        assertArrayEquals(new int[]{-1, -1}, Practice03Sol.solve(m1, 13), "P3: not found");
        int[][] m2 = {{1,3,5},{7,9,11}};
        assertArrayEquals(new int[]{0, 0}, Practice03Sol.solve(m2, 1), "P3: first");
        assertArrayEquals(new int[]{1, 2}, Practice03Sol.solve(m2, 11), "P3: last");
        assertArrayEquals(new int[]{0, 0}, Practice03Sol.solve(new int[][]{{5}}, 5), "P3: single found");
        assertArrayEquals(new int[]{-1, -1}, Practice03Sol.solve(new int[][]{{5}}, 3), "P3: single not found");
        assertArrayEquals(new int[]{-1, -1}, Practice03Sol.solve(new int[][]{}, 1), "P3: empty");
    }

    // ── P4: Row with Maximum 1s ────────────────────────────────────

    static void testP4() {
        int[][] m1 = {{0,0,0,1,1},{0,0,1,1,1},{0,0,0,0,1},{0,1,1,1,1},{0,0,0,0,0}};
        assertEquals(3, Practice04Sol.solve(m1), "P4: basic");
        assertEquals(-1, Practice04Sol.solve(new int[][]{{0,0,0},{0,0,0}}), "P4: all zeros");
        assertEquals(0, Practice04Sol.solve(new int[][]{{1,1,1},{1,1,1}}), "P4: all ones");
        assertEquals(0, Practice04Sol.solve(new int[][]{{0,1,1}}), "P4: single row");
        assertEquals(0, Practice04Sol.solve(new int[][]{{1}}), "P4: single 1");
        assertEquals(-1, Practice04Sol.solve(new int[][]{{0}}), "P4: single 0");
        assertEquals(2, Practice04Sol.solve(new int[][]{{0,0,0},{0,0,1},{0,1,1}}), "P4: last row wins");
    }

    // ── P5: Minimum Pages Allocation ───────────────────────────────

    static void testP5() {
        assertEquals(113, Practice05Sol.solve(new int[]{12,34,67,90}, 2), "P5: basic");
        assertEquals(60, Practice05Sol.solve(new int[]{10,20,30}, 1), "P5: single student");
        assertEquals(30, Practice05Sol.solve(new int[]{10,20,30}, 3), "P5: one each");
        assertEquals(50, Practice05Sol.solve(new int[]{25,25,25,25}, 2), "P5: equal");
        assertEquals(-1, Practice05Sol.solve(new int[]{10,20}, 3), "P5: more students");
        assertEquals(100, Practice05Sol.solve(new int[]{5,5,5,100}, 2), "P5: large last");
        assertEquals(50, Practice05Sol.solve(new int[]{50}, 1), "P5: single book");
    }

    // ── C1: Aggressive Cows ────────────────────────────────────────

    static void testC1() {
        assertEquals(3, Challenge01Sol.solve(new int[]{1,2,8,4,9}, 3), "C1: basic");
        assertEquals(8, Challenge01Sol.solve(new int[]{1,2,4,8,9}, 2), "C1: two cows");
        assertEquals(2, Challenge01Sol.solve(new int[]{1,3,5}, 3), "C1: all used");
        assertEquals(99, Challenge01Sol.solve(new int[]{1,100}, 2), "C1: large gap");
        assertEquals(4, Challenge01Sol.solve(new int[]{1,5,9,13}, 4), "C1: evenly spaced");
        assertEquals(4, Challenge01Sol.solve(new int[]{10,1,5,7,3}, 3), "C1: unsorted");
        assertEquals(9, Challenge01Sol.solve(new int[]{1,2,3,4,5,6,7,8,9,10}, 2), "C1: many stalls");
    }

    // ── C2: Painter's Partition ────────────────────────────────────

    static void testC2() {
        assertEquals(60, Challenge02Sol.solve(new int[]{10,20,30,40}, 2), "C2: basic");
        assertEquals(60, Challenge02Sol.solve(new int[]{10,20,30}, 1), "C2: single painter");
        assertEquals(30, Challenge02Sol.solve(new int[]{10,20,30}, 3), "C2: one each");
        assertEquals(50, Challenge02Sol.solve(new int[]{25,25,25,25}, 2), "C2: equal");
        assertEquals(20, Challenge02Sol.solve(new int[]{10,20}, 5), "C2: more painters");
        assertEquals(100, Challenge02Sol.solve(new int[]{5,5,5,100}, 2), "C2: large board");
        assertEquals(5, Challenge02Sol.solve(new int[]{1,2,3,4,5}, 5), "C2: many painters");
    }

    // ── C3: Median of Two Sorted Arrays ────────────────────────────

    static void testC3() {
        assertDoubleEquals(2.0, Challenge03Sol.solve(new int[]{1,3}, new int[]{2}), "C3: odd total");
        assertDoubleEquals(2.5, Challenge03Sol.solve(new int[]{1,2}, new int[]{3,4}), "C3: even total");
        assertDoubleEquals(1.0, Challenge03Sol.solve(new int[]{}, new int[]{1}), "C3: one empty");
        assertDoubleEquals(2.0, Challenge03Sol.solve(new int[]{2}, new int[]{}), "C3: other empty");
        assertDoubleEquals(1.0, Challenge03Sol.solve(new int[]{1,1}, new int[]{1,1}), "C3: all same");
        assertDoubleEquals(3.0, Challenge03Sol.solve(new int[]{1,2}, new int[]{3,4,5}), "C3: no overlap");
        assertDoubleEquals(1.5, Challenge03Sol.solve(new int[]{1}, new int[]{2}), "C3: single each");
        assertDoubleEquals(4.5, Challenge03Sol.solve(new int[]{1,3,5,7}, new int[]{2,4,6,8}), "C3: interleaved");
    }

    // ── C4: Kth Element of Two Sorted Arrays ───────────────────────

    static void testC4() {
        assertEquals(6, Challenge04Sol.solve(new int[]{2,3,6,7,9}, new int[]{1,4,8,10}, 5), "C4: basic");
        assertEquals(1, Challenge04Sol.solve(new int[]{1,3,5}, new int[]{2,4,6}, 1), "C4: first");
        assertEquals(4, Challenge04Sol.solve(new int[]{1,3}, new int[]{2,4}, 4), "C4: last");
        assertEquals(2, Challenge04Sol.solve(new int[]{}, new int[]{1,2,3}, 2), "C4: one empty");
        assertEquals(15, Challenge04Sol.solve(new int[]{5,10,15}, new int[]{}, 3), "C4: other empty");
        assertEquals(3, Challenge04Sol.solve(new int[]{1,2,3}, new int[]{10,20,30}, 3), "C4: all from first");
        assertEquals(3, Challenge04Sol.solve(new int[]{10,20,30}, new int[]{1,2,3}, 3), "C4: all from second");
        assertEquals(1, Challenge04Sol.solve(new int[]{3,5}, new int[]{1,7}, 1), "C4: k=1");
    }

    // ── Main ───────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 16: Binary Search Beyond Arrays — Searching on Answers");
        System.out.println("================================================================\n");

        testW1();
        testW2();
        testW3();
        testW4();
        testP1();
        testP2();
        testP3();
        testP4();
        testP5();
        testC1();
        testC2();
        testC3();
        testC4();

        System.out.println();
        if (failed == 0) {
            System.out.println("All " + passed + " tests passed!");
        } else {
            System.out.println(passed + " passed, " + failed + " failed.");
            System.exit(1);
        }
    }
}
