package ch31.tests;

import java.util.*;
import ch31.solutions.*;

/**
 * Tests for Chapter 31: Advanced DP — Bitmask, Interval, Trees
 *
 * Build and run:
 *   cd code/java
 *   javac ch31/tests/TestCh31.java
 *   java -ea ch31.tests.TestCh31
 */
public class TestCh31 {

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
        assertEquals(80, Warmup01Sol.solve(4, new int[][]{{0,10,15,20},{10,0,35,25},{15,35,0,30},{20,25,30,0}}), "W1: four cities");
        assertEquals(23, Warmup01Sol.solve(3, new int[][]{{0,1,15},{1,0,7},{15,7,0}}), "W1: three cities");
        assertEquals(10, Warmup01Sol.solve(2, new int[][]{{0,5},{5,0}}), "W1: two cities");
        assertEquals(4, Warmup01Sol.solve(4, new int[][]{{0,1,1,1},{1,0,1,1},{1,1,0,1},{1,1,1,0}}), "W1: symmetric");
    }

    static void testW2() {
        assertEquals(4500, Warmup02Sol.solve(new int[]{10,30,5,60}), "W2: three matrices");
        assertEquals(26000, Warmup02Sol.solve(new int[]{40,20,30,10,30}), "W2: four matrices");
        assertEquals(6000, Warmup02Sol.solve(new int[]{10,20,30}), "W2: two matrices");
        assertEquals(0, Warmup02Sol.solve(new int[]{5,10}), "W2: single matrix");
    }

    static void testW3() {
        assertEquals(7, Warmup03Sol.solve(4, new int[]{1,2,3,4}, new int[][]{{0,1},{0,2},{1,3}}), "W3: four nodes");
        assertEquals(8, Warmup03Sol.solve(3, new int[]{1,3,5}, new int[][]{{0,1},{0,2}}), "W3: three nodes");
        assertEquals(10, Warmup03Sol.solve(1, new int[]{10}, new int[][]{}), "W3: single");
        assertEquals(10, Warmup03Sol.solve(4, new int[]{3,4,5,6}, new int[][]{{0,1},{1,2},{2,3}}), "W3: chain");
    }

    static void testP1() {
        assertEquals(50, Practice01Sol.solve(4, new int[][]{{0,10,15,20},{10,0,35,25},{15,35,0,30},{20,25,30,0}}), "P1: four cities");
        assertEquals(8, Practice01Sol.solve(3, new int[][]{{0,1,15},{1,0,7},{15,7,0}}), "P1: three cities");
        assertEquals(5, Practice01Sol.solve(2, new int[][]{{0,5},{5,0}}), "P1: two cities");
    }

    static void testP2() {
        assertEquals(167, Practice02Sol.solve(new int[]{3,1,5,8}), "P2: four balloons");
        assertEquals(10, Practice02Sol.solve(new int[]{1,5}), "P2: two balloons");
        assertEquals(7, Practice02Sol.solve(new int[]{7}), "P2: single");
    }

    static void testP3() {
        assertEquals(6, Practice03Sol.solve(new int[]{1,2,3}), "P3: triangle");
        assertEquals(144, Practice03Sol.solve(new int[]{3,7,4,5}), "P3: square");
        assertEquals(13, Practice03Sol.solve(new int[]{1,3,1,4,1,5}), "P3: hexagon");
    }

    static void testP4() {
        assertEquals(3, Practice04Sol.solve(5, new int[][]{{0,1},{1,2},{1,3},{3,4}}), "P4: five nodes");
        assertEquals(1, Practice04Sol.solve(2, new int[][]{{0,1}}), "P4: two nodes");
        assertEquals(0, Practice04Sol.solve(1, new int[][]{}), "P4: single");
        assertEquals(2, Practice04Sol.solve(5, new int[][]{{0,1},{0,2},{0,3},{0,4}}), "P4: star");
    }

    static void testP5() {
        assertEquals(19, Practice05Sol.solve(20), "P5: twenty");
        assertEquals(90, Practice05Sol.solve(100), "P5: hundred");
        assertEquals(10, Practice05Sol.solve(10), "P5: ten");
        assertEquals(1, Practice05Sol.solve(1), "P5: one");
    }

    static void testC1() {
        assertEquals(20, Challenge01Sol.solve(new int[]{3,2,4,1}, 2), "C1: k=2");
        assertEquals(25, Challenge01Sol.solve(new int[]{3,5,1,2,6}, 3), "C1: k=3");
        assertEquals(-1, Challenge01Sol.solve(new int[]{3,2,4,1}, 3), "C1: impossible");
        assertEquals(0, Challenge01Sol.solve(new int[]{5}, 2), "C1: single");
    }

    static void testC2() {
        assertEquals(2, Challenge02Sol.solve(2, new int[][]{{1,2},{1,2}}), "C2: two same");
        assertEquals(4, Challenge02Sol.solve(2, new int[][]{{1,2,3},{1,2}}), "C2: two diff");
        assertEquals(1, Challenge02Sol.solve(1, new int[][]{{1}}), "C2: single");
        assertEquals(4, Challenge02Sol.solve(3, new int[][]{{1,2},{2,3},{3,4}}), "C2: three people");
    }

    static void testC3() {
        assertEquals(2, Challenge03Sol.solve(5, new int[][]{{0,1},{0,2},{1,3},{1,4}}), "C3: five nodes");
        assertEquals(1, Challenge03Sol.solve(3, new int[][]{{0,1},{1,2}}), "C3: chain");
        assertEquals(1, Challenge03Sol.solve(1, new int[][]{}), "C3: single");
        assertEquals(1, Challenge03Sol.solve(2, new int[][]{{0,1}}), "C3: two nodes");
    }

    static void testC4() {
        assertEquals(1, Challenge04Sol.solve("aab"), "C4: aab");
        assertEquals(0, Challenge04Sol.solve("a"), "C4: single");
        assertEquals(1, Challenge04Sol.solve("ab"), "C4: ab");
        assertEquals(1, Challenge04Sol.solve("aabb"), "C4: aabb");
        assertEquals(0, Challenge04Sol.solve("aba"), "C4: palindrome");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 31: Advanced DP — Bitmask, Interval, Trees");
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
