package ch21.tests;

import java.util.*;
import ch21.solutions.*;

/**
 * Tests for Chapter 21: Linked Lists — Pointers and Connections
 *
 * Build and run:
 *   cd code/java
 *   javac ch21/tests/TestCh21.java
 *   java -ea ch21.tests.TestCh21
 */
public class TestCh21 {

    // ── Helper methods ──────────────────────────────────────────────

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
            System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected) + ", got " + Arrays.toString(actual));
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

    // ── W1: Traverse ────────────────────────────────────────────────

    static void testW1() {
        System.out.println("Testing W1: Traverse Linked List...");
        assertArrayEquals(new int[]{1,2,3}, Warmup01Sol.solve(new int[]{1,2,3}), "basic");
        assertArrayEquals(new int[]{5}, Warmup01Sol.solve(new int[]{5}), "single");
        assertArrayEquals(new int[]{}, Warmup01Sol.solve(new int[]{}), "empty");
        assertArrayEquals(new int[]{10,20,30,40,50}, Warmup01Sol.solve(new int[]{10,20,30,40,50}), "five");
        assertArrayEquals(new int[]{-1,-2,-3}, Warmup01Sol.solve(new int[]{-1,-2,-3}), "negative");
    }

    // ── W2: Insert ──────────────────────────────────────────────────

    static void testW2() {
        System.out.println("Testing W2: Insert at Position...");
        assertArrayEquals(new int[]{1,2,10,3,4}, Warmup02Sol.solve(new int[]{1,2,3,4}, 10, 2), "middle");
        assertArrayEquals(new int[]{0,1,2,3}, Warmup02Sol.solve(new int[]{1,2,3}, 0, 0), "head");
        assertArrayEquals(new int[]{1,2,3,4}, Warmup02Sol.solve(new int[]{1,2,3}, 4, 3), "tail");
        assertArrayEquals(new int[]{5}, Warmup02Sol.solve(new int[]{}, 5, 0), "empty");
        assertArrayEquals(new int[]{1,2}, Warmup02Sol.solve(new int[]{1}, 2, 1), "single");
    }

    // ── W3: Delete ──────────────────────────────────────────────────

    static void testW3() {
        System.out.println("Testing W3: Delete at Position...");
        assertArrayEquals(new int[]{1,2,4,5}, Warmup03Sol.solve(new int[]{1,2,3,4,5}, 2), "middle");
        assertArrayEquals(new int[]{2,3}, Warmup03Sol.solve(new int[]{1,2,3}, 0), "head");
        assertArrayEquals(new int[]{1,2}, Warmup03Sol.solve(new int[]{1,2,3}, 2), "tail");
        assertArrayEquals(new int[]{}, Warmup03Sol.solve(new int[]{1}, 0), "single");
        assertArrayEquals(new int[]{10,30,40}, Warmup03Sol.solve(new int[]{10,20,30,40}, 1), "second");
    }

    // ── W4: Search ──────────────────────────────────────────────────

    static void testW4() {
        System.out.println("Testing W4: Search...");
        assertBoolEquals(true, Warmup04Sol.solve(new int[]{1,2,3,4,5}, 3), "found");
        assertBoolEquals(false, Warmup04Sol.solve(new int[]{1,2,3}, 7), "not found");
        assertBoolEquals(false, Warmup04Sol.solve(new int[]{}, 1), "empty");
        assertBoolEquals(true, Warmup04Sol.solve(new int[]{5}, 5), "single found");
        assertBoolEquals(false, Warmup04Sol.solve(new int[]{5}, 3), "single not found");
        assertBoolEquals(true, Warmup04Sol.solve(new int[]{10,20,30}, 10), "first");
        assertBoolEquals(true, Warmup04Sol.solve(new int[]{10,20,30}, 30), "last");
    }

    // ── W5: Reverse ─────────────────────────────────────────────────

    static void testW5() {
        System.out.println("Testing W5: Reverse...");
        assertArrayEquals(new int[]{5,4,3,2,1}, Warmup05Sol.solve(new int[]{1,2,3,4,5}), "basic");
        assertArrayEquals(new int[]{2,1}, Warmup05Sol.solve(new int[]{1,2}), "two");
        assertArrayEquals(new int[]{1}, Warmup05Sol.solve(new int[]{1}), "single");
        assertArrayEquals(new int[]{}, Warmup05Sol.solve(new int[]{}), "empty");
        assertArrayEquals(new int[]{1,2,3,4,5}, Warmup05Sol.solve(new int[]{5,4,3,2,1}), "already reversed");
    }

    // ── P1: Find Middle ─────────────────────────────────────────────

    static void testP1() {
        System.out.println("Testing P1: Find Middle...");
        assertEquals(3, Practice01Sol.solve(new int[]{1,2,3,4,5}), "odd");
        assertEquals(3, Practice01Sol.solve(new int[]{1,2,3,4}), "even");
        assertEquals(1, Practice01Sol.solve(new int[]{1}), "single");
        assertEquals(2, Practice01Sol.solve(new int[]{1,2}), "two");
        assertEquals(20, Practice01Sol.solve(new int[]{10,20,30}), "three");
        assertEquals(4, Practice01Sol.solve(new int[]{1,2,3,4,5,6}), "six");
    }

    // ── P2: Detect Cycle ────────────────────────────────────────────

    static void testP2() {
        System.out.println("Testing P2: Detect Cycle...");
        assertBoolEquals(true, Practice02Sol.solve(new int[]{3,2,0,-4}, 1), "cycle mid");
        assertBoolEquals(false, Practice02Sol.solve(new int[]{1,2}, -1), "no cycle");
        assertBoolEquals(true, Practice02Sol.solve(new int[]{1}, 0), "self loop");
        assertBoolEquals(true, Practice02Sol.solve(new int[]{1,2,3}, 0), "cycle head");
        assertBoolEquals(false, Practice02Sol.solve(new int[]{}, -1), "empty");
        assertBoolEquals(false, Practice02Sol.solve(new int[]{1,2,3,4,5,6,7}, -1), "long no cycle");
        assertBoolEquals(true, Practice02Sol.solve(new int[]{1,2,3,4}, 3), "cycle tail");
    }

    // ── P3: Merge Sorted ────────────────────────────────────────────

    static void testP3() {
        System.out.println("Testing P3: Merge Sorted...");
        assertArrayEquals(new int[]{1,2,3,4,5,6}, Practice03Sol.solve(new int[]{1,3,5}, new int[]{2,4,6}), "basic");
        assertArrayEquals(new int[]{1,2,3}, Practice03Sol.solve(new int[]{}, new int[]{1,2,3}), "first empty");
        assertArrayEquals(new int[]{1,2,3}, Practice03Sol.solve(new int[]{1,2,3}, new int[]{}), "second empty");
        assertArrayEquals(new int[]{}, Practice03Sol.solve(new int[]{}, new int[]{}), "both empty");
        assertArrayEquals(new int[]{1,1,2,2,3,3}, Practice03Sol.solve(new int[]{1,2,3}, new int[]{1,2,3}), "duplicates");
        assertArrayEquals(new int[]{1,2}, Practice03Sol.solve(new int[]{1}, new int[]{2}), "single");
    }

    // ── P4: Remove Nth From End ─────────────────────────────────────

    static void testP4() {
        System.out.println("Testing P4: Remove Nth From End...");
        assertArrayEquals(new int[]{1,2,3,5}, Practice04Sol.solve(new int[]{1,2,3,4,5}, 2), "2nd from end");
        assertArrayEquals(new int[]{1}, Practice04Sol.solve(new int[]{1,2}, 1), "last");
        assertArrayEquals(new int[]{}, Practice04Sol.solve(new int[]{1}, 1), "only");
        assertArrayEquals(new int[]{1,2}, Practice04Sol.solve(new int[]{1,2,3}, 1), "1st from end");
        assertArrayEquals(new int[]{2,3}, Practice04Sol.solve(new int[]{1,2,3}, 3), "head");
        assertArrayEquals(new int[]{2}, Practice04Sol.solve(new int[]{1,2}, 2), "head of two");
    }

    // ── P5: Palindrome ──────────────────────────────────────────────

    static void testP5() {
        System.out.println("Testing P5: Palindrome...");
        assertBoolEquals(true, Practice05Sol.solve(new int[]{1,2,3,2,1}), "odd palindrome");
        assertBoolEquals(false, Practice05Sol.solve(new int[]{1,2,3,4,5}), "not palindrome");
        assertBoolEquals(true, Practice05Sol.solve(new int[]{1}), "single");
        assertBoolEquals(true, Practice05Sol.solve(new int[]{}), "empty");
        assertBoolEquals(true, Practice05Sol.solve(new int[]{1,2,2,1}), "even palindrome");
        assertBoolEquals(true, Practice05Sol.solve(new int[]{1,1}), "two same");
        assertBoolEquals(false, Practice05Sol.solve(new int[]{1,2}), "two different");
    }

    // ── C1: Cycle Start ─────────────────────────────────────────────

    static void testC1() {
        System.out.println("Testing C1: Find Cycle Start...");
        assertEquals(1, Challenge01Sol.solve(new int[]{3,2,0,-4}, 1), "idx 1");
        assertEquals(0, Challenge01Sol.solve(new int[]{1,2}, 0), "idx 0");
        assertEquals(-1, Challenge01Sol.solve(new int[]{1}, -1), "no cycle");
        assertEquals(0, Challenge01Sol.solve(new int[]{1}, 0), "self loop");
        assertEquals(2, Challenge01Sol.solve(new int[]{1,2,3,4,5}, 2), "idx 2");
        assertEquals(-1, Challenge01Sol.solve(new int[]{}, -1), "empty");
    }

    // ── C2: Intersection ────────────────────────────────────────────

    static void testC2() {
        System.out.println("Testing C2: Intersection...");
        assertEquals(8, Challenge02Sol.solve(new int[]{4,1,8,4,5}, new int[]{5,6,1,8,4,5}, 2, 3), "basic");
        assertEquals(-1, Challenge02Sol.solve(new int[]{1,2,3}, new int[]{4,5,6}, 3, 3), "none");
        assertEquals(1, Challenge02Sol.solve(new int[]{1,2,3}, new int[]{1,2,3}, 0, 0), "at head");
        assertEquals(2, Challenge02Sol.solve(new int[]{1,9,1,2,4}, new int[]{3,2,4}, 3, 1), "diff prefix");
        assertEquals(7, Challenge02Sol.solve(new int[]{1,2,7}, new int[]{3,4,5,7}, 2, 3), "single shared");
    }

    // ── C3: Add Two Numbers ─────────────────────────────────────────

    static void testC3() {
        System.out.println("Testing C3: Add Two Numbers...");
        assertArrayEquals(new int[]{7,0,8}, Challenge03Sol.solve(new int[]{2,4,3}, new int[]{5,6,4}), "342+465");
        assertArrayEquals(new int[]{0,0,0,1}, Challenge03Sol.solve(new int[]{9,9,9}, new int[]{1}), "999+1");
        assertArrayEquals(new int[]{0}, Challenge03Sol.solve(new int[]{0}, new int[]{0}), "0+0");
        assertArrayEquals(new int[]{0,0,1}, Challenge03Sol.solve(new int[]{9,9}, new int[]{1}), "99+1");
        assertArrayEquals(new int[]{0,1}, Challenge03Sol.solve(new int[]{5}, new int[]{5}), "5+5");
        assertArrayEquals(new int[]{5,7,9}, Challenge03Sol.solve(new int[]{1,2,3}, new int[]{4,5,6}), "321+654");
    }

    // ── C4: Flatten ─────────────────────────────────────────────────

    static void testC4() {
        System.out.println("Testing C4: Flatten...");
        // [1, 2, [3, 4, [5, 6]], 7]
        List<Object> t1 = new ArrayList<>();
        t1.add(1); t1.add(2);
        List<Object> sub1 = new ArrayList<>();
        sub1.add(3); sub1.add(4);
        List<Object> sub2 = new ArrayList<>();
        sub2.add(5); sub2.add(6);
        sub1.add(sub2);
        t1.add(sub1);
        t1.add(7);
        assertListEquals(Arrays.asList(1,2,3,4,5,6,7), Challenge04Sol.solve(t1), "nested");

        // [1, [2, [3]]]
        List<Object> t2 = new ArrayList<>();
        t2.add(1);
        List<Object> s2a = new ArrayList<>();
        s2a.add(2);
        List<Object> s2b = new ArrayList<>();
        s2b.add(3);
        s2a.add(s2b);
        t2.add(s2a);
        assertListEquals(Arrays.asList(1,2,3), Challenge04Sol.solve(t2), "deep");

        // [1, 2, 3]
        List<Object> t3 = new ArrayList<>();
        t3.add(1); t3.add(2); t3.add(3);
        assertListEquals(Arrays.asList(1,2,3), Challenge04Sol.solve(t3), "flat");

        // []
        assertListEquals(new ArrayList<>(), Challenge04Sol.solve(new ArrayList<>()), "empty");
    }

    // ── Main ────────────────────────────────────────────────────────

    public static void main(String[] args) {
        testW1();
        testW2();
        testW3();
        testW4();
        testW5();
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
        if (passed == passed + failed) {
            System.out.println("All " + (passed + failed) + " tests passed!");
        } else {
            System.out.println(passed + " / " + (passed + failed) + " tests passed.");
        }
        System.exit(failed > 0 ? 1 : 0);
    }
}
