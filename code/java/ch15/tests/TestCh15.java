package ch15.tests;

import java.util.*;
import ch15.solutions.*;

/**
 * Tests for Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * Build and run:
 *   cd code/java
 *   javac -cp . ch15/tests/TestCh15.java ch15/solutions/*.java
 *   java -ea ch15.tests.TestCh15
 */
public class TestCh15 {

    static int passed = 0;
    static int failed = 0;

    static void assertEquals(int expected, int actual, String msg) {
        if (expected == actual) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertArrayEquals(int[] expected, int[] actual, String msg) {
        if (Arrays.equals(expected, actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected) + ", got " + Arrays.toString(actual)); }
    }

    static void assertStringEquals(String expected, String actual, String msg) {
        if (expected.equals(actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected \"" + expected + "\", got \"" + actual + "\""); }
    }

    static void assertListEquals(List<List<Integer>> expected, List<List<Integer>> actual, String msg) {
        if (expected.equals(actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    // ── W1: Pair Sum in Sorted Array ─────────────────────────────────

    static void testW1() {
        assertArrayEquals(new int[]{1, 12}, Warmup01Sol.solve(new int[]{1,3,5,8,12,15}, 13), "W1: basic");
        assertArrayEquals(new int[]{1, 5}, Warmup01Sol.solve(new int[]{1,2,3,4,5}, 6), "W1: first+last");
        assertArrayEquals(new int[]{-1, -1}, Warmup01Sol.solve(new int[]{1,2,3,4,5}, 10), "W1: no pair");
        assertArrayEquals(new int[]{3, 7}, Warmup01Sol.solve(new int[]{3,7}, 10), "W1: two elements");
        assertArrayEquals(new int[]{-5, -3}, Warmup01Sol.solve(new int[]{-5,-3,0,2,8}, -8), "W1: negatives");
        assertArrayEquals(new int[]{-1, -1}, Warmup01Sol.solve(new int[]{}, 5), "W1: empty");
        assertArrayEquals(new int[]{-1, -1}, Warmup01Sol.solve(new int[]{5}, 5), "W1: single");
        assertArrayEquals(new int[]{1, 9}, Warmup01Sol.solve(new int[]{1,3,5,7,9}, 10), "W1: smallest first");
    }

    // ── W2: Remove Duplicates from Sorted ────────────────────────────

    static void testW2() {
        assertArrayEquals(new int[]{1, 2}, Warmup02Sol.solve(new int[]{1,1,2}), "W2: basic");
        assertArrayEquals(new int[]{0,1,2,3,4}, Warmup02Sol.solve(new int[]{0,0,1,1,1,2,2,3,3,4}), "W2: many dupes");
        assertArrayEquals(new int[]{1,2,3}, Warmup02Sol.solve(new int[]{1,2,3}), "W2: no dupes");
        assertArrayEquals(new int[]{5}, Warmup02Sol.solve(new int[]{5,5,5,5}), "W2: all same");
        assertArrayEquals(new int[]{1}, Warmup02Sol.solve(new int[]{1}), "W2: single");
        assertArrayEquals(new int[]{}, Warmup02Sol.solve(new int[]{}), "W2: empty");
        assertArrayEquals(new int[]{-3,-1,0,2}, Warmup02Sol.solve(new int[]{-3,-3,-1,0,0,2}), "W2: negatives");
    }

    // ── W3: Max Sum of Fixed Window ──────────────────────────────────

    static void testW3() {
        assertEquals(9, Warmup03Sol.solve(new int[]{2,1,5,1,3,2}, 3), "W3: basic");
        assertEquals(6, Warmup03Sol.solve(new int[]{1,2,3}, 3), "W3: k==len");
        assertEquals(0, Warmup03Sol.solve(new int[]{1,2}, 3), "W3: k>len");
        assertEquals(5, Warmup03Sol.solve(new int[]{5}, 1), "W3: single");
        assertEquals(-3, Warmup03Sol.solve(new int[]{-1,-2,-3,-4}, 2), "W3: all neg");
        assertEquals(9, Warmup03Sol.solve(new int[]{4,-1,2,1,6,-5}, 3), "W3: mixed");
        assertEquals(0, Warmup03Sol.solve(new int[]{}, 1), "W3: empty");
    }

    // ── W4: Move Zeros to End ────────────────────────────────────────

    static void testW4() {
        assertArrayEquals(new int[]{1,3,12,0,0}, Warmup04Sol.solve(new int[]{0,1,0,3,12}), "W4: basic");
        assertArrayEquals(new int[]{0}, Warmup04Sol.solve(new int[]{0}), "W4: single zero");
        assertArrayEquals(new int[]{1,2,3}, Warmup04Sol.solve(new int[]{1,2,3}), "W4: no zeros");
        assertArrayEquals(new int[]{0,0,0}, Warmup04Sol.solve(new int[]{0,0,0}), "W4: all zeros");
        assertArrayEquals(new int[]{1,0,0}, Warmup04Sol.solve(new int[]{0,0,1}), "W4: zeros at start");
        assertArrayEquals(new int[]{}, Warmup04Sol.solve(new int[]{}), "W4: empty");
        assertArrayEquals(new int[]{5,3,1,0,0,0}, Warmup04Sol.solve(new int[]{0,5,0,3,0,1}), "W4: mixed");
    }

    // ── P1: Container With Most Water ────────────────────────────────

    static void testP1() {
        assertEquals(49, Practice01Sol.solve(new int[]{1,8,6,2,5,4,8,3,7}), "P1: basic");
        assertEquals(1, Practice01Sol.solve(new int[]{1,1}), "P1: two elements");
        assertEquals(4, Practice01Sol.solve(new int[]{4,3,2,1}), "P1: decreasing");
        assertEquals(4, Practice01Sol.solve(new int[]{1,2,3,4}), "P1: increasing");
        assertEquals(15, Practice01Sol.solve(new int[]{5,5,5,5}), "P1: equal");
        assertEquals(40, Practice01Sol.solve(new int[]{10,1,1,1,10}), "P1: tall ends");
    }

    // ── P2: Longest Substring Without Repeating ──────────────────────

    static void testP2() {
        assertEquals(3, Practice02Sol.solve("abcabcbb"), "P2: basic");
        assertEquals(1, Practice02Sol.solve("bbbbb"), "P2: all same");
        assertEquals(3, Practice02Sol.solve("pwwkew"), "P2: alternating");
        assertEquals(0, Practice02Sol.solve(""), "P2: empty");
        assertEquals(1, Practice02Sol.solve("a"), "P2: single");
        assertEquals(6, Practice02Sol.solve("abcdef"), "P2: all unique");
        assertEquals(5, Practice02Sol.solve("ab cd"), "P2: with space");
    }

    // ── P3: Minimum Window Substring ─────────────────────────────────

    static void testP3() {
        assertStringEquals("BANC", Practice03Sol.solve("ADOBECODEBANC", "ABC"), "P3: basic");
        assertStringEquals("a", Practice03Sol.solve("a", "a"), "P3: exact");
        assertStringEquals("", Practice03Sol.solve("a", "aa"), "P3: no window");
        assertStringEquals("", Practice03Sol.solve("ab", "abc"), "P3: t longer");
        assertStringEquals("abc", Practice03Sol.solve("abc", "abc"), "P3: entire string");
        assertStringEquals("AAB", Practice03Sol.solve("AABC", "AAB"), "P3: dupes in t");
        assertStringEquals("", Practice03Sol.solve("", "a"), "P3: empty s");
    }

    // ── P4: Subarray Sum Equals K ────────────────────────────────────

    static void testP4() {
        assertEquals(2, Practice04Sol.solve(new int[]{1,1,1}, 2), "P4: basic");
        assertEquals(2, Practice04Sol.solve(new int[]{1,2,3}, 3), "P4: exact");
        assertEquals(1, Practice04Sol.solve(new int[]{5}, 5), "P4: single match");
        assertEquals(0, Practice04Sol.solve(new int[]{1,2,3}, 10), "P4: no match");
        assertEquals(3, Practice04Sol.solve(new int[]{1,1,1,1,1}, 3), "P4: all ones");
        assertEquals(2, Practice04Sol.solve(new int[]{2,3,1,2,4,3}, 7), "P4: larger");
    }

    // ── P5: Dutch National Flag ──────────────────────────────────────

    static void testP5() {
        assertArrayEquals(new int[]{0,0,1,1,2,2}, Practice05Sol.solve(new int[]{2,0,2,1,1,0}), "P5: basic");
        assertArrayEquals(new int[]{0,1,2}, Practice05Sol.solve(new int[]{2,0,1}), "P5: three");
        assertArrayEquals(new int[]{0,0,1,1,2,2}, Practice05Sol.solve(new int[]{0,0,1,1,2,2}), "P5: already sorted");
        assertArrayEquals(new int[]{0,0,1,1,2,2}, Practice05Sol.solve(new int[]{2,2,1,1,0,0}), "P5: reverse");
        assertArrayEquals(new int[]{1,1,1}, Practice05Sol.solve(new int[]{1,1,1}), "P5: all same");
        assertArrayEquals(new int[]{0}, Practice05Sol.solve(new int[]{0}), "P5: single");
        assertArrayEquals(new int[]{}, Practice05Sol.solve(new int[]{}), "P5: empty");
        assertArrayEquals(new int[]{0,0,2,2}, Practice05Sol.solve(new int[]{2,0,2,0}), "P5: no ones");
    }

    // ── C1: Three Sum ────────────────────────────────────────────────

    static void testC1() {
        assertListEquals(
            Arrays.asList(Arrays.asList(-1,-1,2), Arrays.asList(-1,0,1)),
            Challenge01Sol.solve(new int[]{-1,0,1,2,-1,-4}), "C1: basic");
        assertListEquals(new ArrayList<>(),
            Challenge01Sol.solve(new int[]{0,1,1}), "C1: no triplet");
        assertListEquals(Arrays.asList(Arrays.asList(0,0,0)),
            Challenge01Sol.solve(new int[]{0,0,0}), "C1: all zeros");
        assertListEquals(Arrays.asList(Arrays.asList(0,0,0)),
            Challenge01Sol.solve(new int[]{0,0,0,0}), "C1: four zeros");
        assertListEquals(new ArrayList<>(),
            Challenge01Sol.solve(new int[]{1,2,3}), "C1: no result");

        List<List<Integer>> result = Challenge01Sol.solve(new int[]{-2,-1,0,1,2,3});
        assertEquals(3, result.size(), "C1: multiple triplets count");
    }

    // ── C2: Trapping Rain Water ──────────────────────────────────────

    static void testC2() {
        assertEquals(6, Challenge02Sol.solve(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}), "C2: basic");
        assertEquals(9, Challenge02Sol.solve(new int[]{4,2,0,3,2,5}), "C2: v shape");
        assertEquals(0, Challenge02Sol.solve(new int[]{3,3,3}), "C2: flat");
        assertEquals(0, Challenge02Sol.solve(new int[]{1,2,3,4}), "C2: ascending");
        assertEquals(0, Challenge02Sol.solve(new int[]{4,3,2,1}), "C2: descending");
        assertEquals(0, Challenge02Sol.solve(new int[]{}), "C2: empty");
        assertEquals(0, Challenge02Sol.solve(new int[]{1,2}), "C2: two elements");
        assertEquals(0, Challenge02Sol.solve(new int[]{5}), "C2: single");
    }

    // ── C3: Longest Repeating Character Replacement ──────────────────

    static void testC3() {
        assertEquals(4, Challenge03Sol.solve("ABAB", 2), "C3: basic");
        assertEquals(4, Challenge03Sol.solve("AABABBA", 1), "C3: limited");
        assertEquals(4, Challenge03Sol.solve("AAAA", 0), "C3: no replacement");
        assertEquals(3, Challenge03Sol.solve("ABCDE", 2), "C3: all different");
        assertEquals(1, Challenge03Sol.solve("A", 0), "C3: single");
        assertEquals(2, Challenge03Sol.solve("AB", 2), "C3: k==len");
        assertEquals(5, Challenge03Sol.solve("AAABBC", 2), "C3: long run");
    }

    // ── C4: Fruit Into Baskets ───────────────────────────────────────

    static void testC4() {
        assertEquals(3, Challenge04Sol.solve(new int[]{1,2,1}), "C4: basic");
        assertEquals(3, Challenge04Sol.solve(new int[]{0,1,2,2}), "C4: three types");
        assertEquals(4, Challenge04Sol.solve(new int[]{1,2,3,2,2}), "C4: longer");
        assertEquals(4, Challenge04Sol.solve(new int[]{1,1,1,1}), "C4: single type");
        assertEquals(5, Challenge04Sol.solve(new int[]{1,2,1,2,1}), "C4: alternating");
        assertEquals(1, Challenge04Sol.solve(new int[]{5}), "C4: single");
        assertEquals(2, Challenge04Sol.solve(new int[]{1,2}), "C4: two");
        assertEquals(5, Challenge04Sol.solve(new int[]{3,3,3,1,2,1,1,2,3,3,4}), "C4: many types");
    }

    // ── Main ────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method");
        System.out.println("===================================================================\n");

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
