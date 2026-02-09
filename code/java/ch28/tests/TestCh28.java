package ch28.tests;

import java.util.*;
import ch28.solutions.*;

/**
 * Tests for Chapter 28: Topological Sort — Ordering Dependencies
 *
 * Build and run:
 *   cd code/java
 *   javac ch28/tests/TestCh28.java
 *   java -ea ch28.tests.TestCh28
 */
public class TestCh28 {

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

    static void assertListEquals(List<?> expected, List<?> actual, String msg) {
        if (expected.equals(actual)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual);
        }
    }

    static boolean isValidTopoOrder(int n, int[][] edges, int[] order) {
        if (order.length != n) return false;
        Set<Integer> seen = new HashSet<>();
        for (int node : order) seen.add(node);
        if (seen.size() != n) return false;
        Map<Integer, Integer> pos = new HashMap<>();
        for (int i = 0; i < n; i++) pos.put(order[i], i);
        for (int[] e : edges)
            if (pos.get(e[0]) >= pos.get(e[1])) return false;
        return true;
    }

    static boolean isValidCourseOrder(int numCourses, int[][] prereqs, int[] order) {
        if (order.length != numCourses) return false;
        Map<Integer, Integer> pos = new HashMap<>();
        for (int i = 0; i < order.length; i++) pos.put(order[i], i);
        if (pos.size() != numCourses) return false;
        for (int[] p : prereqs)
            if (pos.get(p[1]) >= pos.get(p[0])) return false;
        return true;
    }

    static void assertValidTopo(int n, int[][] edges, int[] order, String msg) {
        if (isValidTopoOrder(n, edges, order)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — invalid topo order: " + Arrays.toString(order));
        }
    }

    static void assertValidCourseOrder(int numCourses, int[][] prereqs, int[] order, String msg) {
        if (isValidCourseOrder(numCourses, prereqs, order)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — invalid course order: " + Arrays.toString(order));
        }
    }

    static boolean isValidAlienOrder(String[] words, String order) {
        if (order.isEmpty()) return false;
        Map<Character, Integer> pos = new HashMap<>();
        for (int i = 0; i < order.length(); i++) pos.put(order.charAt(i), i);
        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i], w2 = words[i + 1];
            boolean foundDiff = false;
            int len = Math.min(w1.length(), w2.length());
            for (int j = 0; j < len; j++) {
                if (w1.charAt(j) != w2.charAt(j)) {
                    if (pos.getOrDefault(w1.charAt(j), -1) >= pos.getOrDefault(w2.charAt(j), -1))
                        return false;
                    foundDiff = true;
                    break;
                }
            }
            if (!foundDiff && w1.length() > w2.length()) return false;
        }
        return true;
    }

    // ── Tests ───────────────────────────────────────────────────────

    static void testW1() {
        int[][] edges = {{5,2},{5,0},{4,0},{4,1},{2,3},{3,1}};
        assertValidTopo(6, edges, Warmup01Sol.solve(6, edges), "W1: basic");
        assertArrayEquals(new int[]{0,1,2}, Warmup01Sol.solve(3, new int[][]{{0,1},{1,2}}), "W1: chain");
        assertArrayEquals(new int[]{0}, Warmup01Sol.solve(1, new int[][]{}), "W1: single");
    }

    static void testW2() {
        assertBoolEquals(true, Warmup02Sol.solve(2, new int[][]{{1,0}}), "W2: possible");
        assertBoolEquals(false, Warmup02Sol.solve(2, new int[][]{{1,0},{0,1}}), "W2: cycle");
        assertBoolEquals(true, Warmup02Sol.solve(4, new int[][]{{1,0},{2,1},{3,2}}), "W2: chain");
        assertBoolEquals(true, Warmup02Sol.solve(1, new int[][]{}), "W2: single");
    }

    static void testW3() {
        int[][] prereqs = {{1,0},{2,0},{3,1},{3,2}};
        assertValidCourseOrder(4, prereqs, Warmup03Sol.solve(4, prereqs), "W3: basic");
        assertArrayEquals(new int[]{}, Warmup03Sol.solve(2, new int[][]{{1,0},{0,1}}), "W3: cycle");
        assertArrayEquals(new int[]{0}, Warmup03Sol.solve(1, new int[][]{}), "W3: single");
    }

    static void testW4() {
        assertBoolEquals(true, Warmup04Sol.solve(4, new int[][]{{0,1},{1,2},{2,3}}), "W4: dag");
        assertBoolEquals(false, Warmup04Sol.solve(3, new int[][]{{0,1},{1,2},{2,0}}), "W4: cycle");
        assertBoolEquals(true, Warmup04Sol.solve(4, new int[][]{{0,1},{1,2},{3,0}}), "W4: dag branch");
        assertBoolEquals(true, Warmup04Sol.solve(1, new int[][]{}), "W4: single");
    }

    static void testP1() {
        String[] w1 = {"wrt","wrf","er","ett","rftt"};
        String r1 = Practice01Sol.solve(w1);
        if (isValidAlienOrder(w1, r1)) passed++; else { failed++; System.out.println("FAIL: P1: basic — got " + r1); }

        String[] w2 = {"z","x"};
        String r2 = Practice01Sol.solve(w2);
        if (isValidAlienOrder(w2, r2)) passed++; else { failed++; System.out.println("FAIL: P1: two — got " + r2); }

        if (Practice01Sol.solve(new String[]{"z","x","z"}).isEmpty()) passed++;
        else { failed++; System.out.println("FAIL: P1: cycle"); }
    }

    static void testP2() {
        assertEquals(2, Practice02Sol.solve(3, new int[][]{{1,3},{2,3}}), "P2: basic");
        assertEquals(-1, Practice02Sol.solve(3, new int[][]{{1,2},{2,3},{3,1}}), "P2: cycle");
        assertEquals(3, Practice02Sol.solve(4, new int[][]{{1,2},{1,3},{2,4},{3,4}}), "P2: diamond");
    }

    static void testP3() {
        List<String> r1 = Practice03Sol.solve(
            new String[]{"bread","sandwich"},
            new String[][]{{"yeast","flour"},{"bread","meat"}},
            new String[]{"yeast","flour","meat"}
        );
        List<String> s1 = new ArrayList<>(r1);
        Collections.sort(s1);
        assertListEquals(Arrays.asList("bread","sandwich"), s1, "P3: chain");

        List<String> r2 = Practice03Sol.solve(
            new String[]{"bread"},
            new String[][]{{"yeast","flour"}},
            new String[]{"yeast"}
        );
        assertListEquals(new ArrayList<>(), r2, "P3: missing");
    }

    static void testP4() {
        List<List<Integer>> r1 = Practice04Sol.solve(5, new int[][]{{0,1},{0,2},{0,3},{1,4},{2,4}});
        assertListEquals(Arrays.asList(), r1.get(0), "P4: node 0");
        assertListEquals(Arrays.asList(0), r1.get(1), "P4: node 1");
        assertListEquals(Arrays.asList(0), r1.get(2), "P4: node 2");
        assertListEquals(Arrays.asList(0), r1.get(3), "P4: node 3");
        assertListEquals(Arrays.asList(0, 1, 2), r1.get(4), "P4: node 4");

        List<List<Integer>> r2 = Practice04Sol.solve(3, new int[][]{{0,1},{1,2}});
        assertListEquals(Arrays.asList(), r2.get(0), "P4: chain 0");
        assertListEquals(Arrays.asList(0), r2.get(1), "P4: chain 1");
        assertListEquals(Arrays.asList(0, 1), r2.get(2), "P4: chain 2");
    }

    static void testC1() {
        List<Integer> r1 = Challenge01Sol.solve(4, new int[][]{{1,0},{1,2},{1,3}});
        Collections.sort(r1);
        assertListEquals(Arrays.asList(1), r1, "C1: star");

        List<Integer> r2 = Challenge01Sol.solve(6, new int[][]{{3,0},{3,1},{3,2},{3,4},{5,4}});
        Collections.sort(r2);
        assertListEquals(Arrays.asList(3, 4), r2, "C1: path");

        assertListEquals(Arrays.asList(0), Challenge01Sol.solve(1, new int[][]{}), "C1: single");

        List<Integer> r3 = Challenge01Sol.solve(2, new int[][]{{0,1}});
        Collections.sort(r3);
        assertListEquals(Arrays.asList(0, 1), r3, "C1: pair");
    }

    static void testC2() {
        assertListEquals(Arrays.asList(2,4,5,6),
            Challenge02Sol.solve(new int[][]{{1,2},{2,3},{5},{0},{5},{},{}}), "C2: basic");
        assertListEquals(Arrays.asList(4),
            Challenge02Sol.solve(new int[][]{{1,2,3,4},{1,2},{3,4},{0,4},{}}), "C2: cycle heavy");
    }

    static void testC3() {
        assertEquals(3, Challenge03Sol.solve("abaca", new int[][]{{0,1},{0,2},{2,3},{3,4}}), "C3: basic");
        assertEquals(-1, Challenge03Sol.solve("a", new int[][]{{0,0}}), "C3: self loop");
        assertEquals(1, Challenge03Sol.solve("a", new int[][]{}), "C3: single");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 28: Topological Sort — Ordering Dependencies");
        System.out.println("======================================================\n");

        testW1(); testW2(); testW3(); testW4();
        testP1(); testP2(); testP3(); testP4();
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
