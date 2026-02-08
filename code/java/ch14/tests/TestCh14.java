package ch14.tests;

import java.util.*;

/**
 * Tests for Chapter 14: Prefix Sums — The Running Total Trick
 *
 * Build and run:
 *   cd code/java
 *   javac ch14/tests/TestCh14.java
 *   java -ea ch14.tests.TestCh14
 */
public class TestCh14 {

    static int passed = 0;
    static int failed = 0;

    static void assertEquals(long expected, long actual, String msg) {
        if (expected == actual) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertBoolEquals(boolean expected, boolean actual, String msg) {
        if (expected == actual) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertArrayEquals(long[] expected, long[] actual, String msg) {
        if (Arrays.equals(expected, actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected) + ", got " + Arrays.toString(actual)); }
    }

    // ── Reference solutions ─────────────────────────────────────────

    // W1: Build Prefix Sum
    static long[] solveW1(int[] arr) {
        int n = arr.length;
        long[] p = new long[n + 1];
        for (int i = 1; i <= n; i++) p[i] = p[i - 1] + arr[i - 1];
        return p;
    }

    // W2: Range Sum Query
    static long[] solveW2(int[] arr, int[][] queries) {
        int n = arr.length;
        long[] p = new long[n + 1];
        for (int i = 0; i < n; i++) p[i + 1] = p[i] + arr[i];
        long[] result = new long[queries.length];
        for (int q = 0; q < queries.length; q++)
            result[q] = p[queries[q][1] + 1] - p[queries[q][0]];
        return result;
    }

    // W3: Running Sum
    static long[] solveW3(int[] arr) {
        if (arr.length == 0) return new long[0];
        long[] r = new long[arr.length];
        r[0] = arr[0];
        for (int i = 1; i < arr.length; i++) r[i] = r[i - 1] + arr[i];
        return r;
    }

    // W4: Is Prefix
    static boolean solveW4(int[] a1, int[] a2) {
        if (a1.length > a2.length) return false;
        for (int i = 0; i < a1.length; i++) if (a1[i] != a2[i]) return false;
        return true;
    }

    // P1: Equilibrium Index
    static int solveP1(int[] arr) {
        int n = arr.length;
        long[] p = new long[n + 1];
        for (int i = 0; i < n; i++) p[i + 1] = p[i] + arr[i];
        for (int i = 0; i < n; i++) {
            if (p[i] == p[n] - p[i + 1]) return i;
        }
        return -1;
    }

    // P2: Subarray Sum K
    static int solveP2(int[] arr, int k) {
        Map<Long, Integer> map = new HashMap<>();
        map.put(0L, 1);
        long sum = 0; int count = 0;
        for (int x : arr) {
            sum += x;
            count += map.getOrDefault(sum - k, 0);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }

    // P3: Product Except Self
    static long[] solveP3(int[] arr) {
        int n = arr.length;
        long[] r = new long[n];
        long left = 1;
        for (int i = 0; i < n; i++) { r[i] = left; left *= arr[i]; }
        long right = 1;
        for (int i = n - 1; i >= 0; i--) { r[i] *= right; right *= arr[i]; }
        return r;
    }

    // P4: Range Update
    static long[] solveP4(int n, int[][] updates) {
        long[] d = new long[n + 1];
        for (int[] u : updates) { d[u[0]] += u[2]; if (u[1] + 1 <= n) d[u[1] + 1] -= u[2]; }
        long[] r = new long[n]; long run = 0;
        for (int i = 0; i < n; i++) { run += d[i]; r[i] = run; }
        return r;
    }

    // P5: Kadane's
    static long solveP5(int[] arr) {
        if (arr.length == 0) return 0;
        long cur = arr[0], mx = arr[0];
        for (int i = 1; i < arr.length; i++) { cur = Math.max(cur + arr[i], arr[i]); mx = Math.max(mx, cur); }
        return mx;
    }

    // C1: 2D Prefix Sum
    static long[] solveC1(int[][] matrix, int[][] queries) {
        int rows = matrix.length, cols = matrix[0].length;
        long[][] p = new long[rows + 1][cols + 1];
        for (int i = 1; i <= rows; i++)
            for (int j = 1; j <= cols; j++)
                p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + matrix[i-1][j-1];
        long[] r = new long[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int r1 = queries[q][0], c1 = queries[q][1], r2 = queries[q][2], c2 = queries[q][3];
            r[q] = p[r2+1][c2+1] - p[r1][c2+1] - p[r2+1][c1] + p[r1][c1];
        }
        return r;
    }

    // C2: Max Subarray Three Ways
    static long solveC2Brute(int[] arr) {
        if (arr.length == 0) return 0;
        long mx = arr[0]; int n = arr.length;
        for (int l = 0; l < n; l++) for (int r = l; r < n; r++) {
            long t = 0; for (int k = l; k <= r; k++) t += arr[k]; mx = Math.max(mx, t);
        }
        return mx;
    }
    static long solveC2Prefix(int[] arr) {
        if (arr.length == 0) return 0;
        int n = arr.length; long[] p = new long[n + 1];
        for (int i = 0; i < n; i++) p[i+1] = p[i] + arr[i];
        long mx = arr[0];
        for (int l = 0; l < n; l++) for (int r = l; r < n; r++) mx = Math.max(mx, p[r+1] - p[l]);
        return mx;
    }
    static long solveC2Kadane(int[] arr) { return solveP5(arr); }

    // C3: Divisible by K
    static int solveC3(int[] arr, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1); long sum = 0; int count = 0;
        for (int x : arr) {
            sum += x;
            int rem = (int)(((sum % k) + k) % k);
            count += map.getOrDefault(rem, 0);
            map.put(rem, map.getOrDefault(rem, 0) + 1);
        }
        return count;
    }

    // C4: Min Ops Make Equal
    static long solveC4(int[] arr) {
        Arrays.sort(arr); int n = arr.length;
        if (n <= 1) return 0;
        long[] p = new long[n + 1];
        for (int i = 0; i < n; i++) p[i+1] = p[i] + arr[i];
        long min = Long.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            long lc = (long)i * arr[i] - p[i];
            long rc = (p[n] - p[i+1]) - (long)(n-i-1) * arr[i];
            min = Math.min(min, lc + rc);
        }
        return min;
    }

