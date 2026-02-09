package ch33.tests;

import java.util.*;
import ch33.solutions.*;

/**
 * Tests for Chapter 33: Advanced Trees & Graph Algorithms
 *
 * Build and run:
 *   cd code/java
 *   javac ch33/tests/TestCh33.java
 *   java -ea ch33.tests.TestCh33
 */
public class TestCh33 {

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

    static void assertArray2DEquals(int[][] expected, int[][] actual, String msg) {
        if (Arrays.deepEquals(expected, actual)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + Arrays.deepToString(expected)
                + ", got " + Arrays.deepToString(actual));
        }
    }

    // ── Tests ───────────────────────────────────────────────────────

    static void testW1() {
        assertArrayEquals(new int[]{1, 0, 2},
            Warmup01Sol.solve(7, new int[][]{{0,1},{0,2},{1,3},{1,4},{2,5},{2,6}},
                new int[][]{{3,4},{3,6},{5,6}}), "W1: basic tree");
        assertArrayEquals(new int[]{1, 0},
            Warmup01Sol.solve(3, new int[][]{{0,1},{1,2}},
                new int[][]{{1,2},{0,2}}), "W1: chain");
        assertArrayEquals(new int[]{1},
            Warmup01Sol.solve(3, new int[][]{{0,1},{0,2}},
                new int[][]{{1,1}}), "W1: same node");
        assertArrayEquals(new int[]{0},
            Warmup01Sol.solve(3, new int[][]{{0,1},{0,2}},
                new int[][]{{1,2}}), "W1: root query");
    }

    static void testW2() {
        assertArrayEquals(new int[]{0,1,3,4,2},
            Warmup02Sol.solve(5, new int[][]{{0,1},{0,2},{1,3},{1,4}}), "W2: basic tree");
        assertArrayEquals(new int[]{0,1,2},
            Warmup02Sol.solve(3, new int[][]{{0,1},{0,2}}), "W2: small tree");
        assertArrayEquals(new int[]{0},
            Warmup02Sol.solve(1, new int[][]{}), "W2: single node");
        assertArrayEquals(new int[]{0,1,2,3},
            Warmup02Sol.solve(4, new int[][]{{0,1},{1,2},{2,3}}), "W2: chain");
    }

    static void testW3() {
        assertArray2DEquals(new int[][]{{1,3},{3,4}},
            Warmup03Sol.solve(5, new int[][]{{0,1},{1,2},{2,0},{1,3},{3,4}}), "W3: basic");
        assertArray2DEquals(new int[][]{},
            Warmup03Sol.solve(4, new int[][]{{0,1},{1,2},{2,3},{3,0}}), "W3: cycle no bridges");
        assertArray2DEquals(new int[][]{{0,1}},
            Warmup03Sol.solve(2, new int[][]{{0,1}}), "W3: single edge");
        assertArray2DEquals(new int[][]{{0,1},{1,2},{2,3}},
            Warmup03Sol.solve(4, new int[][]{{0,1},{1,2},{2,3}}), "W3: all bridges");
    }

    static void testP1() {
        assertArrayEquals(new int[]{1, 3},
            Practice01Sol.solve(5, new int[][]{{0,1},{1,2},{2,0},{1,3},{3,4}}), "P1: basic");
        assertArrayEquals(new int[]{},
            Practice01Sol.solve(4, new int[][]{{0,1},{1,2},{2,3},{3,0}}), "P1: cycle no ap");
        assertArrayEquals(new int[]{0},
            Practice01Sol.solve(5, new int[][]{{0,1},{0,2},{0,3},{0,4}}), "P1: star");
        assertArrayEquals(new int[]{1, 2},
            Practice01Sol.solve(4, new int[][]{{0,1},{1,2},{2,3}}), "P1: chain");
    }

    static void testP2() {
        assertEquals(3, Practice02Sol.solve(5, new int[][]{{0,1},{1,2},{2,0},{1,3},{3,4}}), "P2: basic");
        assertEquals(1, Practice02Sol.solve(4, new int[][]{{0,1},{1,2},{2,3},{3,0}}), "P2: single scc");
        assertEquals(3, Practice02Sol.solve(3, new int[][]{{0,1},{1,2}}), "P2: all separate");
        assertEquals(2, Practice02Sol.solve(4, new int[][]{{0,1},{1,0},{2,3},{3,2}}), "P2: two sccs");
    }

    static void testP3() {
        assertArrayEquals(new int[]{15, 11, 3},
            Practice03Sol.solve(5, new int[]{1,2,3,4,5}, new int[][]{{0,1},{0,2},{1,3},{1,4}}, new int[]{0,1,2}), "P3: basic");
        assertArrayEquals(new int[]{60, 20},
            Practice03Sol.solve(3, new int[]{10,20,30}, new int[][]{{0,1},{0,2}}, new int[]{0,1}), "P3: small");
        assertArrayEquals(new int[]{42},
            Practice03Sol.solve(1, new int[]{42}, new int[][]{}, new int[]{0}), "P3: single");
        assertArrayEquals(new int[]{10, 15},
            Practice03Sol.solve(3, new int[]{5,10,15}, new int[][]{{0,1},{0,2}}, new int[]{1,2}), "P3: leaf query");
    }

    static void testP4() {
        assertArrayEquals(new int[]{20, 10},
            Practice04Sol.solve(5, new int[]{10,20,30,40,50}, new int[][]{{0,1},{0,2},{1,3},{1,4}},
                new int[][]{{3,4},{3,2}}), "P4: basic");
        assertArrayEquals(new int[]{5},
            Practice04Sol.solve(3, new int[]{5,10,15}, new int[][]{{0,1},{0,2}},
                new int[][]{{1,2}}), "P4: small");
        assertArrayEquals(new int[]{10},
            Practice04Sol.solve(3, new int[]{5,10,15}, new int[][]{{0,1},{0,2}},
                new int[][]{{1,1}}), "P4: same node");
        assertArrayEquals(new int[]{100},
            Practice04Sol.solve(4, new int[]{100,200,300,400}, new int[][]{{0,1},{0,2},{2,3}},
                new int[][]{{1,3}}), "P4: root is lca");
    }

    static void testP5() {
        assertEquals(2, Practice05Sol.solve(7, new int[][]{{0,1},{1,2},{2,0},{3,4},{4,5},{5,3},{6,0}}), "P5: two large sccs");
        assertEquals(0, Practice05Sol.solve(4, new int[][]{{0,1},{1,2},{2,3}}), "P5: no large sccs");
        assertEquals(1, Practice05Sol.solve(3, new int[][]{{0,1},{1,0},{2,0}}), "P5: one large scc");
        assertEquals(1, Practice05Sol.solve(4, new int[][]{{0,1},{1,2},{2,3},{3,0}}), "P5: single big scc");
    }

    static void testC1() {
        assertArray2DEquals(new int[][]{{1,3}},
            Challenge01Sol.solve(4, new int[][]{{0,1},{1,2},{2,0},{1,3}}), "C1: basic");
        assertArray2DEquals(new int[][]{{2,4}},
            Challenge01Sol.solve(5, new int[][]{{0,1},{1,2},{2,3},{3,0},{2,4}}), "C1: two bridges");
        assertArray2DEquals(new int[][]{},
            Challenge01Sol.solve(3, new int[][]{{0,1},{1,2},{2,0}}), "C1: no bridges");
        assertArray2DEquals(new int[][]{{0,1},{1,2}},
            Challenge01Sol.solve(3, new int[][]{{0,1},{1,2}}), "C1: all bridges");
    }

    static void testC2() {
        assertEquals(3, Challenge02Sol.solve(6, new int[][]{{0,1},{1,3},{2,3},{4,0},{4,5}}), "C2: basic");
        assertEquals(0, Challenge02Sol.solve(3, new int[][]{{1,0},{2,0}}), "C2: all toward zero");
        assertEquals(2, Challenge02Sol.solve(3, new int[][]{{0,1},{0,2}}), "C2: all away");
        assertEquals(3, Challenge02Sol.solve(4, new int[][]{{0,1},{1,2},{2,3}}), "C2: chain");
    }

    static void testC3() {
        assertArrayEquals(new int[]{5, 9},
            Challenge03Sol.solve(5, new int[][]{{0,1,2},{0,2,3},{1,3,4},{1,4,1}},
                new int[][]{{3,4},{3,2}}), "C3: basic");
        assertArrayEquals(new int[]{15},
            Challenge03Sol.solve(3, new int[][]{{0,1,5},{0,2,10}},
                new int[][]{{1,2}}), "C3: simple");
        assertArrayEquals(new int[]{0},
            Challenge03Sol.solve(3, new int[][]{{0,1,5},{0,2,10}},
                new int[][]{{1,1}}), "C3: same node");
        assertArrayEquals(new int[]{7},
            Challenge03Sol.solve(2, new int[][]{{0,1,7}},
                new int[][]{{0,1}}), "C3: root query");
    }

    static void testC4() {
        assertEquals(1, Challenge04Sol.solve(6, new int[][]{{0,1},{1,2},{2,0},{3,4},{4,5},{5,3},{2,3}}), "C4: two sccs one edge");
        assertEquals(1, Challenge04Sol.solve(4, new int[][]{{0,1},{1,0},{2,3},{3,2},{1,2}}), "C4: two sccs connected");
        assertEquals(2, Challenge04Sol.solve(3, new int[][]{{0,1},{1,2}}), "C4: all separate");
        assertEquals(0, Challenge04Sol.solve(3, new int[][]{{0,1},{1,2},{2,0}}), "C4: single scc");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 33: Advanced Trees & Graph Algorithms");
        System.out.println("================================================================\n");

        testW1(); testW2(); testW3();
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
