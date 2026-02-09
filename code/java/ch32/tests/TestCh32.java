package ch32.tests;

import java.util.*;
import ch32.solutions.*;

/**
 * Tests for Chapter 32: String Algorithms — Beyond Brute Force
 *
 * Build and run:
 *   cd code/java
 *   javac ch32/tests/TestCh32.java
 *   java -ea ch32.tests.TestCh32
 */
public class TestCh32 {

    static int passed = 0;
    static int failed = 0;

    static void assertEquals(int expected, int actual, String msg) {
        if (expected == actual) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertBoolArrayEquals(boolean[] expected, boolean[] actual, String msg) {
        if (Arrays.equals(expected, actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected) + ", got " + Arrays.toString(actual)); }
    }

    static void assertIntArrayEquals(int[] expected, int[] actual, String msg) {
        if (Arrays.equals(expected, actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected) + ", got " + Arrays.toString(actual)); }
    }

    static void assertListEquals(List<Integer> expected, List<Integer> actual, String msg) {
        if (expected.equals(actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertStringEquals(String expected, String actual, String msg) {
        if (expected.equals(actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected '" + expected + "', got '" + actual + "'"); }
    }

    static void assertStringListEquals(List<String> expected, List<String> actual, String msg) {
        if (expected.equals(actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    // ── Tests ───────────────────────────────────────────────────────

    static void testW1() {
        assertBoolArrayEquals(new boolean[]{true,true,false,true},
            Warmup01Sol.solve(new String[]{"apple","app","banana"}, new String[]{"app","apple","ban","banana"}), "W1: basic");
        assertBoolArrayEquals(new boolean[]{true,false,false},
            Warmup01Sol.solve(new String[]{"hello"}, new String[]{"hello","hell","helloo"}), "W1: single word");
        assertBoolArrayEquals(new boolean[]{false,true},
            Warmup01Sol.solve(new String[]{"application"}, new String[]{"app","application"}), "W1: prefix not word");
    }

    static void testW2() {
        assertIntArrayEquals(new int[]{3,4,1,0},
            Warmup02Sol.solve(new String[]{"apple","app","application","apt","banana"}, new String[]{"app","a","ban","c"}), "W2: basic");
        assertIntArrayEquals(new int[]{3,3},
            Warmup02Sol.solve(new String[]{"test","testing","tested"}, new String[]{"test","tes"}), "W2: same prefix");
        assertIntArrayEquals(new int[]{0},
            Warmup02Sol.solve(new String[]{"abc","abd"}, new String[]{"xyz"}), "W2: no match");
    }

    static void testW3() {
        assertListEquals(Arrays.asList(0,9,12),
            Warmup03Sol.solve("AABAACAADAABAABA", "AABA"), "W3: multiple matches");
        assertListEquals(Arrays.asList(0,3),
            Warmup03Sol.solve("ABCABC", "ABC"), "W3: two matches");
        assertListEquals(Arrays.asList(0,1,2,3),
            Warmup03Sol.solve("AAAAA", "AA"), "W3: overlapping");
        assertListEquals(new ArrayList<>(),
            Warmup03Sol.solve("HELLO", "WORLD"), "W3: no match");
    }

    static void testW4() {
        assertIntArrayEquals(new int[]{0,1,0,0,2,1},
            Warmup04Sol.solve("aabxaa"), "W4: mixed");
        assertIntArrayEquals(new int[]{0,4,3,2,1},
            Warmup04Sol.solve("aaaaa"), "W4: all same");
        assertIntArrayEquals(new int[]{0,0,0,0,0,0},
            Warmup04Sol.solve("abcdef"), "W4: all different");
    }

    static void testP1() {
        assertListEquals(Arrays.asList(0,9,12),
            Practice01Sol.solve("AABAACAADAABAABA", "AABA"), "P1: multiple matches");
        assertListEquals(Arrays.asList(0,2,4),
            Practice01Sol.solve("ABABABAB", "ABAB"), "P1: overlapping");
        assertListEquals(Arrays.asList(0),
            Practice01Sol.solve("HELLO", "HELLO"), "P1: full match");
    }

    static void testP2() {
        assertStringEquals("fl",
            Practice02Sol.solve(new String[]{"flower","flow","flight"}), "P2: partial");
        assertStringEquals("",
            Practice02Sol.solve(new String[]{"dog","racecar","car"}), "P2: none");
        assertStringEquals("inter",
            Practice02Sol.solve(new String[]{"interstellar","internet","internal"}), "P2: longer");
        assertStringEquals("a",
            Practice02Sol.solve(new String[]{"a"}), "P2: single");
    }

    static void testP3() {
        assertEquals(8, Practice03Sol.solve("abab"), "P3: abab");
        assertEquals(4, Practice03Sol.solve("aaa"), "P3: aaa");
        assertEquals(7, Practice03Sol.solve("abc"), "P3: abc");
    }

    static void testP4() {
        assertEquals(3, Practice04Sol.solve("abcd", "cdabcdab"), "P4: three repeats");
        assertEquals(2, Practice04Sol.solve("a", "aa"), "P4: two repeats");
        assertEquals(-1, Practice04Sol.solve("abc", "xyz"), "P4: impossible");
        assertEquals(1, Practice04Sol.solve("abc", "abc"), "P4: one repeat");
    }

    static void testP5() {
        assertStringEquals("l", Practice05Sol.solve("level"), "P5: level");
        assertStringEquals("abab", Practice05Sol.solve("ababab"), "P5: ababab");
        assertStringEquals("", Practice05Sol.solve("a"), "P5: single");
        assertStringEquals("abc", Practice05Sol.solve("abcabc"), "P5: abcabc");
    }

    static void testC1() {
        char[][] board1 = {{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}};
        List<String> r1 = Challenge01Sol.solve(board1, new String[]{"oath","pea","eat","rain"});
        assertStringListEquals(Arrays.asList("eat","oath"), r1, "C1: basic");

        char[][] board2 = {{'a','b'},{'c','d'}};
        List<String> r2 = Challenge01Sol.solve(board2, new String[]{"abcb"});
        assertStringListEquals(new ArrayList<>(), r2, "C1: no match");
    }

    static void testC2() {
        assertStringEquals("aaacecaaa", Challenge02Sol.solve("aacecaaa"), "C2: almost palindrome");
        assertStringEquals("dcbabcd", Challenge02Sol.solve("abcd"), "C2: no palindrome");
        assertStringEquals("a", Challenge02Sol.solve("a"), "C2: single");
        assertStringEquals("", Challenge02Sol.solve(""), "C2: empty");
    }

    static void testC3() {
        assertEquals(3, Challenge03Sol.solve("abcabc", 3), "C3: abc");
        assertEquals(1, Challenge03Sol.solve("aaaa", 2), "C3: all same");
        assertEquals(6, Challenge03Sol.solve("abcdef", 1), "C3: all different");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 32: String Algorithms — Beyond Brute Force");
        System.out.println("================================================================\n");

        testW1(); testW2(); testW3(); testW4();
        testP1(); testP2(); testP3(); testP4(); testP5();
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