    // ── Test methods ────────────────────────────────────────────────

    static void testW1() {
        assertArrayEquals(new long[]{0,3,4,8,9,14}, solveW1(new int[]{3,1,4,1,5}), "W1: basic");
        assertArrayEquals(new long[]{0,5}, solveW1(new int[]{5}), "W1: single");
        assertArrayEquals(new long[]{0}, solveW1(new int[]{}), "W1: empty");
        assertArrayEquals(new long[]{0,-1,-3,-6}, solveW1(new int[]{-1,-2,-3}), "W1: negatives");
        assertArrayEquals(new long[]{0,1,0,2,0,3}, solveW1(new int[]{1,-1,2,-2,3}), "W1: mixed");
        assertArrayEquals(new long[]{0,0,0,0}, solveW1(new int[]{0,0,0}), "W1: zeros");
    }

    static void testW2() {
        assertArrayEquals(new long[]{23,10,1}, solveW2(new int[]{3,1,4,1,5,9}, new int[][]{{0,5},{2,4},{3,3}}), "W2: basic");
        assertArrayEquals(new long[]{10,20,30}, solveW2(new int[]{10,20,30}, new int[][]{{0,0},{1,1},{2,2}}), "W2: singles");
        assertArrayEquals(new long[]{15}, solveW2(new int[]{1,2,3,4,5}, new int[][]{{0,4}}), "W2: full");
        assertArrayEquals(new long[]{3,7}, solveW2(new int[]{1,2,3,4}, new int[][]{{0,1},{2,3}}), "W2: adjacent");
        assertArrayEquals(new long[]{3000000000L}, solveW2(new int[]{1000000000,1000000000,1000000000}, new int[][]{{0,2}}), "W2: large");
        assertArrayEquals(new long[]{2,8}, solveW2(new int[]{-5,3,-2,7,-1}, new int[][]{{0,4},{1,3}}), "W2: negatives");
    }

    static void testW3() {
        assertArrayEquals(new long[]{1,3,6,10}, solveW3(new int[]{1,2,3,4}), "W3: basic");
        assertArrayEquals(new long[]{5}, solveW3(new int[]{5}), "W3: single");
        assertArrayEquals(new long[]{}, solveW3(new int[]{}), "W3: empty");
        assertArrayEquals(new long[]{-1,-3,-6}, solveW3(new int[]{-1,-2,-3}), "W3: negatives");
        assertArrayEquals(new long[]{3,2,4,0,5}, solveW3(new int[]{3,-1,2,-4,5}), "W3: mixed");
        assertArrayEquals(new long[]{0,0,0}, solveW3(new int[]{0,0,0}), "W3: zeros");
    }

