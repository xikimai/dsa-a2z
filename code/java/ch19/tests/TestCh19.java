package ch19.tests;

import java.util.*;
import ch19.solutions.*;

/**
 * Tests for Chapter 19: Graphs I — Exploring Networks
 *
 * Build and run:
 *   cd code/java
 *   javac ch19/tests/TestCh19.java
 *   java -ea ch19.tests.TestCh19
 */
public class TestCh19 {

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

    static void assertNestedListEquals(List<List<Integer>> expected, List<List<Integer>> actual, String msg) {
        if (expected.equals(actual)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual);
        }
    }

    // ── W1: Build Adjacency List ────────────────────────────────────

    static void testW1() {
        List<List<Integer>> adj = Warmup01Sol.solve(4, new int[][]{{0,1},{0,2},{1,3}});
        assertListEquals(Arrays.asList(1,2), adj.get(0), "W1: node 0");
        assertListEquals(Arrays.asList(0,3), adj.get(1), "W1: node 1");
        assertListEquals(Arrays.asList(0), adj.get(2), "W1: node 2");
        assertListEquals(Arrays.asList(1), adj.get(3), "W1: node 3");

        List<List<Integer>> adj2 = Warmup01Sol.solve(3, new int[][]{});
        assertListEquals(new ArrayList<>(), adj2.get(0), "W1: no edges");

        List<List<Integer>> adj3 = Warmup01Sol.solve(1, new int[][]{});
        assertListEquals(new ArrayList<>(), adj3.get(0), "W1: single node");
    }

    // ── W2: BFS Traversal ──────────────────────────────────────────

    static void testW2() {
        assertListEquals(Arrays.asList(0,1,2,3,4),
            Warmup02Sol.solve(5, new int[][]{{0,1},{0,2},{1,3},{2,3},{3,4}}, 0), "W2: basic");
        assertListEquals(Arrays.asList(2,1,0),
            Warmup02Sol.solve(3, new int[][]{{0,1},{1,2}}, 2), "W2: from end");
        assertListEquals(Arrays.asList(0),
            Warmup02Sol.solve(1, new int[][]{}, 0), "W2: single node");
        assertListEquals(Arrays.asList(0,1),
            Warmup02Sol.solve(4, new int[][]{{0,1},{2,3}}, 0), "W2: disconnected");
    }

    // ── W3: DFS Traversal ──────────────────────────────────────────

    static void testW3() {
        assertListEquals(Arrays.asList(0,1,3,2,4),
            Warmup03Sol.solve(5, new int[][]{{0,1},{0,2},{1,3},{2,3},{3,4}}, 0), "W3: basic");
        assertListEquals(Arrays.asList(0,1,2),
            Warmup03Sol.solve(3, new int[][]{{0,1},{1,2}}, 0), "W3: linear");
        assertListEquals(Arrays.asList(0),
            Warmup03Sol.solve(1, new int[][]{}, 0), "W3: single node");
        assertListEquals(Arrays.asList(1,0,2,3),
            Warmup03Sol.solve(4, new int[][]{{0,1},{1,2},{2,3}}, 1), "W3: from middle");
    }

    // ── W4: Count Connected Components ─────────────────────────────

    static void testW4() {
        assertEquals(2, Warmup04Sol.solve(5, new int[][]{{0,1},{1,2},{3,4}}), "W4: two components");
        assertEquals(4, Warmup04Sol.solve(4, new int[][]{}), "W4: no edges");
        assertEquals(1, Warmup04Sol.solve(3, new int[][]{{0,1},{1,2},{0,2}}), "W4: fully connected");
        assertEquals(1, Warmup04Sol.solve(1, new int[][]{}), "W4: single node");
        assertEquals(3, Warmup04Sol.solve(7, new int[][]{{0,1},{0,2},{3,4},{3,5}}), "W4: three components");
    }

    // ── W5: Is Path Exists ─────────────────────────────────────────

    static void testW5() {
        assertBoolEquals(true, Warmup05Sol.solve(5, new int[][]{{0,1},{1,2},{3,4}}, 0, 2), "W5: path exists");
        assertBoolEquals(false, Warmup05Sol.solve(5, new int[][]{{0,1},{1,2},{3,4}}, 0, 4), "W5: no path");
        assertBoolEquals(true, Warmup05Sol.solve(3, new int[][]{}, 0, 0), "W5: same node");
        assertBoolEquals(true, Warmup05Sol.solve(3, new int[][]{{0,1},{1,2}}, 0, 1), "W5: direct");
        assertBoolEquals(false, Warmup05Sol.solve(3, new int[][]{{0,1}}, 0, 2), "W5: isolated");
    }

    // ── P1: Shortest Path ──────────────────────────────────────────

    static void testP1() {
        assertArrayEquals(new int[]{0,1,1,2,3},
            Practice01Sol.solve(5, new int[][]{{0,1},{0,2},{1,3},{2,3},{3,4}}, 0), "P1: basic");
        assertArrayEquals(new int[]{0,1,-1,-1},
            Practice01Sol.solve(4, new int[][]{{0,1},{2,3}}, 0), "P1: disconnected");
        assertArrayEquals(new int[]{0},
            Practice01Sol.solve(1, new int[][]{}, 0), "P1: single");
        assertArrayEquals(new int[]{0,1,2,3},
            Practice01Sol.solve(4, new int[][]{{0,1},{1,2},{2,3}}, 0), "P1: linear");
        assertArrayEquals(new int[]{2,1,0,1,2},
            Practice01Sol.solve(5, new int[][]{{0,1},{1,2},{2,3},{3,4}}, 2), "P1: from middle");
    }

    // ── P2: Detect Cycle ───────────────────────────────────────────

    static void testP2() {
        assertBoolEquals(false, Practice02Sol.solve(4, new int[][]{{0,1},{1,2},{2,3}}), "P2: no cycle");
        assertBoolEquals(true, Practice02Sol.solve(4, new int[][]{{0,1},{1,2},{2,3},{3,0}}), "P2: has cycle");
        assertBoolEquals(true, Practice02Sol.solve(3, new int[][]{{0,1},{1,2},{0,2}}), "P2: triangle");
        assertBoolEquals(false, Practice02Sol.solve(3, new int[][]{}), "P2: no edges");
        assertBoolEquals(true, Practice02Sol.solve(5, new int[][]{{0,1},{2,3},{3,4},{4,2}}), "P2: disconnected w/ cycle");
        assertBoolEquals(false, Practice02Sol.solve(5, new int[][]{{0,1},{2,3}}), "P2: disconnected no cycle");
    }

    // ── P3: Bipartite Check ────────────────────────────────────────

    static void testP3() {
        assertBoolEquals(true, Practice03Sol.solve(4, new int[][]{{0,1},{1,2},{2,3},{3,0}}), "P3: even cycle");
        assertBoolEquals(false, Practice03Sol.solve(3, new int[][]{{0,1},{1,2},{0,2}}), "P3: triangle");
        assertBoolEquals(true, Practice03Sol.solve(3, new int[][]{}), "P3: no edges");
        assertBoolEquals(true, Practice03Sol.solve(2, new int[][]{{0,1}}), "P3: single edge");
        assertBoolEquals(true, Practice03Sol.solve(5, new int[][]{{0,1},{2,3}}), "P3: disconnected bipartite");
        assertBoolEquals(false, Practice03Sol.solve(5, new int[][]{{0,1},{1,2},{2,3},{3,4},{4,0}}), "P3: 5-cycle");
    }

    // ── P4: Clone Graph ────────────────────────────────────────────

    static void testP4() {
        List<List<Integer>> adj = new ArrayList<>();
        adj.add(Arrays.asList(1,2)); adj.add(Arrays.asList(0,3));
        adj.add(Arrays.asList(0,3)); adj.add(Arrays.asList(1,2));
        List<List<Integer>> clone = Practice04Sol.solve(adj);
        assertNestedListEquals(adj, clone, "P4: basic content match");
        assertBoolEquals(true, clone != adj, "P4: different top-level ref");

        List<List<Integer>> empty = new ArrayList<>();
        assertNestedListEquals(empty, Practice04Sol.solve(empty), "P4: empty");

        List<List<Integer>> single = new ArrayList<>();
        single.add(new ArrayList<>());
        List<List<Integer>> singleClone = Practice04Sol.solve(single);
        assertNestedListEquals(single, singleClone, "P4: single node");
    }

    // ── P5: All Paths ──────────────────────────────────────────────

    static void testP5() {
        List<List<Integer>> expected1 = new ArrayList<>();
        expected1.add(Arrays.asList(0,1,3)); expected1.add(Arrays.asList(0,2,3));
        assertNestedListEquals(expected1,
            Practice05Sol.solve(4, new int[][]{{0,1},{0,2},{1,3},{2,3}}), "P5: basic");

        List<List<Integer>> expected2 = new ArrayList<>();
        expected2.add(Arrays.asList(0,1,2,3)); expected2.add(Arrays.asList(0,1,3));
        expected2.add(Arrays.asList(0,2,3));
        assertNestedListEquals(expected2,
            Practice05Sol.solve(4, new int[][]{{0,1},{0,2},{1,2},{1,3},{2,3}}), "P5: multiple");

        List<List<Integer>> expected3 = new ArrayList<>();
        expected3.add(Arrays.asList(0,1));
        assertNestedListEquals(expected3,
            Practice05Sol.solve(2, new int[][]{{0,1}}), "P5: direct");

        assertNestedListEquals(new ArrayList<>(),
            Practice05Sol.solve(3, new int[][]{{0,1}}), "P5: no path");
    }

    // ── C1: Number of Provinces ────────────────────────────────────

    static void testC1() {
        assertEquals(2, Challenge01Sol.solve(new int[][]{{1,1,0},{1,1,0},{0,0,1}}), "C1: two provinces");
        assertEquals(3, Challenge01Sol.solve(new int[][]{{1,0,0},{0,1,0},{0,0,1}}), "C1: three provinces");
        assertEquals(1, Challenge01Sol.solve(new int[][]{{1,1,1},{1,1,1},{1,1,1}}), "C1: one province");
        assertEquals(1, Challenge01Sol.solve(new int[][]{{1}}), "C1: single");
    }

    // ── C2: Course Schedule ────────────────────────────────────────

    static void testC2() {
        assertBoolEquals(true, Challenge02Sol.solve(2, new int[][]{{1,0}}), "C2: no cycle");
        assertBoolEquals(false, Challenge02Sol.solve(2, new int[][]{{1,0},{0,1}}), "C2: cycle");
        assertBoolEquals(true, Challenge02Sol.solve(4, new int[][]{{1,0},{2,1},{3,2}}), "C2: chain");
        assertBoolEquals(true, Challenge02Sol.solve(3, new int[][]{}), "C2: no prereqs");
        assertBoolEquals(false, Challenge02Sol.solve(4, new int[][]{{1,0},{2,1},{0,2}}), "C2: complex cycle");
        assertBoolEquals(true, Challenge02Sol.solve(4, new int[][]{{1,0},{3,2}}), "C2: disconnected");
    }

    // ── C3: Word Ladder ────────────────────────────────────────────

    static void testC3() {
        assertEquals(5, Challenge03Sol.solve("hit", "cog",
            Arrays.asList("hot","dot","dog","lot","log","cog")), "C3: basic");
        assertEquals(0, Challenge03Sol.solve("hit", "cog",
            Arrays.asList("hot","dot","dog","lot","log")), "C3: no path");
        assertEquals(2, Challenge03Sol.solve("hot", "dot",
            Arrays.asList("dot")), "C3: direct");
        assertEquals(2, Challenge03Sol.solve("a", "c",
            Arrays.asList("a","b","c")), "C3: single letter");
        assertEquals(0, Challenge03Sol.solve("abc", "xyz",
            Arrays.asList("abd","acd")), "C3: end not in list");
    }

    // ── Main ────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 19: Graphs I — Exploring Networks");
        System.out.println("==========================================\n");

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

        System.out.println();
        if (failed == 0) {
            System.out.println("All " + passed + " tests passed!");
        } else {
            System.out.println(passed + " passed, " + failed + " failed.");
            System.exit(1);
        }
    }
}
