package ch17.tests;

import java.util.*;

/**
 * Tests for Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * Build and run:
 *   cd code/java
 *   javac ch17/tests/TestCh17.java
 *   java -ea ch17.tests.TestCh17
 */
public class TestCh17 {

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

    static void assertArrayEquals(int[] expected, int[] actual, String msg) {
        if (Arrays.equals(expected, actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + Arrays.toString(expected) + ", got " + Arrays.toString(actual)); }
    }

    static void assertListEquals(List<Integer> expected, List<Integer> actual, String msg) {
        if (expected.equals(actual)) { passed++; }
        else { failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); }
    }

    static void assertDoubleListEquals(List<Double> expected, List<Double> actual, String msg) {
        if (expected.size() != actual.size()) {
            failed++; System.out.println("FAIL: " + msg + " — size mismatch"); return;
        }
        for (int i = 0; i < expected.size(); i++) {
            if (Math.abs(expected.get(i) - actual.get(i)) > 0.01) {
                failed++; System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual); return;
            }
        }
        passed++;
    }

    static void assertStringValid(String original, String result, String msg) {
        if (result.isEmpty()) {
            // Check if impossible
            int[] freq = new int[26];
            for (char c : original.toCharArray()) freq[c - 'a']++;
            int maxF = 0;
            for (int f : freq) maxF = Math.max(maxF, f);
            if (maxF > (original.length() + 1) / 2) { passed++; return; }
            failed++; System.out.println("FAIL: " + msg + " — returned empty but solution exists"); return;
        }
        // Check same chars
        char[] a = original.toCharArray(), b = result.toCharArray();
        Arrays.sort(a); Arrays.sort(b);
        if (!Arrays.equals(a, b)) { failed++; System.out.println("FAIL: " + msg + " — chars mismatch"); return; }
        // Check no adjacent same
        for (int i = 1; i < result.length(); i++) {
            if (result.charAt(i) == result.charAt(i-1)) {
                failed++; System.out.println("FAIL: " + msg + " — adjacent same at " + i); return;
            }
        }
        passed++;
    }

    // ── Reference solutions ─────────────────────────────────────────

    static int solveW1(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int n : nums) { pq.add(n); if (pq.size() > k) pq.poll(); }
        return pq.peek();
    }

    static int[] solveW2(int[] arr) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int x : arr) pq.add(x);
        int[] r = new int[arr.length];
        for (int i = 0; i < r.length; i++) r[i] = pq.poll();
        return r;
    }

    static int solveW3(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : stones) pq.add(s);
        while (pq.size() > 1) {
            int a = pq.poll(), b = pq.poll();
            if (a != b) pq.add(a - b);
        }
        return pq.isEmpty() ? 0 : pq.peek();
    }

    static boolean solveW4(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n / 2; i++) {
            int l = 2*i+1, r = 2*i+2;
            if (l < n && arr[i] > arr[l]) return false;
            if (r < n && arr[i] > arr[r]) return false;
        }
        return true;
    }

    static List<Integer> solveP1(int[] nums, int k) {
        HashMap<Integer,Integer> freq = new HashMap<>();
        for (int n : nums) freq.put(n, freq.getOrDefault(n,0)+1);
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)->freq.get(a)-freq.get(b));
        for (int key : freq.keySet()) { pq.add(key); if (pq.size() > k) pq.poll(); }
        List<Integer> r = new ArrayList<>(pq);
        Collections.sort(r);
        return r;
    }

    static List<Integer> solveP2(int[][] arrays) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->Integer.compare(a[0],b[0]));
        for (int i = 0; i < arrays.length; i++)
            if (arrays[i].length > 0) pq.add(new int[]{arrays[i][0], i, 0});
        List<Integer> r = new ArrayList<>();
        while (!pq.isEmpty()) {
            int[] t = pq.poll(); r.add(t[0]);
            if (t[2]+1 < arrays[t[1]].length) pq.add(new int[]{arrays[t[1]][t[2]+1], t[1], t[2]+1});
        }
        return r;
    }

    static int solveP3(int[][] matrix, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->Integer.compare(a[0],b[0]));
        for (int r = 0; r < matrix.length; r++) pq.add(new int[]{matrix[r][0], r, 0});
        int val = 0;
        for (int i = 0; i < k; i++) {
            int[] t = pq.poll(); val = t[0];
            if (t[2]+1 < matrix[t[1]].length) pq.add(new int[]{matrix[t[1]][t[2]+1], t[1], t[2]+1});
        }
        return val;
    }

    static List<Double> solveP4(int[] nums) {
        PriorityQueue<Integer> maxH = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minH = new PriorityQueue<>();
        List<Double> medians = new ArrayList<>();
        for (int num : nums) {
            maxH.add(num);
            if (!minH.isEmpty() && maxH.peek() > minH.peek()) minH.add(maxH.poll());
            if (maxH.size() > minH.size()+1) minH.add(maxH.poll());
            else if (minH.size() > maxH.size()) maxH.add(minH.poll());
            if (maxH.size() > minH.size()) medians.add((double)maxH.peek());
            else medians.add((maxH.peek()+minH.peek())/2.0);
        }
        return medians;
    }

    static int solveC2(char[] tasks, int n) {
        int[] freq = new int[26];
        for (char t : tasks) freq[t-'A']++;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int f : freq) if (f > 0) pq.add(f);
        int time = 0;
        while (!pq.isEmpty()) {
            int cycle = n+1; List<Integer> temp = new ArrayList<>(); int done = 0;
            for (int i = 0; i < cycle; i++) {
                if (!pq.isEmpty()) { int c = pq.poll(); if (c>1) temp.add(c-1); done++; }
            }
            for (int t : temp) pq.add(t);
            time += pq.isEmpty() ? done : cycle;
        }
        return time;
    }

    static int[] solveC3(int[] nums, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        int[] r = new int[nums.length - k + 1]; int ri = 0;
        for (int i = 0; i < nums.length; i++) {
            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();
            dq.addLast(i);
            if (dq.peekFirst() <= i - k) dq.pollFirst();
            if (i >= k-1) r[ri++] = nums[dq.peekFirst()];
        }
        return r;
    }

    // ── Test methods ────────────────────────────────────────────────

    static void testW1() {
        assertEquals(5, solveW1(new int[]{3,2,1,5,6,4}, 2), "W1: basic");
        assertEquals(4, solveW1(new int[]{3,2,3,1,2,4,5,5,6}, 4), "W1: duplicates");
        assertEquals(1, solveW1(new int[]{1}, 1), "W1: single");
        assertEquals(1, solveW1(new int[]{7,6,5,4,3,2,1}, 7), "W1: k=n");
        assertEquals(5, solveW1(new int[]{5,5,5,5}, 2), "W1: all same");
        assertEquals(-2, solveW1(new int[]{-1,-2,-3,-4,-5}, 2), "W1: negative");
    }

    static void testW2() {
        assertArrayEquals(new int[]{1,2,3,5,8}, solveW2(new int[]{5,3,8,1,2}), "W2: basic");
        assertArrayEquals(new int[]{1,2,3,4,5}, solveW2(new int[]{1,2,3,4,5}), "W2: sorted");
        assertArrayEquals(new int[]{1,2,3,4,5}, solveW2(new int[]{5,4,3,2,1}), "W2: reverse");
        assertArrayEquals(new int[]{1}, solveW2(new int[]{1}), "W2: single");
        assertArrayEquals(new int[]{}, solveW2(new int[]{}), "W2: empty");
        assertArrayEquals(new int[]{1,1,2,3,3}, solveW2(new int[]{3,1,3,1,2}), "W2: dups");
    }

    static void testW3() {
        assertEquals(1, solveW3(new int[]{2,7,4,1,8,1}), "W3: basic");
        assertEquals(1, solveW3(new int[]{1}), "W3: single");
        assertEquals(0, solveW3(new int[]{3,3}), "W3: equal");
        assertEquals(4, solveW3(new int[]{3,7}), "W3: two diff");
        assertEquals(0, solveW3(new int[]{5,5,5,5}), "W3: all equal");
    }

    static void testW4() {
        assertBoolEquals(true, solveW4(new int[]{1,3,2,7,6,5,4}), "W4: valid");
        assertBoolEquals(true, solveW4(new int[]{1,2,3,4,5,6,7}), "W4: sorted");
        assertBoolEquals(false, solveW4(new int[]{7,3,2,1,6,5,4}), "W4: invalid");
        assertBoolEquals(true, solveW4(new int[]{5}), "W4: single");
        assertBoolEquals(true, solveW4(new int[]{}), "W4: empty");
        assertBoolEquals(true, solveW4(new int[]{1,2}), "W4: two valid");
        assertBoolEquals(false, solveW4(new int[]{2,1}), "W4: two invalid");
    }

    static void testP1() {
        assertListEquals(Arrays.asList(1,2), solveP1(new int[]{1,1,1,2,2,3}, 2), "P1: basic");
        assertListEquals(Arrays.asList(1), solveP1(new int[]{1}, 1), "P1: single");
        assertListEquals(Arrays.asList(5), solveP1(new int[]{5,5,5,5}, 1), "P1: all same");
        assertListEquals(Arrays.asList(-1,2), solveP1(new int[]{4,1,-1,2,-1,2,3}, 2), "P1: larger");
    }

    static void testP2() {
        assertListEquals(Arrays.asList(1,2,3,4,5,6,7,8,9),
                solveP2(new int[][]{{1,4,7},{2,5,8},{3,6,9}}), "P2: three arrays");
        assertListEquals(Arrays.asList(1,2,3,4,5,6),
                solveP2(new int[][]{{1,3,5},{2,4,6}}), "P2: two arrays");
        assertListEquals(Arrays.asList(1), solveP2(new int[][]{{},{1}}), "P2: with empty");
        assertListEquals(new ArrayList<>(), solveP2(new int[][]{{},{}}), "P2: all empty");
        assertListEquals(Arrays.asList(1,2,3), solveP2(new int[][]{{1,2,3}}), "P2: single");
        assertListEquals(new ArrayList<>(), solveP2(new int[][]{}), "P2: no arrays");
    }

    static void testP3() {
        assertEquals(13, solveP3(new int[][]{{1,5,9},{10,11,13},{12,13,15}}, 8), "P3: basic k=8");
        assertEquals(-5, solveP3(new int[][]{{-5}}, 1), "P3: single");
        assertEquals(1, solveP3(new int[][]{{1,2},{3,4}}, 1), "P3: first");
        assertEquals(4, solveP3(new int[][]{{1,2},{3,4}}, 4), "P3: last");
        assertEquals(11, solveP3(new int[][]{{1,5,9},{10,11,13},{12,13,15}}, 5), "P3: k=5");
    }

    static void testP4() {
        assertDoubleListEquals(Arrays.asList(5.0,10.0,5.0,4.0), solveP4(new int[]{5,15,1,3}), "P4: basic");
        assertDoubleListEquals(Arrays.asList(2.0,2.5,3.0), solveP4(new int[]{2,3,4}), "P4: ascending");
        assertDoubleListEquals(Arrays.asList(1.0), solveP4(new int[]{1}), "P4: single");
        assertDoubleListEquals(Arrays.asList(1.0,1.5), solveP4(new int[]{1,2}), "P4: two");
        assertDoubleListEquals(Arrays.asList(5.0,4.5,4.0,3.5,3.0), solveP4(new int[]{5,4,3,2,1}), "P4: desc");
        assertDoubleListEquals(Arrays.asList(7.0,7.0,7.0,7.0), solveP4(new int[]{7,7,7,7}), "P4: same");
    }

    static void testC1() {
        assertStringValid("aab", solveReorganize("aab"), "C1: aab");
        assertStringValid("aaab", solveReorganize("aaab"), "C1: impossible");
        assertStringValid("a", solveReorganize("a"), "C1: single");
        assertStringValid("aaabbbccc", solveReorganize("aaabbbccc"), "C1: longer");
        assertStringValid("aaaa", solveReorganize("aaaa"), "C1: all same");
    }

    static String solveReorganize(String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c-'a']++;
        int max = 0; for (int f : freq) max = Math.max(max, f);
        if (max > (s.length()+1)/2) return "";
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->b[0]-a[0]);
        for (int i = 0; i < 26; i++) if (freq[i]>0) pq.add(new int[]{freq[i],i});
        StringBuilder sb = new StringBuilder();
        int[] prev = {0,-1};
        while (!pq.isEmpty()) {
            int[] cur = pq.poll(); sb.append((char)(cur[1]+'a'));
            if (prev[0]>0) pq.add(prev);
            prev = new int[]{cur[0]-1, cur[1]};
        }
        return sb.toString();
    }

    static void testC2() {
        assertEquals(8, solveC2(new char[]{'A','A','A','B','B','B'}, 2), "C2: basic");
        assertEquals(6, solveC2(new char[]{'A','A','A','B','B','B'}, 0), "C2: no cooldown");
        assertEquals(16, solveC2(new char[]{'A','A','A','A','A','A','B','C','D','E'}, 2), "C2: large cd");
        assertEquals(1, solveC2(new char[]{'A'}, 2), "C2: single");
        assertEquals(4, solveC2(new char[]{'A','B','C','D'}, 2), "C2: all diff");
        assertEquals(4, solveC2(new char[]{'A','A'}, 2), "C2: two same");
    }

    static void testC3() {
        assertArrayEquals(new int[]{3,3,5,5,6,7}, solveC3(new int[]{1,3,-1,-3,5,3,6,7}, 3), "C3: basic");
        assertArrayEquals(new int[]{1}, solveC3(new int[]{1}, 1), "C3: single");
        assertArrayEquals(new int[]{1}, solveC3(new int[]{1,-1}, 2), "C3: k=n");
        assertArrayEquals(new int[]{3,4,5}, solveC3(new int[]{1,2,3,4,5}, 3), "C3: ascending");
        assertArrayEquals(new int[]{5,4,3}, solveC3(new int[]{5,4,3,2,1}, 3), "C3: descending");
        assertArrayEquals(new int[]{2,2,2}, solveC3(new int[]{2,2,2,2}, 2), "C3: all same");
    }

    public static void main(String[] args) {
        System.out.println("Chapter 17: Heaps & Priority Queues — The VIP Line");
        System.out.println("===================================================\n");

        testW1();
        testW2();
        testW3();
        testW4();
        testP1();
        testP2();
        testP3();
        testP4();
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
