package ch29.tests;

import java.util.*;
import ch29.solutions.*;

/**
 * Tests for Chapter 29: Union-Find & Minimum Spanning Trees
 *
 * Build and run:
 *   cd code/java
 *   javac ch29/tests/TestCh29.java
 *   java -ea ch29.tests.TestCh29
 */
public class TestCh29 {

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

    static void assertStringEquals(String expected, String actual, String msg) {
        if (expected.equals(actual)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected '" + expected + "', got '" + actual + "'");
        }
    }

    static void assertListEquals(List<Integer> expected, List<Integer> actual, String msg) {
        if (expected.equals(actual)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual);
        }
    }

    // ── Tests ───────────────────────────────────────────────────────

    static void testW1() {
        assertEquals(2, Warmup01Sol.solve(5, new int[][]{{0,1},{1,2},{3,4}}), "W1: two components");
        assertEquals(5, Warmup01Sol.solve(5, new int[][]{}), "W1: all isolated");
        assertEquals(1, Warmup01Sol.solve(4, new int[][]{{0,1},{1,2},{2,3}}), "W1: single chain");
        assertEquals(1, Warmup01Sol.solve(3, new int[][]{{0,1},{0,2},{1,2}}), "W1: with cycle");
    }

    static void testW2() {
        assertArrayEquals(new int[]{2,3}, Warmup02Sol.solve(new int[][]{{1,2},{1,3},{2,3}}), "W2: triangle");
        assertArrayEquals(new int[]{1,4}, Warmup02Sol.solve(new int[][]{{1,2},{2,3},{3,4},{1,4},{1,5}}), "W2: longer");
    }

    static void testW3() {
        assertEquals(19, Warmup03Sol.solve(4, new int[][]{{0,1,10},{0,2,6},{0,3,5},{1,3,15},{2,3,4}}), "W3: basic");
        assertEquals(3, Warmup03Sol.solve(3, new int[][]{{0,1,1},{1,2,2},{0,2,3}}), "W3: triangle");
        assertEquals(0, Warmup03Sol.solve(1, new int[][]{}), "W3: single node");
    }

    static void testW4() {
        assertEquals(19, Warmup04Sol.solve(4, new int[][]{{0,1,10},{0,2,6},{0,3,5},{1,3,15},{2,3,4}}), "W4: basic");
        assertEquals(3, Warmup04Sol.solve(3, new int[][]{{0,1,1},{1,2,2},{0,2,3}}), "W4: triangle");
        assertEquals(0, Warmup04Sol.solve(1, new int[][]{}), "W4: single node");
    }

    static void testP1() {
        assertEquals(2, Practice01Sol.solve(new int[][]{{1,1,0},{1,1,0},{0,0,1}}), "P1: two provinces");
        assertEquals(3, Practice01Sol.solve(new int[][]{{1,0,0},{0,1,0},{0,0,1}}), "P1: all isolated");
        assertEquals(1, Practice01Sol.solve(new int[][]{{1,1,1},{1,1,1},{1,1,1}}), "P1: all connected");
    }

    static void testP2() {
        List<List<String>> accounts = new ArrayList<>();
        accounts.add(Arrays.asList("John","j1@m","j2@m"));
        accounts.add(Arrays.asList("John","j1@m","j3@m"));
        accounts.add(Arrays.asList("Mary","m1@m"));
        List<List<String>> result = Practice02Sol.solve(accounts);
        // Check sizes
        assertEquals(2, result.size(), "P2: account count");
        if (result.size() == 2) {
            assertEquals(4, result.get(0).size(), "P2: first account size (name + 3 emails)");
            assertEquals(2, result.get(1).size(), "P2: second account size (name + 1 email)");
        }
    }

    static void testP3() {
        assertEquals(5, Practice03Sol.solve(new int[][]{{0,0},{0,1},{1,0},{1,2},{2,1},{2,2}}), "P3: grid");
        assertEquals(3, Practice03Sol.solve(new int[][]{{0,0},{0,2},{1,1},{2,0},{2,2}}), "P3: diagonal");
        assertEquals(0, Practice03Sol.solve(new int[][]{{0,0}}), "P3: single");
    }

    static void testP4() {
        assertEquals(20, Practice04Sol.solve(new int[][]{{0,0},{2,2},{3,10},{5,2},{7,0}}), "P4: basic");
        assertEquals(18, Practice04Sol.solve(new int[][]{{3,12},{-2,5},{-4,1}}), "P4: three points");
        assertEquals(0, Practice04Sol.solve(new int[][]{{0,0}}), "P4: single point");
    }

    static void testP5() {
        assertBoolEquals(false, Practice05Sol.solve(new String[]{"a==b","b!=a"}), "P5: contradiction");
        assertBoolEquals(true, Practice05Sol.solve(new String[]{"b==a","a==b"}), "P5: consistent");
        assertBoolEquals(true, Practice05Sol.solve(new String[]{"a==b","b==c","a==c"}), "P5: transitive");
        assertBoolEquals(false, Practice05Sol.solve(new String[]{"a==b","b!=c","c==a"}), "P5: transitive contradiction");
    }

    static void testC1() {
        assertEquals(1, Challenge01Sol.solve(4, new int[][]{{0,1},{0,2},{1,2}}), "C1: one spare");
        assertEquals(2, Challenge01Sol.solve(6, new int[][]{{0,1},{0,2},{0,3},{1,2},{1,3}}), "C1: two spare");
        assertEquals(-1, Challenge01Sol.solve(4, new int[][]{{0,1},{0,2}}), "C1: impossible");
    }

    static void testC2() {
        assertEquals(3, Challenge02Sol.solve(new int[][]{{1,0},{0,1}}), "C2: diagonal");
        assertEquals(4, Challenge02Sol.solve(new int[][]{{1,1},{1,0}}), "C2: one zero");
        assertEquals(4, Challenge02Sol.solve(new int[][]{{1,1},{1,1}}), "C2: all ones");
    }

    static void testC3() {
        assertListEquals(Arrays.asList(1,1,2,3),
            Challenge03Sol.solve(3, 3, new int[][]{{0,0},{0,1},{1,2},{2,1}}), "C3: basic");
        assertListEquals(Arrays.asList(1),
            Challenge03Sol.solve(1, 1, new int[][]{{0,0}}), "C3: single");
    }

    static void testC4() {
        List<int[]> pairs1 = Arrays.asList(new int[]{0,3}, new int[]{1,2});
        assertStringEquals("bacd", Challenge04Sol.solve("dcab", pairs1), "C4: two groups");
        List<int[]> pairs2 = Arrays.asList(new int[]{0,3}, new int[]{1,2}, new int[]{0,2});
        assertStringEquals("abcd", Challenge04Sol.solve("dcab", pairs2), "C4: all connected");
        List<int[]> pairs3 = Arrays.asList(new int[]{0,1}, new int[]{1,2});
        assertStringEquals("abc", Challenge04Sol.solve("cba", pairs3), "C4: chain");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 29: Union-Find & Minimum Spanning Trees");
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
