package ch30.tests;

import java.util.*;
import ch30.solutions.*;

/**
 * Tests for Chapter 30: Segment Trees & Range Queries
 *
 * Build and run:
 *   cd code/java
 *   javac ch30/tests/TestCh30.java
 *   java -ea ch30.tests.TestCh30
 */
public class TestCh30 {

    static int passed = 0;
    static int failed = 0;

    static void assertEquals(int expected, int actual, String msg) {
        if (expected == actual) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertLongEquals(long expected, long actual, String msg) {
        if (expected == actual) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertArrayEquals(int[] expected, int[] actual, String msg) {
        if (Arrays.equals(expected, actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected) + ", got " + Arrays.toString(actual)); }
    }

    static void assertLongArrayEquals(long[] expected, long[] actual, String msg) {
        if (Arrays.equals(expected, actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected) + ", got " + Arrays.toString(actual)); }
    }

    // ── Tests ───────────────────────────────────────────────────────

    static void testW1() {
        assertArrayEquals(new int[]{15, 22},
            Warmup01Sol.solve(new int[]{1,3,5,7,9,11}, new int[][]{{1,1,3},{2,1,10},{1,1,3}}), "W1: basic");
        assertArrayEquals(new int[]{15, 22},
            Warmup01Sol.solve(new int[]{1,2,3,4,5}, new int[][]{{1,0,4},{2,2,10},{1,0,4}}), "W1: full range");
        assertArrayEquals(new int[]{5, 3},
            Warmup01Sol.solve(new int[]{5}, new int[][]{{1,0,0},{2,0,3},{1,0,0}}), "W1: single");
    }

    static void testW2() {
        assertArrayEquals(new int[]{1, 2},
            Warmup02Sol.solve(new int[]{2,5,1,4,9,3}, new int[][]{{1,0,5},{2,2,8},{1,0,5}}), "W2: basic");
        assertArrayEquals(new int[]{1, 2},
            Warmup02Sol.solve(new int[]{7,3,8,1,6}, new int[][]{{1,1,3},{2,3,2},{1,1,3}}), "W2: update");
    }

    static void testW3() {
        assertArrayEquals(new int[]{10, 15},
            Warmup03Sol.solve(new int[]{1,2,3,4,5}, new int[][]{{1,3,0},{2,2,5},{1,3,0}}), "W3: basic");
        assertArrayEquals(new int[]{14, 16},
            Warmup03Sol.solve(new int[]{3,1,4,1,5}, new int[][]{{1,4,0},{2,0,2},{1,4,0}}), "W3: with add");
    }

    static void testW4() {
        assertEquals(5, Warmup04Sol.solve(new int[]{2,3,8,6,1}), "W4: mixed");
        assertEquals(10, Warmup04Sol.solve(new int[]{5,4,3,2,1}), "W4: reverse");
        assertEquals(0, Warmup04Sol.solve(new int[]{1,2,3,4,5}), "W4: sorted");
        assertEquals(0, Warmup04Sol.solve(new int[]{1,1,1}), "W4: same");
    }

    static void testP1() {
        assertLongArrayEquals(new long[]{15, 15},
            Practice01Sol.solve(5, new int[][]{{1,0,4,3},{2,0,4},{1,1,3,2},{2,1,3}}), "P1: basic");
        assertLongArrayEquals(new long[]{15, 15},
            Practice01Sol.solve(3, new int[][]{{1,0,2,5},{2,0,2},{1,0,0,10},{2,0,0}}), "P1: add then query");
    }

    static void testP2() {
        assertArrayEquals(new int[]{9, 6},
            Practice02Sol.solve(new int[]{3,1,4,1,5,9,2,6}, new int[][]{{1,0,7},{2,5,1},{1,0,7}}), "P2: basic");
        assertArrayEquals(new int[]{3, 5},
            Practice02Sol.solve(new int[]{1,2,3}, new int[][]{{1,0,2},{2,1,5},{1,0,2}}), "P2: small");
    }

    static void testP3() {
        assertArrayEquals(new int[]{5, 3, 3},
            Practice03Sol.solve(new int[]{1,3,5,7,9,2,4,6}, new int[][]{{0,7,3,7},{0,3,1,5},{2,5,5,9}}), "P3: basic");
        assertArrayEquals(new int[]{1},
            Practice03Sol.solve(new int[]{10,20,30}, new int[][]{{0,2,15,25}}), "P3: single match");
    }

    static void testP4() {
        assertArrayEquals(new int[]{3, 5},
            Practice04Sol.solve(new int[][]{{1,5},{1,3},{1,7},{1,1},{3,2},{2,3},{3,2}}), "P4: basic");
        assertArrayEquals(new int[]{10},
            Practice04Sol.solve(new int[][]{{1,10},{3,1}}), "P4: single");
    }

    static void testP5() {
        assertArrayEquals(new int[]{1, 5},
            Practice05Sol.solve(new int[]{1,2,3,4,5}, new int[][]{{1,0,4},{2,2,7},{1,0,4}}), "P5: basic");
        assertArrayEquals(new int[]{6, 3},
            Practice05Sol.solve(new int[]{3,5}, new int[][]{{1,0,1},{2,0,6},{1,0,1}}), "P5: small");
    }

    static void testC1() {
        assertLongArrayEquals(new long[]{15, 21},
            Challenge01Sol.solve(5, new int[][]{{1,0,4,3},{2,0,4},{1,1,3,5},{2,0,4}}), "C1: basic");
        assertLongArrayEquals(new long[]{30, 20},
            Challenge01Sol.solve(3, new int[][]{{1,0,2,10},{2,0,2},{1,1,1,0},{2,0,2}}), "C1: overwrite");
    }

    static void testC2() {
        assertArrayEquals(new int[]{3, 2, 3},
            Challenge02Sol.solve(new int[]{1,2,1,3,2,1}, new int[][]{{0,5},{0,2},{3,5}}), "C2: basic");
        assertArrayEquals(new int[]{1},
            Challenge02Sol.solve(new int[]{1,1,1}, new int[][]{{0,2}}), "C2: all same");
    }

    static void testC3() {
        assertArrayEquals(new int[]{8, 8, 7},
            Challenge03Sol.solve(new int[]{1,-2,3,4,-1,2,-5,3}, new int[][]{{0,7},{2,5},{0,3}}), "C3: basic");
        assertArrayEquals(new int[]{-1},
            Challenge03Sol.solve(new int[]{-1,-2,-3}, new int[][]{{0,2}}), "C3: all negative");
    }

    static void testC4() {
        assertEquals(2, Challenge04Sol.solve(new int[][]{{1,3},{2,5},{4,7},{6,9}}), "C4: overlapping");
        assertEquals(4, Challenge04Sol.solve(new int[][]{{1,2},{2,3},{3,4},{4,5}}), "C4: non-overlapping");
        assertEquals(3, Challenge04Sol.solve(new int[][]{{1,10},{2,3},{4,5},{6,7}}), "C4: one large");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 30: Segment Trees & Range Queries");
        System.out.println("================================================================\n");

        testW1(); testW2(); testW3(); testW4();
        testP1(); testP2(); testP3(); testP4(); testP5();
        testC1(); testC2(); testC3(); testC4();

        System.out.println();
        if (failed == 0) {
            System.out.println("All " + passed + " tests passed!");
        } else {
            System.out.println(passed + " passed, " + failed + " failed.");
            System.exit(1);
        }
    }
}
