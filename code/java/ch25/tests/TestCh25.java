package ch25.tests;

import java.util.*;
import ch25.solutions.*;

/**
 * Tests for Chapter 25: Dynamic Programming III — Subsequences & Knapsack
 *
 * Build and run:
 *   cd code/java
 *   javac ch25/tests/TestCh25.java
 *   java -ea ch25.tests.TestCh25
 */
public class TestCh25 {

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

    static boolean isSubsequence(String s, String t) {
        int si = 0;
        for (int ti = 0; ti < t.length() && si < s.length(); ti++)
            if (s.charAt(si) == t.charAt(ti)) si++;
        return si == s.length();
    }

    static void assertSCS(String str1, String str2, String result, int expectedLen, String msg) {
        if (result.length() == expectedLen && isSubsequence(str1, result) && isSubsequence(str2, result)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — got '" + result + "' (len " + result.length()
                + "), expected len " + expectedLen);
        }
    }

    // ── Tests ───────────────────────────────────────────────────────

    static void testW1() {
        assertEquals(9, Warmup01Sol.solve(new int[]{1,3,4,5}, new int[]{1,4,5,7}, 7), "W1: basic");
        assertEquals(7, Warmup01Sol.solve(new int[]{2,3,4,5}, new int[]{3,4,5,6}, 5), "W1: tight");
        assertEquals(0, Warmup01Sol.solve(new int[]{10}, new int[]{10}, 5), "W1: too heavy");
        assertEquals(10, Warmup01Sol.solve(new int[]{5}, new int[]{10}, 5), "W1: exact fit");
        assertEquals(0, Warmup01Sol.solve(new int[]{}, new int[]{}, 10), "W1: empty");
    }

    static void testW2() {
        assertBoolEquals(true, Warmup02Sol.solve(new int[]{3,34,4,12,5,2}, 9), "W2: basic true");
        assertBoolEquals(false, Warmup02Sol.solve(new int[]{3,34,4,12,5,2}, 30), "W2: basic false");
        assertBoolEquals(true, Warmup02Sol.solve(new int[]{1,5,11,5}, 11), "W2: sum 11");
        assertBoolEquals(true, Warmup02Sol.solve(new int[]{1,2,3}, 0), "W2: target 0");
        assertBoolEquals(true, Warmup02Sol.solve(new int[]{5}, 5), "W2: single match");
    }

    static void testW3() {
        assertEquals(3, Warmup03Sol.solve(new int[]{1,5,11}, 15), "W3: basic");
        assertEquals(-1, Warmup03Sol.solve(new int[]{2}, 3), "W3: impossible");
        assertEquals(0, Warmup03Sol.solve(new int[]{1}, 0), "W3: zero");
        assertEquals(3, Warmup03Sol.solve(new int[]{1,2,5}, 11), "W3: classic");
        assertEquals(5, Warmup03Sol.solve(new int[]{1}, 5), "W3: single coin");
    }

    static void testW4() {
        assertEquals(4, Warmup04Sol.solve(new int[]{1,2,5}, 5), "W4: basic");
        assertEquals(0, Warmup04Sol.solve(new int[]{2}, 3), "W4: impossible");
        assertEquals(1, Warmup04Sol.solve(new int[]{10}, 10), "W4: exact");
        assertEquals(1, Warmup04Sol.solve(new int[]{1,2}, 0), "W4: zero amount");
        assertEquals(1, Warmup04Sol.solve(new int[]{1}, 5), "W4: single coin");
    }

    static void testW5() {
        assertEquals(3, Warmup05Sol.solve("abcde", "ace"), "W5: basic");
        assertEquals(3, Warmup05Sol.solve("abc", "abc"), "W5: identical");
        assertEquals(0, Warmup05Sol.solve("abc", "def"), "W5: no common");
        assertEquals(2, Warmup05Sol.solve("oxcpqrsvwf", "shmtulqrypy"), "W5: longer");
    }

    static void testP1() {
        assertBoolEquals(true, Practice01Sol.solve(new int[]{1,5,11,5}), "P1: true");
        assertBoolEquals(false, Practice01Sol.solve(new int[]{1,2,3,5}), "P1: false");
        assertBoolEquals(true, Practice01Sol.solve(new int[]{1,1}), "P1: pair");
        assertBoolEquals(false, Practice01Sol.solve(new int[]{1}), "P1: single");
    }

    static void testP2() {
        assertEquals(27, Practice02Sol.solve(new int[]{2,4,6}, new int[]{5,11,13}, 10), "P2: basic");
        assertEquals(110, Practice02Sol.solve(new int[]{1,3,4,5}, new int[]{10,40,50,70}, 8), "P2: basic2");
        assertEquals(21, Practice02Sol.solve(new int[]{3}, new int[]{7}, 9), "P2: single item");
        assertEquals(0, Practice02Sol.solve(new int[]{10}, new int[]{100}, 5), "P2: no fit");
    }

