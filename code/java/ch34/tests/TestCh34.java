package ch34.tests;

import java.util.*;
import ch34.solutions.*;

/**
 * Tests for Chapter 34: Computational Geometry & Sweep Line
 *
 * Build and run:
 *   cd code/java
 *   javac ch34/tests/TestCh34.java
 *   java -ea ch34.tests.TestCh34
 */
public class TestCh34 {

    static int passed = 0;
    static int failed = 0;

    static void assertEquals(int expected, int actual, String msg) {
        if (expected == actual) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual);
        }
    }

    static void assertDoubleEquals(double expected, double actual, String msg) {
        if (Math.abs(expected - actual) < 1e-6) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual);
        }
    }

    static void assertBoolEquals(boolean expected, boolean actual, String msg) {
        if (expected == actual) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual);
        }
    }

    static void assertArrayEquals(int[] expected, int[] actual, String msg) {
        if (Arrays.equals(expected, actual)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected)
                + ", got " + Arrays.toString(actual));
        }
    }

    static void assertBoolArrayEquals(boolean[] expected, boolean[] actual, String msg) {
        if (Arrays.equals(expected, actual)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected)
                + ", got " + Arrays.toString(actual));
        }
    }

    static void assert2DArrayEquals(int[][] expected, int[][] actual, String msg) {
        if (expected.length != actual.length) {
            failed++;
            System.out.println("FAIL: " + msg + " — length mismatch: expected " + expected.length
                + ", got " + actual.length);
            return;
        }
        for (int i = 0; i < expected.length; i++) {
            if (!Arrays.equals(expected[i], actual[i])) {
                failed++;
                System.out.println("FAIL: " + msg + " — diff at index " + i);
                return;
            }
        }
        passed++;
    }

    // ── Tests ───────────────────────────────────────────────────────

    static void testW1() {
        int[][][] queries1 = {{{0,0},{4,4},{1,2}}, {{0,0},{4,4},{1,0}}, {{0,0},{4,4},{2,2}}};
        assertArrayEquals(new int[]{1, -1, 0}, Warmup01Sol.solve(queries1), "W1: mixed orientations");

        int[][][] queries2 = {{{0,0},{1,0},{0,1}}};
        assertArrayEquals(new int[]{1}, Warmup01Sol.solve(queries2), "W1: ccw");

        int[][][] queries3 = {{{0,0},{1,1},{2,2}}, {{0,0},{5,5},{10,10}}};
        assertArrayEquals(new int[]{0, 0}, Warmup01Sol.solve(queries3), "W1: collinear");

        int[][][] queries4 = {{{0,0},{0,1},{1,0}}};
        assertArrayEquals(new int[]{-1}, Warmup01Sol.solve(queries4), "W1: cw");
    }

    static void testW2() {
        assert2DArrayEquals(new int[][]{{0,0},{2,0},{2,2},{0,2}},
            Warmup02Sol.solve(new int[][]{{0,0},{2,0},{0,2},{2,2},{1,1}}), "W2: square with interior");
        assert2DArrayEquals(new int[][]{{0,0},{2,0}},
            Warmup02Sol.solve(new int[][]{{0,0},{1,0},{2,0}}), "W2: collinear");
        assert2DArrayEquals(new int[][]{{0,0},{4,0},{2,3}},
            Warmup02Sol.solve(new int[][]{{0,0},{4,0},{2,3}}), "W2: triangle");
    }

    static void testW3() {
        assertDoubleEquals(12.0, Warmup03Sol.solve(new int[][]{{0,0},{4,0},{4,3},{0,3}}), "W3: rectangle");
        assertDoubleEquals(0.5, Warmup03Sol.solve(new int[][]{{0,0},{1,0},{0,1}}), "W3: triangle");
        assertDoubleEquals(4.0, Warmup03Sol.solve(new int[][]{{0,0},{2,0},{2,2},{0,2}}), "W3: square");
        assertDoubleEquals(12.0, Warmup03Sol.solve(new int[][]{{0,3},{4,3},{4,0},{0,0}}), "W3: reverse");
    }

    static void testP1() {
        assertDoubleEquals(Math.sqrt(2), Practice01Sol.solve(new int[][]{{0,0},{3,4},{1,1},{5,5}}), "P1: basic");
        assertDoubleEquals(1.0, Practice01Sol.solve(new int[][]{{0,0},{1,0},{0,1}}), "P1: unit");
        assertDoubleEquals(Math.sqrt(200), Practice01Sol.solve(new int[][]{{0,0},{10,10}}), "P1: two points");
        assertDoubleEquals(2.0, Practice01Sol.solve(new int[][]{{0,0},{2,0},{5,0}}), "P1: collinear");
    }

    static void testP2() {
        assertBoolArrayEquals(new boolean[]{true, false, false},
            Practice02Sol.solve(new int[][][]{
                {{0,0},{2,2},{0,2},{2,0}},
                {{0,0},{1,0},{2,0},{3,0}},
                {{0,0},{1,1},{2,2},{3,3}}
            }), "P2: mixed");
        assertBoolArrayEquals(new boolean[]{true},
            Practice02Sol.solve(new int[][][]{
                {{0,0},{1,1},{1,1},{2,0}}
            }), "P2: touching");
        assertBoolArrayEquals(new boolean[]{true},
            Practice02Sol.solve(new int[][][]{
                {{0,0},{2,0},{1,0},{3,0}}
            }), "P2: overlapping collinear");
    }

    static void testP3() {
        assertBoolArrayEquals(new boolean[]{true, false, true, true},
            Practice03Sol.solve(new int[][]{{0,0},{4,0},{4,4},{0,4}},
                                new int[][]{{2,2},{5,5},{0,0},{4,2}}), "P3: square");
        assertBoolArrayEquals(new boolean[]{true, false},
            Practice03Sol.solve(new int[][]{{0,0},{2,0},{1,2}},
                                new int[][]{{1,1},{3,3}}), "P3: triangle");
        assertBoolArrayEquals(new boolean[]{true, true, true},
            Practice03Sol.solve(new int[][]{{0,0},{4,0},{4,4},{0,4}},
                                new int[][]{{2,0},{0,2},{4,4}}), "P3: boundary");
    }

    static void testP4() {
        assertEquals(3, Practice04Sol.solve(new int[][]{{1,1},{2,2},{3,3},{4,1}}), "P4: three collinear");
        assertEquals(4, Practice04Sol.solve(new int[][]{{1,1},{3,2},{5,3},{4,1},{2,3},{1,4}}), "P4: four");
        assertEquals(1, Practice04Sol.solve(new int[][]{{0,0}}), "P4: single");
        assertEquals(2, Practice04Sol.solve(new int[][]{{0,0},{1,1}}), "P4: two");
    }

    static void testC1() {
        assertDoubleEquals(14.0, Challenge01Sol.solve(new int[][]{{0,0},{4,0},{4,3},{0,3},{2,1}}), "C1: rectangle");
        assertDoubleEquals(2 + Math.sqrt(2), Challenge01Sol.solve(new int[][]{{0,0},{1,0},{0,1}}), "C1: triangle");
        assertDoubleEquals(0.0, Challenge01Sol.solve(new int[][]{{5,5}}), "C1: single point");
        assertDoubleEquals(10.0, Challenge01Sol.solve(new int[][]{{0,0},{3,4}}), "C1: two points");
    }

    static void testC2() {
        assertEquals(10, Challenge02Sol.solve(new int[]{2,1,5,6,2,3}), "C2: basic");
        assertEquals(4, Challenge02Sol.solve(new int[]{2,4}), "C2: two bars");
        assertEquals(1, Challenge02Sol.solve(new int[]{1}), "C2: single");
        assertEquals(9, Challenge02Sol.solve(new int[]{1,2,3,4,5}), "C2: increasing");
        assertEquals(12, Challenge02Sol.solve(new int[]{3,3,3,3}), "C2: all same");
    }

    static void testC3() {
        assertEquals(7, Challenge03Sol.solve(new int[][]{{0,0,2,2},{1,1,3,3}}), "C3: overlapping");
        assertEquals(2, Challenge03Sol.solve(new int[][]{{0,0,1,1},{2,2,3,3}}), "C3: disjoint");
        assertEquals(100, Challenge03Sol.solve(new int[][]{{0,0,10,10},{1,1,9,9}}), "C3: contained");
        assertEquals(25, Challenge03Sol.solve(new int[][]{{0,0,5,5}}), "C3: single");
        assertEquals(19, Challenge03Sol.solve(new int[][]{{0,0,3,3},{1,1,4,4},{2,2,5,5}}), "C3: three overlap");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 34: Computational Geometry & Sweep Line");
        System.out.println("================================================================\n");

        testW1(); testW2(); testW3();
        testP1(); testP2(); testP3(); testP4();
        testC1(); testC2(); testC3();

        System.out.println();
        if (failed == 0) {
            System.out.println("All " + passed + " tests passed!");
        } else {
            System.out.println(passed + " passed, " + failed + " failed.");
            System.exit(1);
        }
    }
}
