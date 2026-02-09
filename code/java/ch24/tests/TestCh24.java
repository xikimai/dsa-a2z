package ch24.tests;

import java.util.*;
import ch24.solutions.*;

/**
 * Tests for Chapter 24: Dynamic Programming II — Grids and Paths
 *
 * Build and run:
 *   cd code/java
 *   javac ch24/tests/TestCh24.java
 *   java -ea ch24.tests.TestCh24
 */
public class TestCh24 {

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

    // ── Tests ───────────────────────────────────────────────────────

    static void testW1() {
        assertEquals(28, Warmup01Sol.solve(3, 7), "W1: (3,7)");
        assertEquals(1, Warmup01Sol.solve(1, 1), "W1: (1,1)");
        assertEquals(3, Warmup01Sol.solve(3, 2), "W1: (3,2)");
        assertEquals(3, Warmup01Sol.solve(2, 3), "W1: (2,3)");
        assertEquals(48620, Warmup01Sol.solve(10, 10), "W1: (10,10)");
        assertEquals(1, Warmup01Sol.solve(1, 5), "W1: (1,5)");
        assertEquals(1, Warmup01Sol.solve(5, 1), "W1: (5,1)");
    }

    static void testW2() {
        assertEquals(2, Warmup02Sol.solve(new int[][]{{0,0,0},{0,1,0},{0,0,0}}), "W2: basic");
        assertEquals(1, Warmup02Sol.solve(new int[][]{{0,1},{0,0}}), "W2: small");
        assertEquals(0, Warmup02Sol.solve(new int[][]{{1,0}}), "W2: start blocked");
        assertEquals(0, Warmup02Sol.solve(new int[][]{{0,0},{0,1}}), "W2: end blocked");
        assertEquals(6, Warmup02Sol.solve(new int[][]{{0,0,0},{0,0,0},{0,0,0}}), "W2: no obstacle");
        assertEquals(1, Warmup02Sol.solve(new int[][]{{0}}), "W2: single");
    }

    static void testW3() {
        assertEquals(7, Warmup03Sol.solve(new int[][]{{1,3,1},{1,5,1},{4,2,1}}), "W3: basic");
        assertEquals(6, Warmup03Sol.solve(new int[][]{{1,2,3}}), "W3: single row");
        assertEquals(6, Warmup03Sol.solve(new int[][]{{1},{2},{3}}), "W3: single col");
        assertEquals(5, Warmup03Sol.solve(new int[][]{{5}}), "W3: single cell");
        assertEquals(7, Warmup03Sol.solve(new int[][]{{1,2},{3,4}}), "W3: 2x2");
    }

    static void testW4() {
        assertEquals(11, Warmup04Sol.solve(new int[][]{{2},{3,4},{6,5,7},{4,1,8,3}}), "W4: basic");
        assertEquals(-10, Warmup04Sol.solve(new int[][]{{-10}}), "W4: single");
        assertEquals(-1, Warmup04Sol.solve(new int[][]{{-1},{2,3},{1,-1,-3}}), "W4: negative");
        assertEquals(3, Warmup04Sol.solve(new int[][]{{1},{2,3}}), "W4: two rows");
        assertEquals(0, Warmup04Sol.solve(new int[][]{{0},{0,0},{0,0,0}}), "W4: zeros");
    }

    static void testP1() {
        assertEquals(2, Practice01Sol.solve(new int[][]{{1,0,0,0},{0,0,0,0},{0,0,2,-1}}), "P1: basic");
        assertEquals(4, Practice01Sol.solve(new int[][]{{1,0,0,0},{0,0,0,0},{0,0,0,2}}), "P1: full");
        assertEquals(0, Practice01Sol.solve(new int[][]{{0,1},{2,0}}), "P1: no path");
        assertEquals(1, Practice01Sol.solve(new int[][]{{1,2}}), "P1: minimal");
    }

    static void testP2() {
        assertEquals(13, Practice02Sol.solve(new int[][]{{2,1,3},{6,5,4},{7,8,9}}), "P2: basic");
        assertEquals(-59, Practice02Sol.solve(new int[][]{{-19,57},{-40,-5}}), "P2: negative");
        assertEquals(-48, Practice02Sol.solve(new int[][]{{-48}}), "P2: single");
        assertEquals(3, Practice02Sol.solve(new int[][]{{1,1,1},{1,1,1},{1,1,1}}), "P2: all same");
        assertEquals(4, Practice02Sol.solve(new int[][]{{1,2},{3,4}}), "P2: 2x2");
    }