    static void testW4() {
        assertBoolEquals(true, solveW4(new int[]{1,2,3}, new int[]{1,2,3,4,5}), "W4: is prefix");
        assertBoolEquals(false, solveW4(new int[]{1,2,4}, new int[]{1,2,3,4,5}), "W4: not prefix");
        assertBoolEquals(true, solveW4(new int[]{}, new int[]{1,2,3}), "W4: empty prefix");
        assertBoolEquals(true, solveW4(new int[]{1,2,3}, new int[]{1,2,3}), "W4: equal");
        assertBoolEquals(false, solveW4(new int[]{1,2,3,4}, new int[]{1,2,3}), "W4: longer");
        assertBoolEquals(true, solveW4(new int[]{}, new int[]{}), "W4: both empty");
        assertBoolEquals(true, solveW4(new int[]{7}, new int[]{7,8,9}), "W4: single match");
        assertBoolEquals(false, solveW4(new int[]{7}, new int[]{8,9}), "W4: single no match");
    }

    static void testP1() {
        assertEquals(3, solveP1(new int[]{-7,1,5,2,-4,3,0}), "P1: basic");
        assertEquals(-1, solveP1(new int[]{1,2,3}), "P1: no equilibrium");
        assertEquals(0, solveP1(new int[]{0,1,-1}), "P1: at start");
        assertEquals(2, solveP1(new int[]{1,-1,0}), "P1: at end");
        assertEquals(0, solveP1(new int[]{42}), "P1: single");
        assertEquals(-1, solveP1(new int[]{1,1}), "P1: two elements");
        assertEquals(2, solveP1(new int[]{1,3,5,2,2}), "P1: another");
    }

    static void testP2() {
        assertEquals(2, solveP2(new int[]{1,1,1}, 2), "P2: basic");
        assertEquals(2, solveP2(new int[]{1,2,3}, 3), "P2: two ways");
        assertEquals(0, solveP2(new int[]{1}, 0), "P2: no match");
        assertEquals(3, solveP2(new int[]{1,-1,0}, 0), "P2: zeros");
        assertEquals(6, solveP2(new int[]{0,0,0}, 0), "P2: all zeros");
        assertEquals(1, solveP2(new int[]{1}, 1), "P2: single match");
        assertEquals(2, solveP2(new int[]{1,-2,3,-1}, -1), "P2: negative k");
    }

    static void testP3() {
        assertArrayEquals(new long[]{24,12,8,6}, solveP3(new int[]{1,2,3,4}), "P3: basic");
        assertArrayEquals(new long[]{0,0,9,0,0}, solveP3(new int[]{-1,1,0,-3,3}), "P3: with zero");
        assertArrayEquals(new long[]{5,3}, solveP3(new int[]{3,5}), "P3: two elements");
        assertArrayEquals(new long[]{6,3,2}, solveP3(new int[]{-1,-2,-3}), "P3: negatives");
        assertArrayEquals(new long[]{1,1,1,1}, solveP3(new int[]{1,1,1,1}), "P3: all ones");
        assertArrayEquals(new long[]{0,0,0}, solveP3(new int[]{0,0,1}), "P3: two zeros");
    }

    static void testP4() {
        assertArrayEquals(new long[]{-1,1,5,5,3}, solveP4(5, new int[][]{{1,3,2},{2,4,3},{0,1,-1}}), "P4: basic");
        assertArrayEquals(new long[]{5,5,5,5}, solveP4(4, new int[][]{{0,3,5}}), "P4: full range");
        assertArrayEquals(new long[]{10,10,0,0,20,20}, solveP4(6, new int[][]{{0,1,10},{4,5,20}}), "P4: non-overlapping");
        assertArrayEquals(new long[]{7,7,7}, solveP4(3, new int[][]{{0,2,7}}), "P4: full");
        assertArrayEquals(new long[]{0,0,100,0,0}, solveP4(5, new int[][]{{2,2,100}}), "P4: single element");
        assertArrayEquals(new long[]{10,5,5,10}, solveP4(4, new int[][]{{0,3,10},{1,2,-5}}), "P4: negative");
    }

    static void testP5() {
        assertEquals(6, solveP5(new int[]{-2,1,-3,4,-1,2,1,-5,4}), "P5: basic");
        assertEquals(-1, solveP5(new int[]{-5,-3,-1,-4}), "P5: all negative");
        assertEquals(1, solveP5(new int[]{1}), "P5: single");
        assertEquals(23, solveP5(new int[]{5,4,-1,7,8}), "P5: all positive-ish");
        assertEquals(-7, solveP5(new int[]{-7}), "P5: single negative");
        assertEquals(4, solveP5(new int[]{2,-1,2,-1,2}), "P5: alternating");
        assertEquals(30, solveP5(new int[]{10,-20,30}), "P5: large dip");
    }

