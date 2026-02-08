package ch20.tests;

import java.util.*;
import ch20.solutions.*;

/**
 * Tests for Chapter 20: Graphs II — Real Problems
 *
 * Build and run:
 *   cd code/java
 *   javac ch20/tests/TestCh20.java
 *   java -ea ch20.tests.TestCh20
 */
public class TestCh20 {

    static int passed = 0;
    static int failed = 0;

    static void assertEquals(int expected, int actual, String msg) {
        if (expected == actual) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assert2DEquals(int[][] expected, int[][] actual, String msg) {
        if (expected.length != actual.length) {
            failed++; System.out.println("FAIL: " + msg + " — row count mismatch"); return;
        }
        for (int i = 0; i < expected.length; i++) {
            if (!Arrays.equals(expected[i], actual[i])) {
                failed++; System.out.println("FAIL: " + msg + " — mismatch at row " + i
                    + ": expected " + Arrays.toString(expected[i]) + ", got " + Arrays.toString(actual[i])); return;
            }
        }
        passed++;
    }

    static void assert2DCharEquals(char[][] expected, char[][] actual, String msg) {
        if (expected.length != actual.length) {
            failed++; System.out.println("FAIL: " + msg + " — row count mismatch"); return;
        }
        for (int i = 0; i < expected.length; i++) {
            if (!Arrays.equals(expected[i], actual[i])) {
                failed++; System.out.println("FAIL: " + msg + " — mismatch at row " + i); return;
            }
        }
        passed++;
    }

    static void assertPacificAtlantic(int[][] expected, List<int[]> actual, String msg) {
        if (expected.length != actual.size()) {
            failed++; System.out.println("FAIL: " + msg + " — size mismatch: expected " + expected.length + ", got " + actual.size()); return;
        }
        // Sort both
        Arrays.sort(expected, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        actual.sort((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        for (int i = 0; i < expected.length; i++) {
            if (expected[i][0] != actual.get(i)[0] || expected[i][1] != actual.get(i)[1]) {
                failed++; System.out.println("FAIL: " + msg + " — mismatch at index " + i); return;
            }
        }
        passed++;
    }

    // ── W1: Flood Fill ──
    static void testW1() {
        assert2DEquals(new int[][]{{2,2,2},{2,2,0},{2,0,1}},
            Warmup01Sol.solve(new int[][]{{1,1,1},{1,1,0},{1,0,1}}, 1, 1, 2), "W1 basic");
        assert2DEquals(new int[][]{{0,0,0},{0,0,0}},
            Warmup01Sol.solve(new int[][]{{0,0,0},{0,0,0}}, 0, 0, 0), "W1 same color");
        assert2DEquals(new int[][]{{3}},
            Warmup01Sol.solve(new int[][]{{5}}, 0, 0, 3), "W1 single");
        assert2DEquals(new int[][]{{7,7},{7,7}},
            Warmup01Sol.solve(new int[][]{{1,1},{1,1}}, 0, 0, 7), "W1 all connected");
    }

    // ── W2: Number of Islands ──
    static void testW2() {
        assertEquals(3, Warmup02Sol.solve(new int[][]{{1,1,0,0,0},{1,1,0,0,0},{0,0,1,0,0},{0,0,0,1,1}}), "W2 three islands");
        assertEquals(1, Warmup02Sol.solve(new int[][]{{1,1,1},{0,1,0},{1,1,1}}), "W2 one island");
        assertEquals(0, Warmup02Sol.solve(new int[][]{{0,0},{0,0}}), "W2 no islands");
        assertEquals(2, Warmup02Sol.solve(new int[][]{{1,0},{0,1}}), "W2 diagonal");
    }

    // ── W3: Max Area of Island ──
    static void testW3() {
        assertEquals(5, Warmup03Sol.solve(new int[][]{{0,0,1,0,0},{0,0,1,0,0},{0,1,1,0,1},{0,0,1,0,0}}), "W3 basic");
        assertEquals(0, Warmup03Sol.solve(new int[][]{{0,0,0,0}}), "W3 no island");
        assertEquals(4, Warmup03Sol.solve(new int[][]{{1,1},{1,1}}), "W3 all land");
        assertEquals(1, Warmup03Sol.solve(new int[][]{{1}}), "W3 single");
    }

    // ── W4: Surrounded Regions ──
    static void testW4() {
        char[][] b1 = {{'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'}};
        assert2DCharEquals(new char[][]{{'X','X','X','X'},{'X','X','X','X'},{'X','X','X','X'},{'X','O','X','X'}},
            Warmup04Sol.solve(b1), "W4 basic");
        char[][] b2 = {{'O','O'},{'O','O'}};
        assert2DCharEquals(new char[][]{{'O','O'},{'O','O'}}, Warmup04Sol.solve(b2), "W4 all O border");
        char[][] b3 = {{'X','X','X','X','X'},{'X','O','O','O','X'},{'X','O','X','O','X'},{'X','O','O','O','X'},{'X','X','X','X','X'}};
        assert2DCharEquals(new char[][]{{'X','X','X','X','X'},{'X','X','X','X','X'},{'X','X','X','X','X'},{'X','X','X','X','X'},{'X','X','X','X','X'}},
            Warmup04Sol.solve(b3), "W4 inner surrounded");
    }

    // ── P1: Rotten Oranges ──
    static void testP1() {
        assertEquals(4, Practice01Sol.solve(new int[][]{{2,1,1},{1,1,0},{0,1,1}}), "P1 basic");
        assertEquals(-1, Practice01Sol.solve(new int[][]{{2,1,1},{0,1,1},{1,0,1}}), "P1 impossible");
        assertEquals(0, Practice01Sol.solve(new int[][]{{0,2}}), "P1 no fresh");
        assertEquals(2, Practice01Sol.solve(new int[][]{{2,1,1},{1,1,1},{1,1,2}}), "P1 multi source");
    }

    // ── P2: 01 Matrix ──
    static void testP2() {
        assert2DEquals(new int[][]{{0,0,0},{0,1,0},{0,0,0}},
            Practice02Sol.solve(new int[][]{{0,0,0},{0,1,0},{0,0,0}}), "P2 center");
        assert2DEquals(new int[][]{{0,0,0},{0,1,0},{1,2,1}},
            Practice02Sol.solve(new int[][]{{0,0,0},{0,1,0},{1,1,1}}), "P2 bottom");
        assert2DEquals(new int[][]{{2,1,2},{1,0,1},{2,1,2}},
            Practice02Sol.solve(new int[][]{{1,1,1},{1,0,1},{1,1,1}}), "P2 single zero");
    }

    // ── P3: Pacific Atlantic ──
    static void testP3() {
        int[][] h = {{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}};
        int[][] exp = {{0,4},{1,3},{1,4},{2,2},{3,0},{3,1},{4,0}};
        assertPacificAtlantic(exp, Practice03Sol.solve(h), "P3 basic");
        assertPacificAtlantic(new int[][]{{0,0}}, Practice03Sol.solve(new int[][]{{1}}), "P3 single");
    }

    // ── P4: Shortest Path Binary Matrix ──
    static void testP4() {
        assertEquals(2, Practice04Sol.solve(new int[][]{{0,1},{1,0}}), "P4 2x2");
        assertEquals(4, Practice04Sol.solve(new int[][]{{0,0,0},{1,1,0},{1,1,0}}), "P4 3x3");
        assertEquals(-1, Practice04Sol.solve(new int[][]{{1,0,0},{1,1,0},{1,1,0}}), "P4 blocked");
        assertEquals(1, Practice04Sol.solve(new int[][]{{0}}), "P4 single");
    }

    // ── P5: Number of Enclaves ──
    static void testP5() {
        assertEquals(3, Practice05Sol.solve(new int[][]{{0,0,0,0},{1,0,1,0},{0,1,1,0},{0,0,0,0}}), "P5 basic");
        assertEquals(0, Practice05Sol.solve(new int[][]{{0,1,1,0},{0,0,1,0},{0,0,1,0},{0,0,0,0}}), "P5 no enclaves");
        assertEquals(1, Practice05Sol.solve(new int[][]{{0,0,0},{0,1,0},{0,0,0}}), "P5 single enclave");
    }

    // ── C1: Walls and Gates ──
    static void testC1() {
        int INF = 2147483647;
        assert2DEquals(new int[][]{{3,-1,0,1},{2,2,1,-1},{1,-1,2,-1},{0,-1,3,4}},
            Challenge01Sol.solve(new int[][]{{INF,-1,0,INF},{INF,INF,INF,-1},{INF,-1,INF,-1},{0,-1,INF,INF}}), "C1 basic");
        assert2DEquals(new int[][]{{0,1},{1,2}},
            Challenge01Sol.solve(new int[][]{{0,INF},{INF,INF}}), "C1 single gate");
    }

    // ── C2: Shortest Bridge ──
    static void testC2() {
        assertEquals(1, Challenge02Sol.solve(new int[][]{{0,1},{1,0}}), "C2 diagonal");
        assertEquals(2, Challenge02Sol.solve(new int[][]{{0,1,0},{0,0,0},{0,0,1}}), "C2 separated");
        assertEquals(1, Challenge02Sol.solve(new int[][]{{1,1,1,1,1},{1,0,0,0,1},{1,0,1,0,1},{1,0,0,0,1},{1,1,1,1,1}}), "C2 concentric");
    }

    // ── C3: Making a Large Island ──
    static void testC3() {
        assertEquals(3, Challenge03Sol.solve(new int[][]{{1,0},{0,1}}), "C3 diagonal");
        assertEquals(4, Challenge03Sol.solve(new int[][]{{1,1},{1,0}}), "C3 almost full");
        assertEquals(4, Challenge03Sol.solve(new int[][]{{1,1},{1,1}}), "C3 full");
        assertEquals(5, Challenge03Sol.solve(new int[][]{{1,0,1},{1,0,1},{0,0,0}}), "C3 bridge");
    }

    // ── C4: Swim in Rising Water ──
    static void testC4() {
        assertEquals(3, Challenge04Sol.solve(new int[][]{{0,2},{1,3}}), "C4 2x2");
        assertEquals(16, Challenge04Sol.solve(new int[][]{{0,1,2,3,4},{24,23,22,21,5},{12,13,14,15,16},{11,17,18,19,20},{10,9,8,7,6}}), "C4 5x5");
        assertEquals(0, Challenge04Sol.solve(new int[][]{{0}}), "C4 1x1");
    }

    public static void main(String[] args) {
        testW1(); testW2(); testW3(); testW4();
        testP1(); testP2(); testP3(); testP4(); testP5();
        testC1(); testC2(); testC3(); testC4();

        System.out.println("\n========================================");
        System.out.println("Chapter 20 Java Tests: " + passed + " passed, " + failed + " failed");
        if (failed == 0)
            System.out.println("All ch20 tests passed!");
        else
            System.exit(1);
    }
}
