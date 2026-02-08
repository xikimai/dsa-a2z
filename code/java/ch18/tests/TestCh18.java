package ch18.tests;

import java.util.*;

/**
 * Tests for Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * Build and run:
 *   cd code/java
 *   javac ch18/tests/TestCh18.java
 *   java -ea ch18.tests.TestCh18
 */
public class TestCh18 {

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

    static void assertDoubleEquals(double expected, double actual, double tol, String msg) {
        if (Math.abs(expected - actual) < tol) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertArrayEquals(int[] expected, int[] actual, String msg) {
        if (Arrays.equals(expected, actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected) + ", got " + Arrays.toString(actual)); }
    }

    static void assert2DArrayEquals(int[][] expected, int[][] actual, String msg) {
        if (Arrays.deepEquals(expected, actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + Arrays.deepToString(expected) + ", got " + Arrays.deepToString(actual)); }
    }

    // ── Reference solutions ─────────────────────────────────────────

    // W1: Assign Cookies
    static int refW1(int[] greed, int[] cookies) {
        Arrays.sort(greed); Arrays.sort(cookies);
        int c = 0, k = 0;
        while (c < greed.length && k < cookies.length) {
            if (cookies[k] >= greed[c]) c++;
            k++;
        }
        return c;
    }

    // W2: Jump Game
    static boolean refW2(int[] nums) {
        int mr = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > mr) return false;
            mr = Math.max(mr, i + nums[i]);
        }
        return true;
    }

    // W3: Buy Sell Stock
    static int refW3(int[] prices) {
        if (prices.length < 2) return 0;
        int mn = prices[0], mx = 0;
        for (int i = 1; i < prices.length; i++) {
            mx = Math.max(mx, prices[i] - mn);
            mn = Math.min(mn, prices[i]);
        }
        return mx;
    }

    // W4: Lemonade Change
    static boolean refW4(int[] bills) {
        int f = 0, t = 0;
        for (int b : bills) {
            if (b == 5) f++;
            else if (b == 10) { if (f == 0) return false; f--; t++; }
            else { if (t > 0 && f > 0) { t--; f--; } else if (f >= 3) f -= 3; else return false; }
        }
        return true;
    }

    // P1: Activity Selection
    static int refP1(int[][] a) {
        if (a.length == 0) return 0;
        Arrays.sort(a, (x, y) -> Integer.compare(x[1], y[1]));
        int c = 0, le = 0;
        for (int[] act : a) { if (act[0] >= le) { c++; le = act[1]; } }
        return c;
    }

    // P2: Fractional Knapsack
    static double refP2(int cap, int[][] items) {
        if (cap == 0 || items.length == 0) return 0.0;
        Arrays.sort(items, (a, b) -> Double.compare((double)b[1]/b[0], (double)a[1]/a[0]));
        double tv = 0; int rem = cap;
        for (int[] it : items) {
            if (rem <= 0) break;
            int take = Math.min(it[0], rem);
            tv += take * ((double)it[1] / it[0]);
            rem -= take;
        }
        return tv;
    }

    // P3: Merge Intervals
    static int[][] refP3(int[][] iv) {
        if (iv.length == 0) return new int[0][];
        Arrays.sort(iv, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> m = new ArrayList<>();
        m.add(iv[0].clone());
        for (int i = 1; i < iv.length; i++) {
            int[] last = m.get(m.size() - 1);
            if (iv[i][0] <= last[1]) last[1] = Math.max(last[1], iv[i][1]);
            else m.add(iv[i].clone());
        }
        return m.toArray(new int[0][]);
    }

    // P4: Non-overlapping Intervals
    static int refP4(int[][] iv) {
        if (iv.length == 0) return 0;
        Arrays.sort(iv, (a, b) -> Integer.compare(a[1], b[1]));
        int keep = 0, le = Integer.MIN_VALUE;
        for (int[] x : iv) { if (x[0] >= le) { keep++; le = x[1]; } }
        return iv.length - keep;
    }

    // P5: Jump Game II
    static int refP5(int[] nums) {
        if (nums.length <= 1) return 0;
        int j = 0, ce = 0, f = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            f = Math.max(f, i + nums[i]);
            if (i == ce) { j++; ce = f; if (ce >= nums.length - 1) break; }
        }
        return j;
    }

    // C1: Job Sequencing
    static int[] refC1(int[][] jobs) {
        if (jobs.length == 0) return new int[]{0, 0};
        Arrays.sort(jobs, (a, b) -> Integer.compare(b[2], a[2]));
        int md = 0;
        for (int[] j : jobs) md = Math.max(md, j[1]);
        boolean[] s = new boolean[md + 1];
        int c = 0, tp = 0;
        for (int[] job : jobs) {
            for (int t = job[1]; t >= 1; t--) {
                if (!s[t]) { s[t] = true; c++; tp += job[2]; break; }
            }
        }
        return new int[]{c, tp};
    }

    // C2: Gas Station
    static int refC2(int[] gas, int[] cost) {
        int tg = 0, tc = 0;
        for (int i = 0; i < gas.length; i++) { tg += gas[i]; tc += cost[i]; }
        if (tg < tc) return -1;
        int start = 0, tank = 0;
        for (int i = 0; i < gas.length; i++) {
            tank += gas[i] - cost[i];
            if (tank < 0) { start = i + 1; tank = 0; }
        }
        return start;
    }

    // C3: Min Platforms
    static int refC3(int[] arr, int[] dep) {
        if (arr.length == 0) return 0;
        Arrays.sort(arr); Arrays.sort(dep);
        int p = 0, mx = 0, i = 0, j = 0, n = arr.length;
        while (i < n) {
            if (arr[i] <= dep[j]) { p++; mx = Math.max(mx, p); i++; }
            else { p--; j++; }
        }
        return mx;
    }

    // C4: Candy
    static int refC4(int[] ratings) {
        int n = ratings.length;
        if (n == 0) return 0;
        int[] c = new int[n];
        Arrays.fill(c, 1);
        for (int i = 1; i < n; i++) if (ratings[i] > ratings[i-1]) c[i] = c[i-1] + 1;
        for (int i = n-2; i >= 0; i--) if (ratings[i] > ratings[i+1]) c[i] = Math.max(c[i], c[i+1] + 1);
        int s = 0; for (int x : c) s += x; return s;
    }

    // ── Test methods ────────────────────────────────────────────────

    static void testW1() {
        assertEquals(1, refW1(new int[]{1,2,3}, new int[]{1,1}), "W1: basic");
        assertEquals(2, refW1(new int[]{1,2}, new int[]{1,2,3}), "W1: all");
        assertEquals(0, refW1(new int[]{10,9}, new int[]{1,2}), "W1: none");
        assertEquals(2, refW1(new int[]{10,9,8,7}, new int[]{5,6,7,8}), "W1: partial");
        assertEquals(0, refW1(new int[]{}, new int[]{1,2}), "W1: empty children");
        assertEquals(0, refW1(new int[]{1,2}, new int[]{}), "W1: empty cookies");
        assertEquals(1, refW1(new int[]{1}, new int[]{1}), "W1: single");
        assertEquals(1, refW1(new int[]{1,2,3}, new int[]{3}), "W1: one big cookie");
    }

    static void testW2() {
        assertBoolEquals(true, refW2(new int[]{2,3,1,1,4}), "W2: reachable");
        assertBoolEquals(false, refW2(new int[]{3,2,1,0,4}), "W2: unreachable");
        assertBoolEquals(true, refW2(new int[]{0}), "W2: single");
        assertBoolEquals(true, refW2(new int[]{1,0}), "W2: two ok");
        assertBoolEquals(false, refW2(new int[]{0,1}), "W2: two fail");
        assertBoolEquals(true, refW2(new int[]{1,1,1,1}), "W2: all ones");
        assertBoolEquals(true, refW2(new int[]{5,0,0,0,0,0}), "W2: big jump");
        assertBoolEquals(true, refW2(new int[]{2,0,0}), "W2: zeros mid");
    }

    static void testW3() {
        assertEquals(5, refW3(new int[]{7,1,5,3,6,4}), "W3: basic");
        assertEquals(0, refW3(new int[]{7,6,4,3,1}), "W3: decreasing");
        assertEquals(0, refW3(new int[]{5}), "W3: single");
        assertEquals(2, refW3(new int[]{2,4}), "W3: two profit");
        assertEquals(0, refW3(new int[]{4,2}), "W3: two no profit");
        assertEquals(0, refW3(new int[]{3,3,3}), "W3: same");
        assertEquals(4, refW3(new int[]{1,2,3,4,5}), "W3: increasing");
        assertEquals(9, refW3(new int[]{10,1,10}), "W3: valley");
    }

    static void testW4() {
        assertBoolEquals(true, refW4(new int[]{5,5,5,10,20}), "W4: basic true");
        assertBoolEquals(false, refW4(new int[]{5,5,10,10,20}), "W4: basic false");
        assertBoolEquals(true, refW4(new int[]{5,5,5}), "W4: all fives");
        assertBoolEquals(true, refW4(new int[]{5}), "W4: single five");
        assertBoolEquals(false, refW4(new int[]{10}), "W4: ten no change");
        assertBoolEquals(false, refW4(new int[]{20}), "W4: twenty no change");
        assertBoolEquals(true, refW4(new int[]{5,5,10,5,5,20}), "W4: complex");
        assertBoolEquals(true, refW4(new int[]{5,5,5,20}), "W4: three fives twenty");
    }

    static void testP1() {
        assertEquals(4, refP1(new int[][]{{1,2},{3,4},{0,6},{5,7},{8,9},{5,9}}), "P1: basic");
        assertEquals(2, refP1(new int[][]{{1,3},{2,5},{4,7},{6,8}}), "P1: overlap");
        assertEquals(3, refP1(new int[][]{{1,2},{3,4},{5,6}}), "P1: no overlap");
        assertEquals(1, refP1(new int[][]{{1,10},{2,10},{3,10}}), "P1: all overlap");
        assertEquals(1, refP1(new int[][]{{0,5}}), "P1: single");
        assertEquals(0, refP1(new int[][]{}), "P1: empty");
        assertEquals(4, refP1(new int[][]{{0,1},{1,2},{2,3},{3,4}}), "P1: touching");
    }

    static void testP2() {
        assertDoubleEquals(240.0, refP2(50, new int[][]{{10,60},{20,100},{30,120}}), 1e-6, "P2: basic");
        assertDoubleEquals(160.0, refP2(30, new int[][]{{10,60},{20,100}}), 1e-6, "P2: exact");
        assertDoubleEquals(85.0, refP2(15, new int[][]{{10,60},{20,100}}), 1e-6, "P2: partial");
        assertDoubleEquals(0.0, refP2(0, new int[][]{{10,60}}), 1e-6, "P2: zero cap");
        assertDoubleEquals(50.0, refP2(100, new int[][]{{10,50}}), 1e-6, "P2: excess cap");
        assertDoubleEquals(25.0, refP2(5, new int[][]{{10,50}}), 1e-6, "P2: half item");
        assertDoubleEquals(0.0, refP2(10, new int[][]{}), 1e-6, "P2: empty");
    }

    static void testP3() {
        assert2DArrayEquals(new int[][]{{1,6},{8,10},{15,18}}, refP3(new int[][]{{1,3},{2,6},{8,10},{15,18}}), "P3: basic");
        assert2DArrayEquals(new int[][]{{1,5}}, refP3(new int[][]{{1,4},{4,5}}), "P3: touching");
        assert2DArrayEquals(new int[][]{{1,4}}, refP3(new int[][]{{1,4},{2,3}}), "P3: contained");
        assert2DArrayEquals(new int[][]{{1,2},{5,6},{9,10}}, refP3(new int[][]{{1,2},{5,6},{9,10}}), "P3: no overlap");
        assert2DArrayEquals(new int[][]{{1,5}}, refP3(new int[][]{{1,5},{1,5},{1,5}}), "P3: all same");
        assert2DArrayEquals(new int[][]{{1,10}}, refP3(new int[][]{{1,10}}), "P3: single");
        assert2DArrayEquals(new int[][]{{0,4}}, refP3(new int[][]{{1,4},{0,4}}), "P3: unsorted");
        assert2DArrayEquals(new int[][]{}, refP3(new int[][]{}), "P3: empty");
    }

    static void testP4() {
        assertEquals(1, refP4(new int[][]{{1,2},{2,3},{3,4},{1,3}}), "P4: basic");
        assertEquals(2, refP4(new int[][]{{1,2},{1,2},{1,2}}), "P4: all same");
        assertEquals(0, refP4(new int[][]{{1,2},{2,3}}), "P4: no overlap");
        assertEquals(2, refP4(new int[][]{{1,5},{2,6},{3,7}}), "P4: all overlap");
        assertEquals(0, refP4(new int[][]{{1,2}}), "P4: single");
        assertEquals(1, refP4(new int[][]{{1,100},{2,3},{4,5},{6,7}}), "P4: nested");
        assertEquals(0, refP4(new int[][]{}), "P4: empty");
    }

    static void testP5() {
        assertEquals(2, refP5(new int[]{2,3,1,1,4}), "P5: basic");
        assertEquals(2, refP5(new int[]{2,3,0,1,4}), "P5: zeros");
        assertEquals(0, refP5(new int[]{1}), "P5: single");
        assertEquals(1, refP5(new int[]{1,1}), "P5: two");
        assertEquals(1, refP5(new int[]{10,0,0,0,0}), "P5: big jump");
        assertEquals(4, refP5(new int[]{1,1,1,1,1}), "P5: all ones");
        assertEquals(1, refP5(new int[]{4,3,2,1,0}), "P5: decreasing");
    }

    static void testC1() {
        assertArrayEquals(new int[]{2,60}, refC1(new int[][]{{1,4,20},{2,1,10},{3,1,40},{4,1,30}}), "C1: basic");
        assertArrayEquals(new int[]{2,127}, refC1(new int[][]{{1,2,100},{2,1,19},{3,2,27},{4,1,25},{5,1,15}}), "C1: five");
        assertArrayEquals(new int[]{1,30}, refC1(new int[][]{{1,1,10},{2,1,20},{3,1,30}}), "C1: same deadline");
        assertArrayEquals(new int[]{3,60}, refC1(new int[][]{{1,1,10},{2,2,20},{3,3,30}}), "C1: all fit");
        assertArrayEquals(new int[]{1,50}, refC1(new int[][]{{1,1,50}}), "C1: single");
        assertArrayEquals(new int[]{0,0}, refC1(new int[][]{}), "C1: empty");
    }

    static void testC2() {
        assertEquals(3, refC2(new int[]{1,2,3,4,5}, new int[]{3,4,5,1,2}), "C2: basic");
        assertEquals(-1, refC2(new int[]{2,3,4}, new int[]{3,4,3}), "C2: impossible");
        assertEquals(4, refC2(new int[]{5,1,2,3,4}, new int[]{4,4,1,5,1}), "C2: start last");
        assertEquals(0, refC2(new int[]{5}, new int[]{4}), "C2: single ok");
        assertEquals(-1, refC2(new int[]{3}, new int[]{5}), "C2: single fail");
        assertEquals(0, refC2(new int[]{3,1,1}, new int[]{1,2,2}), "C2: start zero");
        assertEquals(0, refC2(new int[]{3,3,3}, new int[]{3,3,3}), "C2: equal");
    }

    static void testC3() {
        assertEquals(3, refC3(new int[]{900,940,950,1100,1500,1800}, new int[]{910,1200,1120,1130,1900,2000}), "C3: basic");
        assertEquals(1, refC3(new int[]{900,1100,1235}, new int[]{1000,1200,1240}), "C3: no overlap");
        assertEquals(3, refC3(new int[]{100,100,100}, new int[]{200,200,200}), "C3: all overlap");
        assertEquals(1, refC3(new int[]{900}, new int[]{1000}), "C3: single");
        assertEquals(2, refC3(new int[]{900,940}, new int[]{1000,950}), "C3: two overlap");
        assertEquals(1, refC3(new int[]{100,200,300}, new int[]{150,250,350}), "C3: sequential");
        assertEquals(0, refC3(new int[]{}, new int[]{}), "C3: empty");
    }

    static void testC4() {
        assertEquals(5, refC4(new int[]{1,0,2}), "C4: basic");
        assertEquals(4, refC4(new int[]{1,2,2}), "C4: equal neighbor");
        assertEquals(6, refC4(new int[]{3,2,1}), "C4: decreasing");
        assertEquals(6, refC4(new int[]{1,2,3}), "C4: increasing");
        assertEquals(1, refC4(new int[]{5}), "C4: single");
        assertEquals(2, refC4(new int[]{1,1}), "C4: two same");
        assertEquals(7, refC4(new int[]{1,3,2,2,1}), "C4: valley");
        assertEquals(4, refC4(new int[]{5,5,5,5}), "C4: all same");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 18: Greedy Algorithms — The Smart Shortcut");
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
