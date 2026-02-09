package ch27.tests;

import java.util.*;
import ch27.solutions.*;

/**
 * Tests for Chapter 27: Shortest Paths — Finding the Best Route
 *
 * Build and run:
 *   cd code/java
 *   javac ch27/tests/TestCh27.java
 *   java -ea ch27.tests.TestCh27
 */
public class TestCh27 {

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

    static void assertArrayEquals(int[] expected, int[] actual, String msg) {
        if (Arrays.equals(expected, actual)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected)
                + ", got " + Arrays.toString(actual));
        }
    }

    // ── Tests ───────────────────────────────────────────────────────

    static void testW1() {
        assertArrayEquals(new int[]{0,3,1,8,9},
            Warmup01Sol.solve(5, new int[][]{{0,1,4},{0,2,1},{2,1,2},{1,3,5},{2,3,8},{3,4,1}}, 0), "W1: basic");
        assertArrayEquals(new int[]{0,1,3},
            Warmup01Sol.solve(3, new int[][]{{0,1,1},{1,2,2}}, 0), "W1: linear");
        assertArrayEquals(new int[]{0},
            Warmup01Sol.solve(1, new int[][]{}, 0), "W1: single");
        int[] r = Warmup01Sol.solve(3, new int[][]{{0,1,5}}, 0);
        assertEquals(0, r[0], "W1: unreachable src");
        assertEquals(5, r[1], "W1: unreachable mid");
        assertEquals((int) 1e9, r[2], "W1: unreachable end");
    }

    static void testW2() {
        assertEquals(2, Warmup02Sol.solve(new int[][]{{2,1,1},{2,3,1},{3,4,1}}, 4, 2), "W2: basic");
        assertEquals(-1, Warmup02Sol.solve(new int[][]{{1,2,1}}, 2, 2), "W2: unreachable");
        assertEquals(1, Warmup02Sol.solve(new int[][]{{1,2,1}}, 2, 1), "W2: single edge");
        assertEquals(0, Warmup02Sol.solve(new int[][]{}, 1, 1), "W2: single node");
    }

    static void testW3() {
        assertArrayEquals(new int[]{0,-1,2,-2,1},
            Warmup03Sol.solve(5, new int[][]{{0,1,-1},{0,2,4},{1,2,3},{1,3,2},{1,4,2},{3,2,5},{3,1,1},{4,3,-3}}, 0), "W3: negative");
        assertArrayEquals(new int[]{0,3,1},
            Warmup03Sol.solve(3, new int[][]{{0,1,4},{0,2,1},{2,1,2}}, 0), "W3: positive");
        assertArrayEquals(new int[]{0},
            Warmup03Sol.solve(1, new int[][]{}, 0), "W3: single");
    }

    static void testW4() {
        assertEquals(2, Warmup04Sol.solve(new int[][]{{0,1},{1,0}}), "W4: 2x2");
        assertEquals(4, Warmup04Sol.solve(new int[][]{{0,0,0},{1,1,0},{1,1,0}}), "W4: 3x3");
        assertEquals(-1, Warmup04Sol.solve(new int[][]{{1,0,0},{0,0,0},{0,0,0}}), "W4: blocked start");
        assertEquals(1, Warmup04Sol.solve(new int[][]{{0}}), "W4: single cell");
    }

    static void testP1() {
        assertEquals(700, Practice01Sol.solve(4,
            new int[][]{{0,1,100},{1,2,100},{2,0,100},{1,3,600},{2,3,200}}, 0, 3, 1), "P1: basic");
        assertEquals(200, Practice01Sol.solve(3,
            new int[][]{{0,1,100},{1,2,100},{0,2,500}}, 0, 2, 1), "P1: via stop");
        assertEquals(500, Practice01Sol.solve(3,
            new int[][]{{0,1,100},{1,2,100},{0,2,500}}, 0, 2, 0), "P1: no stops");
        assertEquals(-1, Practice01Sol.solve(3,
            new int[][]{{0,1,100}}, 0, 2, 1), "P1: unreachable");
    }

    static void testP2() {
        assertEquals(2, Practice02Sol.solve(new int[][]{{1,2,2},{3,8,2},{5,3,5}}), "P2: basic");
        assertEquals(1, Practice02Sol.solve(new int[][]{{1,2,3},{3,8,4},{5,3,5}}), "P2: small diff");
        assertEquals(0, Practice02Sol.solve(new int[][]{{1,2,1,1,1},{1,2,1,2,1},{1,2,1,2,1},{1,2,1,2,1},{1,1,1,2,1}}), "P2: zero effort");
    }

    static void testP3() {
        assertEquals(3, Practice03Sol.solve(4,
            new int[][]{{0,1,3},{1,2,1},{1,3,4},{2,3,1}}, 4), "P3: basic");
        assertEquals(0, Practice03Sol.solve(5,
            new int[][]{{0,1,2},{0,4,8},{1,2,3},{1,4,2},{2,3,1},{3,4,1}}, 2), "P3: larger");
    }

    static void testP4() {
        assertEquals(4, Practice04Sol.solve(7,
            new int[][]{{0,6,7},{0,1,2},{1,2,3},{1,3,3},{6,3,3},{3,5,1},{6,5,1},{2,5,1},{0,4,5},{4,6,2}}), "P4: basic");
        assertEquals(1, Practice04Sol.solve(2, new int[][]{{1,0,10}}), "P4: two nodes");
    }

    static void testP5() {
        assertEquals(3, Practice05Sol.solve(new int[][]{{0,2},{1,3}}), "P5: 2x2");
        assertEquals(16, Practice05Sol.solve(new int[][]{{0,1,2,3,4},{24,23,22,21,5},{12,13,14,15,16},{11,17,18,19,20},{10,9,8,7,6}}), "P5: 5x5");
    }

    static void testC1() {
        assertEquals(2, Challenge01Sol.solve(new int[][]{{0,1,1},{1,1,0},{1,1,0}}), "C1: basic");
        assertEquals(0, Challenge01Sol.solve(new int[][]{{0,1,0,0,0},{0,1,0,1,0},{0,0,0,1,0}}), "C1: clear path");
    }

    static void testC2() {
        assertArrayEquals(new int[]{0,1,-1},
            Challenge02Sol.solve(3, new int[][]{{0,1},{1,2}}, new int[][]{}), "C2: red only");
        assertArrayEquals(new int[]{0,1,-1},
            Challenge02Sol.solve(3, new int[][]{{0,1}}, new int[][]{{2,1}}), "C2: mixed");
        assertArrayEquals(new int[]{0,1,1},
            Challenge02Sol.solve(3, new int[][]{{0,1},{0,2}}, new int[][]{{1,0}}), "C2: both colors");
    }

    static void testC3() {
        assertEquals(2, Challenge03Sol.solve(new int[][]{{1,1,2},{1,1,2},{1,1,1}}), "C3: needs changes");
        assertEquals(0, Challenge03Sol.solve(new int[][]{{1,1,3},{3,2,2},{1,1,4}}), "C3: free path");
        assertEquals(3, Challenge03Sol.solve(new int[][]{{2,2,2},{2,2,2}}), "C3: all left");
    }

    static void testC4() {
        assertEquals(4, Challenge04Sol.solve(new int[][]{{5,4,5},{1,2,6},{7,4,6}}), "C4: basic");
        assertEquals(2, Challenge04Sol.solve(new int[][]{{2,2,1,2,2,2},{1,2,2,2,1,2}}), "C4: narrow");
        assertEquals(3, Challenge04Sol.solve(new int[][]{{3,4,6,3,4},{0,2,1,1,7},{8,8,3,2,7},{3,2,4,9,8},{4,1,2,0,0},{4,6,5,4,3}}), "C4: larger");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 27: Shortest Paths — Finding the Best Route");
        System.out.println("====================================================\n");

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