    static void testC1() {
        assertArrayEquals(new long[]{45,28,1}, solveC1(new int[][]{{1,2,3},{4,5,6},{7,8,9}},
            new int[][]{{0,0,2,2},{1,1,2,2},{0,0,0,0}}), "C1: 3x3");
        assertArrayEquals(new long[]{5}, solveC1(new int[][]{{5}}, new int[][]{{0,0,0,0}}), "C1: single");
        assertArrayEquals(new long[]{10,5}, solveC1(new int[][]{{1,2,3,4}},
            new int[][]{{0,0,0,3},{0,1,0,2}}), "C1: single row");
        assertArrayEquals(new long[]{6,5}, solveC1(new int[][]{{1},{2},{3}},
            new int[][]{{0,0,2,0},{1,0,2,0}}), "C1: single col");
        assertArrayEquals(new long[]{10,3,7}, solveC1(new int[][]{{1,2},{3,4}},
            new int[][]{{0,0,1,1},{0,0,0,1},{1,0,1,1}}), "C1: 2x2");
        assertArrayEquals(new long[]{0}, solveC1(new int[][]{{-1,2},{3,-4}},
            new int[][]{{0,0,1,1}}), "C1: negatives");
    }

    static void testC2() {
        int[] arr1 = {-2,1,-3,4,-1,2,1,-5,4};
        assertEquals(6, solveC2Brute(arr1), "C2 brute: basic");
        assertEquals(6, solveC2Prefix(arr1), "C2 prefix: basic");
        assertEquals(6, solveC2Kadane(arr1), "C2 kadane: basic");
        int[] arr2 = {-5,-3,-1,-4};
        assertEquals(-1, solveC2Brute(arr2), "C2 brute: all neg");
        assertEquals(-1, solveC2Prefix(arr2), "C2 prefix: all neg");
        assertEquals(-1, solveC2Kadane(arr2), "C2 kadane: all neg");
        int[] arr3 = {7};
        assertEquals(7, solveC2Brute(arr3), "C2 brute: single");
        assertEquals(7, solveC2Prefix(arr3), "C2 prefix: single");
        assertEquals(7, solveC2Kadane(arr3), "C2 kadane: single");
        int[] arr4 = {1,2,3};
        assertEquals(6, solveC2Brute(arr4), "C2 brute: all pos");
        assertEquals(6, solveC2Prefix(arr4), "C2 prefix: all pos");
        assertEquals(6, solveC2Kadane(arr4), "C2 kadane: all pos");
        int[] arr5 = {5,-9,6,-2,3};
        assertEquals(7, solveC2Brute(arr5), "C2 brute: mixed");
        assertEquals(7, solveC2Prefix(arr5), "C2 prefix: mixed");
        assertEquals(7, solveC2Kadane(arr5), "C2 kadane: mixed");
    }

    static void testC3() {
        assertEquals(7, solveC3(new int[]{4,5,0,-2,-3,1}, 5), "C3: basic");
        assertEquals(0, solveC3(new int[]{5}, 9), "C3: no match");
        assertEquals(6, solveC3(new int[]{5,10,15}, 5), "C3: all divisible");
        assertEquals(2, solveC3(new int[]{-1,2,9}, 2), "C3: negative");
        assertEquals(1, solveC3(new int[]{0}, 1), "C3: single zero");
        assertEquals(6, solveC3(new int[]{1,2,3}, 1), "C3: k=1");
    }

    static void testC4() {
        assertEquals(2, solveC4(new int[]{1,2,3}), "C4: basic");
        assertEquals(0, solveC4(new int[]{5}), "C4: single");
        assertEquals(0, solveC4(new int[]{3,3,3}), "C4: equal");
        assertEquals(4, solveC4(new int[]{1,5}), "C4: two elements");
        assertEquals(16, solveC4(new int[]{1,2,9,10}), "C4: larger");
        assertEquals(4, solveC4(new int[]{-5,-3,-1}), "C4: negatives");
        assertEquals(99, solveC4(new int[]{1,100}), "C4: spread");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 14: Prefix Sums — The Running Total Trick");
        System.out.println("===================================================\n");

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
