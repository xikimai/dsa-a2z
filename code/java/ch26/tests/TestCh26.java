package ch26.tests;

import java.util.*;
import ch26.solutions.*;

/**
 * Tests for Chapter 26: Trees — Branches of Logic
 *
 * Build and run:
 *   cd code/java
 *   javac ch26/tests/TestCh26.java
 *   java -ea ch26.tests.TestCh26
 */
public class TestCh26 {

    static int passed = 0;
    static int failed = 0;

    static void assertEquals(int expected, int actual, String msg) {
        if (expected == actual) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertBoolEquals(boolean expected, boolean actual, String msg) {
        if (expected == actual) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertListEquals(List<?> expected, List<?> actual, String msg) {
        if (expected.equals(actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    // Helper: build tree from Integer array
    static Object[] bt(Integer... values) { return values; }

    // ── Tests ───────────────────────────────────────────────────────

    static void testW1() {
        assertListEquals(Arrays.asList(1,3,2), Warmup01Sol.solve(Warmup01Sol.buildTree(new Integer[]{1,null,2,3})), "W1: basic");
        assertListEquals(Arrays.asList(4,2,5,1,3), Warmup01Sol.solve(Warmup01Sol.buildTree(new Integer[]{1,2,3,4,5})), "W1: full");
        assertListEquals(Arrays.asList(), Warmup01Sol.solve(null), "W1: empty");
        assertListEquals(Arrays.asList(1), Warmup01Sol.solve(Warmup01Sol.buildTree(new Integer[]{1})), "W1: single");
    }

    static void testW2() {
        assertListEquals(Arrays.asList(1,2,3), Warmup02Sol.solve(Warmup02Sol.buildTree(new Integer[]{1,null,2,3})), "W2: basic");
        assertListEquals(Arrays.asList(1,2,4,5,3), Warmup02Sol.solve(Warmup02Sol.buildTree(new Integer[]{1,2,3,4,5})), "W2: full");
        assertListEquals(Arrays.asList(), Warmup02Sol.solve(null), "W2: empty");
    }

    static void testW3() {
        List<List<Integer>> expected = Arrays.asList(Arrays.asList(3), Arrays.asList(9,20), Arrays.asList(15,7));
        assertListEquals(expected, Warmup03Sol.solve(Warmup03Sol.buildTree(new Integer[]{3,9,20,null,null,15,7})), "W3: basic");
        assertListEquals(Arrays.asList(Arrays.asList(1)), Warmup03Sol.solve(Warmup03Sol.buildTree(new Integer[]{1})), "W3: single");
        assertListEquals(Arrays.asList(), Warmup03Sol.solve(null), "W3: empty");
    }

    static void testW4() {
        assertEquals(3, Warmup04Sol.solve(Warmup04Sol.buildTree(new Integer[]{3,9,20,null,null,15,7})), "W4: basic");
        assertEquals(2, Warmup04Sol.solve(Warmup04Sol.buildTree(new Integer[]{1,null,2})), "W4: skewed");
        assertEquals(0, Warmup04Sol.solve(null), "W4: empty");
    }

    static void testW5() {
        assertBoolEquals(true, Warmup05Sol.solve(Warmup05Sol.buildTree(new Integer[]{1,2,2,3,4,4,3})), "W5: symmetric");
        assertBoolEquals(false, Warmup05Sol.solve(Warmup05Sol.buildTree(new Integer[]{1,2,2,null,3,null,3})), "W5: asymmetric");
        assertBoolEquals(true, Warmup05Sol.solve(null), "W5: empty");
    }

    static void testP1() {
        assertEquals(3, Practice01Sol.solve(Practice01Sol.buildTree(new Integer[]{1,2,3,4,5})), "P1: basic");
        assertEquals(1, Practice01Sol.solve(Practice01Sol.buildTree(new Integer[]{1,2})), "P1: two");
        assertEquals(0, Practice01Sol.solve(null), "P1: empty");
    }

    static void testP2() {
        assertBoolEquals(true, Practice02Sol.solve(Practice02Sol.buildTree(new Integer[]{3,9,20,null,null,15,7})), "P2: balanced");
        assertBoolEquals(false, Practice02Sol.solve(Practice02Sol.buildTree(new Integer[]{1,2,2,3,3,null,null,4,4})), "P2: unbalanced");
        assertBoolEquals(true, Practice02Sol.solve(null), "P2: empty");
    }

    static void testP3() {
        assertListEquals(Arrays.asList(1,3,4), Practice03Sol.solve(Practice03Sol.buildTree(new Integer[]{1,2,3,null,5,null,4})), "P3: basic");
        assertListEquals(Arrays.asList(1,3), Practice03Sol.solve(Practice03Sol.buildTree(new Integer[]{1,null,3})), "P3: right skewed");
        assertListEquals(Arrays.asList(), Practice03Sol.solve(null), "P3: empty");
    }

    static void testP4() {
        assertBoolEquals(true, Practice04Sol.solve(Practice04Sol.buildTree(new Integer[]{2,1,3})), "P4: valid");
        assertBoolEquals(false, Practice04Sol.solve(Practice04Sol.buildTree(new Integer[]{5,1,4,null,null,3,6})), "P4: invalid");
        assertBoolEquals(true, Practice04Sol.solve(Practice04Sol.buildTree(new Integer[]{1})), "P4: single");
    }

    static void testP5() {
        assertEquals(1, Practice05Sol.solve(Practice05Sol.buildTree(new Integer[]{3,1,4,null,2}), 1), "P5: first");
        assertEquals(3, Practice05Sol.solve(Practice05Sol.buildTree(new Integer[]{5,3,6,2,4,null,null,1}), 3), "P5: third");
    }

    static void testP6() {
        assertEquals(3, Practice06Sol.solve(Practice06Sol.buildTree(new Integer[]{3,5,1,6,2,0,8,null,null,7,4}), 5, 1), "P6: root");
        assertEquals(5, Practice06Sol.solve(Practice06Sol.buildTree(new Integer[]{3,5,1,6,2,0,8,null,null,7,4}), 5, 4), "P6: ancestor");
        assertEquals(1, Practice06Sol.solve(Practice06Sol.buildTree(new Integer[]{1,2}), 1, 2), "P6: parent-child");
    }

    static void testP7() {
        assertEquals(6, Practice07Sol.solve(Practice07Sol.buildTree(new Integer[]{1,2,3})), "P7: basic");
        assertEquals(42, Practice07Sol.solve(Practice07Sol.buildTree(new Integer[]{-10,9,20,null,null,15,7})), "P7: negative");
        assertEquals(-3, Practice07Sol.solve(Practice07Sol.buildTree(new Integer[]{-3})), "P7: single negative");
    }

    static void testC1() {
        List<Integer> expected = new ArrayList<>(Arrays.asList(3, 9, 20, null, null, 15, 7));
        assertListEquals(expected, Challenge01Sol.solve(new int[]{3,9,20,15,7}, new int[]{9,3,15,20,7}), "C1: basic");
        assertListEquals(Arrays.asList(-1), Challenge01Sol.solve(new int[]{-1}, new int[]{-1}), "C1: single");
    }

    static void testC2() {
        // Round-trip test
        Challenge02Sol.TreeNode tree = Challenge02Sol.buildTree(new Integer[]{1,2,3,null,null,4,5});
        String s = Challenge02Sol.serialize(tree);
        Challenge02Sol.TreeNode restored = Challenge02Sol.deserialize(s);
        // Verify by serializing again
        String s2 = Challenge02Sol.serialize(restored);
        if (s.equals(s2)) { passed++; }
        else { failed++; System.out.println("FAIL: C2: round-trip — got different serialization"); }

        // Empty test
        String empty = Challenge02Sol.serialize(null);
        Challenge02Sol.TreeNode nullTree = Challenge02Sol.deserialize(empty);
        if (nullTree == null) { passed++; }
        else { failed++; System.out.println("FAIL: C2: empty — expected null"); }
    }

    static void testC3() {
        assertListEquals(Arrays.asList(1,2,4,7,8,9,10,6,3),
            Challenge03Sol.solve(Challenge03Sol.buildTree(new Integer[]{1,2,3,4,5,6,null,null,null,7,8,9,10})), "C3: basic");
        assertListEquals(Arrays.asList(1),
            Challenge03Sol.solve(Challenge03Sol.buildTree(new Integer[]{1})), "C3: single");
    }

    static void testC4() {
        assertEquals(1, Challenge04Sol.solve(Challenge04Sol.buildTree(new Integer[]{0,0,null,0,0})), "C4: basic");
        assertEquals(2, Challenge04Sol.solve(Challenge04Sol.buildTree(new Integer[]{0,0,null,0,null,0,null,null,0})), "C4: longer");
    }

    static void testC5() {
        assertListEquals(Arrays.asList(1,2,3,4,5,6),
            Challenge05Sol.solve(Challenge05Sol.buildTree(new Integer[]{1,2,5,3,4,null,6})), "C5: basic");
        assertListEquals(Arrays.asList(),
            Challenge05Sol.solve(null), "C5: empty");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 26: Trees — Branches of Logic");
        System.out.println("========================================\n");

        testW1(); testW2(); testW3(); testW4(); testW5();
        testP1(); testP2(); testP3(); testP4(); testP5(); testP6(); testP7();
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