    static void testP3() {
        assertEquals(4, Practice03Sol.solve(new int[][]{{1,0,1,0,0},{1,0,1,1,1},{1,1,1,1,1},{1,0,0,1,0}}), "P3: basic");
        assertEquals(1, Practice03Sol.solve(new int[][]{{0,1},{1,0}}), "P3: diagonal");
        assertEquals(0, Practice03Sol.solve(new int[][]{{0}}), "P3: zero");
        assertEquals(4, Practice03Sol.solve(new int[][]{{1,1},{1,1}}), "P3: all ones");
        assertEquals(1, Practice03Sol.solve(new int[][]{{1}}), "P3: single one");
    }

    static void testP4() {
        assertEquals(24, Practice04Sol.solve(new int[][]{{3,1,1},{2,5,1},{1,5,5},{2,1,1}}), "P4: basic");
        assertEquals(28, Practice04Sol.solve(new int[][]{{1,0,0,0,0,0,1},{2,0,0,0,0,3,0},{2,0,9,0,0,0,0},{0,3,0,5,4,0,0},{1,0,2,3,0,0,6}}), "P4: large");
        assertEquals(4, Practice04Sol.solve(new int[][]{{1,1},{1,1}}), "P4: 2x2");
    }

    static void testP5() {
        assertEquals(15, Practice05Sol.solve(new int[][]{{0,1,1,1},{1,1,1,1},{0,1,1,1}}), "P5: basic");
        assertEquals(7, Practice05Sol.solve(new int[][]{{1,0,1},{1,1,0},{1,1,0}}), "P5: mixed");
        assertEquals(5, Practice05Sol.solve(new int[][]{{1,1},{1,1}}), "P5: all ones");
        assertEquals(0, Practice05Sol.solve(new int[][]{{0,0},{0,0}}), "P5: all zeros");
        assertEquals(1, Practice05Sol.solve(new int[][]{{1}}), "P5: single");
    }

    static void testC1() {
        assertEquals(7, Challenge01Sol.solve(new int[][]{{-2,-3,3},{-5,-10,1},{10,30,-5}}), "C1: basic");
        assertEquals(1, Challenge01Sol.solve(new int[][]{{0}}), "C1: zero");
        assertEquals(1, Challenge01Sol.solve(new int[][]{{100}}), "C1: positive");
        assertEquals(6, Challenge01Sol.solve(new int[][]{{-5}}), "C1: negative");
        assertEquals(6, Challenge01Sol.solve(new int[][]{{-2,-3,3}}), "C1: single row");
    }

    static void testC2() {
        assertEquals(6, Challenge02Sol.solve(new int[][]{{1,0,1,0,0},{1,0,1,1,1},{1,1,1,1,1},{1,0,0,1,0}}), "C2: basic");
        assertEquals(0, Challenge02Sol.solve(new int[][]{{0}}), "C2: zero");
        assertEquals(1, Challenge02Sol.solve(new int[][]{{1}}), "C2: one");
        assertEquals(4, Challenge02Sol.solve(new int[][]{{1,1},{1,1}}), "C2: all ones");
        assertEquals(3, Challenge02Sol.solve(new int[][]{{1,1,1,0,1}}), "C2: single row");
    }

    static void testC3() {
        assertEquals(210, Challenge03Sol.solve(new int[][]{{10,40,70},{20,50,80},{30,60,90}}), "C3: basic");
        assertEquals(11, Challenge03Sol.solve(new int[][]{{1,2,5},{3,1,1},{3,3,3}}), "C3: small");
        assertEquals(10, Challenge03Sol.solve(new int[][]{{10,10,10}}), "C3: single day");
        assertEquals(6, Challenge03Sol.solve(new int[][]{{1,2,3},{3,2,1}}), "C3: two days");
        assertEquals(15, Challenge03Sol.solve(new int[][]{{5,5,5},{5,5,5},{5,5,5}}), "C3: uniform");
    }

    static void testC4() {
        assertEquals(5, Challenge04Sol.solve(new int[][]{{0,1,-1},{1,0,-1},{1,1,1}}), "C4: basic");
        assertEquals(0, Challenge04Sol.solve(new int[][]{{1,1,-1},{1,-1,1},{-1,1,1}}), "C4: blocked");
        assertEquals(1, Challenge04Sol.solve(new int[][]{{1}}), "C4: single");
        assertEquals(0, Challenge04Sol.solve(new int[][]{{0,0},{0,0}}), "C4: no cherries");
        assertEquals(4, Challenge04Sol.solve(new int[][]{{1,1},{1,1}}), "C4: all cherries");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 24: Dynamic Programming II — Grids and Paths");
        System.out.println("=====================================================\n");

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