    static void testP3() {
        assertEquals(3, Practice03Sol.solve("horse", "ros"), "P3: basic");
        assertEquals(5, Practice03Sol.solve("intention", "execution"), "P3: longer");
        assertEquals(3, Practice03Sol.solve("", "abc"), "P3: empty source");
        assertEquals(0, Practice03Sol.solve("abc", "abc"), "P3: identical");
        assertEquals(0, Practice03Sol.solve("", ""), "P3: both empty");
    }

    static void testP4() {
        assertEquals(4, Practice04Sol.solve(new int[]{10,9,2,5,3,7,101,18}), "P4: basic");
        assertEquals(4, Practice04Sol.solve(new int[]{0,1,0,3,2,3}), "P4: mixed");
        assertEquals(1, Practice04Sol.solve(new int[]{7,7,7,7,7}), "P4: all same");
        assertEquals(5, Practice04Sol.solve(new int[]{1,2,3,4,5}), "P4: increasing");
        assertEquals(1, Practice04Sol.solve(new int[]{5,4,3,2,1}), "P4: decreasing");
    }

    static void testP5() {
        assertEquals(3, Practice05Sol.solve("rabbbit", "rabbit"), "P5: rabbbit");
        assertEquals(5, Practice05Sol.solve("babgbag", "bag"), "P5: babgbag");
        assertEquals(3, Practice05Sol.solve("aaa", "a"), "P5: aaa");
        assertEquals(0, Practice05Sol.solve("abc", "d"), "P5: no match");
    }

    static void testP6() {
        assertBoolEquals(false, Practice06Sol.solve("aa", "a"), "P6: no match");
        assertBoolEquals(true, Practice06Sol.solve("aa", "*"), "P6: star all");
        assertBoolEquals(false, Practice06Sol.solve("cb", "?a"), "P6: question fail");
        assertBoolEquals(true, Practice06Sol.solve("adceb", "*a*b"), "P6: star match");
        assertBoolEquals(true, Practice06Sol.solve("", ""), "P6: empty both");
        assertBoolEquals(true, Practice06Sol.solve("", "*"), "P6: empty star");
    }

    static void testC1() {
        assertSCS("abac", "cab", Challenge01Sol.solve("abac", "cab"), 5, "C1: basic");
        assertSCS("aaaaaaaa", "aaaaaaaa", Challenge01Sol.solve("aaaaaaaa", "aaaaaaaa"), 8, "C1: identical");
        assertSCS("abc", "xyz", Challenge01Sol.solve("abc", "xyz"), 6, "C1: no common");
    }

    static void testC2() {
        assertEquals(22, Challenge02Sol.solve(new int[]{1,5,8,9,10,17,17,20}), "C2: basic");
        assertEquals(24, Challenge02Sol.solve(new int[]{3,5,8,9,10,17,17,20}), "C2: basic2");
        assertEquals(1, Challenge02Sol.solve(new int[]{1}), "C2: single");
        assertEquals(5, Challenge02Sol.solve(new int[]{1,5}), "C2: two");
    }

    static void testC3() {
        assertEquals(5, Challenge03Sol.solve(new int[]{1,1,1,1,1}, 3), "C3: basic");
        assertEquals(1, Challenge03Sol.solve(new int[]{1}, 1), "C3: single");
        assertEquals(2, Challenge03Sol.solve(new int[]{1,0}, 1), "C3: with zero");
        assertEquals(0, Challenge03Sol.solve(new int[]{1}, 2), "C3: impossible");
    }

    static void testC4() {
        assertEquals(4, Challenge04Sol.solve(new String[]{"a","b","ba","bca","bda","bdca"}), "C4: basic");
        assertEquals(5, Challenge04Sol.solve(new String[]{"xbc","pcxbcf","xb","cxbc","pcxbc"}), "C4: longer");
        assertEquals(1, Challenge04Sol.solve(new String[]{"abc"}), "C4: single");
    }

    static void testC5() {
        assertEquals(0, Challenge05Sol.solve("zzazz"), "C5: palindrome");
        assertEquals(2, Challenge05Sol.solve("mbadm"), "C5: basic");
        assertEquals(5, Challenge05Sol.solve("leetcode"), "C5: longer");
        assertEquals(0, Challenge05Sol.solve("a"), "C5: single");
        assertEquals(1, Challenge05Sol.solve("ab"), "C5: two diff");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 25: Dynamic Programming III — Subsequences & Knapsack");
        System.out.println("================================================================\n");

        testW1(); testW2(); testW3(); testW4(); testW5();
        testP1(); testP2(); testP3(); testP4(); testP5(); testP6();
        testC1(); testC2(); testC3(); testC4(); testC5();

        System.out.println();
        if (failed == 0) {
            System.out.println("All " + passed + " tests passed!");
        } else {
            System.out.println(passed + " passed, " + failed + " failed.");
            System.exit(1);
        }
    }
}
