package ch11.tests;

import java.util.*;

/**
 * Tests for Chapter 11: Hashing — The Secret Decoder Ring
 *
 * Build and run:
 *   cd code/java
 *   javac ch11/tests/TestCh11.java
 *   java -ea ch11.tests.TestCh11
 */
public class TestCh11 {

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

    static void assertStringEquals(String expected, String actual, String msg) {
        if (expected.equals(actual)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected \"" + expected + "\", got \"" + actual + "\"");
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

    static void assertListIntArrayEquals(List<int[]> expected, List<int[]> actual, String msg) {
        if (expected.size() != actual.size()) {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + expected.size() + " items, got " + actual.size());
            return;
        }
        for (int i = 0; i < expected.size(); i++) {
            if (!Arrays.equals(expected.get(i), actual.get(i))) {
                failed++;
                System.out.println("FAIL: " + msg + " — mismatch at index " + i
                    + ": expected " + Arrays.toString(expected.get(i))
                    + ", got " + Arrays.toString(actual.get(i)));
                return;
            }
        }
        passed++;
    }

    static void assertListEquals(List<Integer> expected, List<Integer> actual, String msg) {
        if (expected.equals(actual)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + expected + ", got " + actual);
        }
    }

    static void assertNestedListEquals(List<List<String>> expected, List<List<String>> actual, String msg) {
        if (expected.size() != actual.size()) {
            failed++;
            System.out.println("FAIL: " + msg + " — expected " + expected.size() + " groups, got " + actual.size());
            return;
        }
        for (int i = 0; i < expected.size(); i++) {
            if (!expected.get(i).equals(actual.get(i))) {
                failed++;
                System.out.println("FAIL: " + msg + " — mismatch at group " + i
                    + "\n  expected: " + expected + "\n  actual:   " + actual);
                return;
            }
        }
        passed++;
    }

    // ── Reference solutions ─────────────────────────────────────────

    // W1: Frequency Count
    static List<int[]> solveW1FreqCount(int[] arr) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int x : arr) {
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        }
        List<int[]> result = new ArrayList<>();
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            result.add(new int[]{e.getKey(), e.getValue()});
        }
        result.sort((a, b) -> Integer.compare(a[0], b[0]));
        return result;
    }

    // W2: Highest and Lowest Frequency
    static int[] solveW2HighestLowestFreq(int[] arr) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int x : arr) {
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        }
        int maxFreq = Integer.MIN_VALUE, minFreq = Integer.MAX_VALUE;
        int maxElem = 0, minElem = 0;
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            if (e.getValue() > maxFreq) { maxFreq = e.getValue(); maxElem = e.getKey(); }
            if (e.getValue() < minFreq) { minFreq = e.getValue(); minElem = e.getKey(); }
        }
        return new int[]{maxElem, minElem};
    }

    // W3: First Non-Repeating Character
    static String solveW3FirstNonRepeating(String s) {
        if (s.isEmpty()) return "_";
        HashMap<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        for (char c : s.toCharArray()) {
            if (freq.get(c) == 1) return String.valueOf(c);
        }
        return "_";
    }

    // W4: Valid Anagram
    static boolean solveW4ValidAnagram(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        HashMap<Character, Integer> freq = new HashMap<>();
        for (char c : s1.toCharArray()) freq.put(c, freq.getOrDefault(c, 0) + 1);
        for (char c : s2.toCharArray()) freq.put(c, freq.getOrDefault(c, 0) - 1);
        for (int v : freq.values()) {
            if (v != 0) return false;
        }
        return true;
    }

    // W5: Intersection of Two Arrays
    static List<Integer> solveW5Intersection(int[] a, int[] b) {
        HashSet<Integer> setA = new HashSet<>();
        for (int x : a) setA.add(x);
        HashSet<Integer> common = new HashSet<>();
        for (int x : b) {
            if (setA.contains(x)) common.add(x);
        }
        List<Integer> result = new ArrayList<>(common);
        Collections.sort(result);
        return result;
    }

    // P1: Group Anagrams
    static List<List<String>> solveP1GroupAnagrams(String[] strs) {
        if (strs.length == 0) return new ArrayList<>();
        HashMap<String, List<String>> groups = new HashMap<>();
        for (String s : strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String key = new String(ca);
            groups.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        List<List<String>> result = new ArrayList<>();
        for (List<String> group : groups.values()) {
            Collections.sort(group);
            result.add(group);
        }
        result.sort((a, b) -> a.get(0).compareTo(b.get(0)));
        return result;
    }

    // P2: Missing Number
    static int solveP2MissingNumber(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int x : nums) set.add(x);
        for (int i = 0; i <= nums.length; i++) {
            if (!set.contains(i)) return i;
        }
        return -1;
    }

    // P3: Longest Subarray with Sum K
    static int solveP3LongestSubarraySumK(int[] arr, int k) {
        HashMap<Long, Integer> prefixIndex = new HashMap<>();
        prefixIndex.put(0L, -1);
        long prefixSum = 0;
        int maxLen = 0;
        for (int i = 0; i < arr.length; i++) {
            prefixSum += arr[i];
            long need = prefixSum - k;
            if (prefixIndex.containsKey(need)) {
                maxLen = Math.max(maxLen, i - prefixIndex.get(need));
            }
            if (!prefixIndex.containsKey(prefixSum)) {
                prefixIndex.put(prefixSum, i);
            }
        }
        return maxLen;
    }

    // P4: Count Subarrays with Sum K
    static int solveP4CountSubarraysSumK(int[] arr, int k) {
        HashMap<Long, Integer> prefixCount = new HashMap<>();
        prefixCount.put(0L, 1);
        long prefixSum = 0;
        int count = 0;
        for (int x : arr) {
            prefixSum += x;
            count += prefixCount.getOrDefault(prefixSum - k, 0);
            prefixCount.put(prefixSum, prefixCount.getOrDefault(prefixSum, 0) + 1);
        }
        return count;
    }

    // P5: Sort Characters by Frequency
    static String solveP5SortCharsByFreq(String s) {
        if (s.isEmpty()) return "";
        HashMap<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        List<Character> chars = new ArrayList<>(freq.keySet());
        chars.sort((a, b) -> {
            int cmp = Integer.compare(freq.get(b), freq.get(a));
            if (cmp != 0) return cmp;
            return Character.compare(a, b);
        });
        StringBuilder sb = new StringBuilder();
        for (char c : chars) {
            for (int i = 0; i < freq.get(c); i++) sb.append(c);
        }
        return sb.toString();
    }

    // C1: Missing Number — Four Ways
    static int solveC1Sort(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        for (int i = 0; i < sorted.length; i++) {
            if (sorted[i] != i) return i;
        }
        return sorted.length;
    }

    static int solveC1Xor(int[] nums) {
        int xor = 0;
        for (int i = 0; i <= nums.length; i++) xor ^= i;
        for (int x : nums) xor ^= x;
        return xor;
    }

    static int solveC1Math(int[] nums) {
        long expected = (long) nums.length * (nums.length + 1) / 2;
        long actual = 0;
        for (int x : nums) actual += x;
        return (int) (expected - actual);
    }

    static int solveC1Hash(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int x : nums) set.add(x);
        for (int i = 0; i <= nums.length; i++) {
            if (!set.contains(i)) return i;
        }
        return -1;
    }

    // C2: Longest Consecutive Sequence
    static int solveC2LongestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        HashSet<Integer> set = new HashSet<>();
        for (int x : nums) set.add(x);
        int longest = 0;
        for (int num : set) {
            if (!set.contains(num - 1)) {
                int current = num;
                int length = 1;
                while (set.contains(current + 1)) { current++; length++; }
                longest = Math.max(longest, length);
            }
        }
        return longest;
    }

    // C3: Repeating and Missing Number
    static int[] solveC3RepeatingMissing(int[] nums) {
        int n = nums.length;
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);
        int repeating = 0, missing = 0;
        for (int i = 1; i <= n; i++) {
            int count = freq.getOrDefault(i, 0);
            if (count == 2) repeating = i;
            if (count == 0) missing = i;
        }
        return new int[]{repeating, missing};
    }

    // ── Test methods ────────────────────────────────────────────────

    static void testW1FrequencyCount() {
        assertListIntArrayEquals(
            Arrays.asList(new int[]{1,1}, new int[]{2,2}, new int[]{3,3}),
            solveW1FreqCount(new int[]{1,2,2,3,3,3}),
            "W1: [1,2,2,3,3,3]");
        assertListIntArrayEquals(
            Arrays.asList(new int[]{5,1}),
            solveW1FreqCount(new int[]{5}),
            "W1: [5]");
        assertListIntArrayEquals(
            new ArrayList<>(),
            solveW1FreqCount(new int[]{}),
            "W1: []");
        assertListIntArrayEquals(
            Arrays.asList(new int[]{1,2}, new int[]{2,1}, new int[]{3,1}),
            solveW1FreqCount(new int[]{3,1,2,1}),
            "W1: [3,1,2,1]");
        assertListIntArrayEquals(
            Arrays.asList(new int[]{4,4}),
            solveW1FreqCount(new int[]{4,4,4,4}),
            "W1: [4,4,4,4]");
    }

    static void testW2HighestLowestFreq() {
        assertArrayEquals(new int[]{3,1}, solveW2HighestLowestFreq(new int[]{1,2,2,3,3,3}),
            "W2: [1,2,2,3,3,3]");
        assertArrayEquals(new int[]{10,30}, solveW2HighestLowestFreq(new int[]{10,10,10,20,20,30}),
            "W2: [10,10,10,20,20,30]");
        assertArrayEquals(new int[]{5,5}, solveW2HighestLowestFreq(new int[]{5}),
            "W2: [5]");
        assertArrayEquals(new int[]{2,1}, solveW2HighestLowestFreq(new int[]{1,1,2,2,2,2,3,3,3}),
            "W2: [1,1,2,2,2,2,3,3,3]");
        assertArrayEquals(new int[]{9,7}, solveW2HighestLowestFreq(new int[]{7,7,8,8,8,9,9,9,9}),
            "W2: [7,7,8,8,8,9,9,9,9]");
    }

    static void testW3FirstNonRepeating() {
        assertStringEquals("c", solveW3FirstNonRepeating("aabbcdd"), "W3: aabbcdd");
        assertStringEquals("_", solveW3FirstNonRepeating("aabb"), "W3: aabb");
        assertStringEquals("_", solveW3FirstNonRepeating("abcabc"), "W3: abcabc");
        assertStringEquals("c", solveW3FirstNonRepeating("aabbc"), "W3: aabbc");
        assertStringEquals("a", solveW3FirstNonRepeating("a"), "W3: a");
        assertStringEquals("_", solveW3FirstNonRepeating(""), "W3: empty");
    }

    static void testW4ValidAnagram() {
        assertBoolEquals(true, solveW4ValidAnagram("listen", "silent"), "W4: listen/silent");
        assertBoolEquals(false, solveW4ValidAnagram("hello", "world"), "W4: hello/world");
        assertBoolEquals(true, solveW4ValidAnagram("", ""), "W4: empty/empty");
        assertBoolEquals(true, solveW4ValidAnagram("a", "a"), "W4: a/a");
        assertBoolEquals(true, solveW4ValidAnagram("ab", "ba"), "W4: ab/ba");
        assertBoolEquals(false, solveW4ValidAnagram("abc", "abd"), "W4: abc/abd");
        assertBoolEquals(true, solveW4ValidAnagram("aab", "aba"), "W4: aab/aba");
    }

    static void testW5Intersection() {
        assertListEquals(Arrays.asList(2),
            solveW5Intersection(new int[]{1,2,2,1}, new int[]{2,2}),
            "W5: [1,2,2,1] & [2,2]");
        assertListEquals(Arrays.asList(4,9),
            solveW5Intersection(new int[]{4,9,5}, new int[]{9,4,9,8,4}),
            "W5: [4,9,5] & [9,4,9,8,4]");
        assertListEquals(new ArrayList<>(),
            solveW5Intersection(new int[]{1,2,3}, new int[]{4,5,6}),
            "W5: [1,2,3] & [4,5,6]");
        assertListEquals(new ArrayList<>(),
            solveW5Intersection(new int[]{}, new int[]{1,2}),
            "W5: [] & [1,2]");
        assertListEquals(Arrays.asList(1),
            solveW5Intersection(new int[]{1,1,1}, new int[]{1}),
            "W5: [1,1,1] & [1]");
    }

    static void testP1GroupAnagrams() {
        assertNestedListEquals(
            Arrays.asList(
                Arrays.asList("ate","eat","tea"),
                Arrays.asList("bat"),
                Arrays.asList("nat","tan")
            ),
            solveP1GroupAnagrams(new String[]{"eat","tea","tan","ate","nat","bat"}),
            "P1: eat,tea,tan,ate,nat,bat");
        assertNestedListEquals(
            Arrays.asList(Arrays.asList("")),
            solveP1GroupAnagrams(new String[]{""}),
            "P1: empty string");
        assertNestedListEquals(
            Arrays.asList(Arrays.asList("a")),
            solveP1GroupAnagrams(new String[]{"a"}),
            "P1: single char");
        assertNestedListEquals(
            Arrays.asList(
                Arrays.asList("abc","bca","cab"),
                Arrays.asList("xyz","zxy")
            ),
            solveP1GroupAnagrams(new String[]{"abc","bca","cab","xyz","zxy"}),
            "P1: abc,bca,cab,xyz,zxy");
        assertNestedListEquals(
            new ArrayList<>(),
            solveP1GroupAnagrams(new String[]{}),
            "P1: empty array");
    }

    static void testP2MissingNumber() {
        assertEquals(2, solveP2MissingNumber(new int[]{3,0,1}), "P2: [3,0,1]");
        assertEquals(2, solveP2MissingNumber(new int[]{0,1}), "P2: [0,1]");
        assertEquals(8, solveP2MissingNumber(new int[]{9,6,4,2,3,5,7,0,1}), "P2: [9,6,4,2,3,5,7,0,1]");
        assertEquals(1, solveP2MissingNumber(new int[]{0}), "P2: [0]");
        assertEquals(0, solveP2MissingNumber(new int[]{1}), "P2: [1]");
    }

    static void testP3LongestSubarraySumK() {
        assertEquals(3, solveP3LongestSubarraySumK(new int[]{1,2,3,1,1,1,1}, 3), "P3: [1,2,3,1,1,1,1] k=3");
        assertEquals(3, solveP3LongestSubarraySumK(new int[]{-1,1,1}, 1), "P3: [-1,1,1] k=1");
        assertEquals(0, solveP3LongestSubarraySumK(new int[]{1,2,3}, 10), "P3: [1,2,3] k=10");
        assertEquals(4, solveP3LongestSubarraySumK(new int[]{1,-1,1,-1,1}, 0), "P3: [1,-1,1,-1,1] k=0");
        assertEquals(3, solveP3LongestSubarraySumK(new int[]{2,0,0,3}, 3), "P3: [2,0,0,3] k=3");
        assertEquals(1, solveP3LongestSubarraySumK(new int[]{1}, 1), "P3: [1] k=1");
    }

    static void testP4CountSubarraysSumK() {
        assertEquals(2, solveP4CountSubarraysSumK(new int[]{1,1,1}, 2), "P4: [1,1,1] k=2");
        assertEquals(2, solveP4CountSubarraysSumK(new int[]{1,2,3}, 3), "P4: [1,2,3] k=3");
        assertEquals(0, solveP4CountSubarraysSumK(new int[]{1}, 0), "P4: [1] k=0");
        assertEquals(3, solveP4CountSubarraysSumK(new int[]{1,-1,0}, 0), "P4: [1,-1,0] k=0");
        assertEquals(6, solveP4CountSubarraysSumK(new int[]{0,0,0}, 0), "P4: [0,0,0] k=0");
        assertEquals(1, solveP4CountSubarraysSumK(new int[]{1}, 1), "P4: [1] k=1");
    }

    static void testP5SortCharsByFreq() {
        assertStringEquals("eert", solveP5SortCharsByFreq("tree"), "P5: tree");
        assertStringEquals("aaaccc", solveP5SortCharsByFreq("cccaaa"), "P5: cccaaa");
        assertStringEquals("aab", solveP5SortCharsByFreq("aab"), "P5: aab");
        assertStringEquals("lleho", solveP5SortCharsByFreq("hello"), "P5: hello");
        assertStringEquals("x", solveP5SortCharsByFreq("x"), "P5: x");
        assertStringEquals("", solveP5SortCharsByFreq(""), "P5: empty");
    }

    static void testC1MissingNumberFourWays() {
        // Test all four methods with the same inputs
        int[][] inputs = {{3,0,1}, {0,1}, {9,6,4,2,3,5,7,0,1}, {1}, {0}};
        int[] expected = {2, 2, 8, 0, 1};

        for (int t = 0; t < inputs.length; t++) {
            String label = "C1 Sort: " + Arrays.toString(inputs[t]);
            assertEquals(expected[t], solveC1Sort(inputs[t]), label);
        }
        for (int t = 0; t < inputs.length; t++) {
            String label = "C1 XOR: " + Arrays.toString(inputs[t]);
            assertEquals(expected[t], solveC1Xor(inputs[t]), label);
        }
        for (int t = 0; t < inputs.length; t++) {
            String label = "C1 Math: " + Arrays.toString(inputs[t]);
            assertEquals(expected[t], solveC1Math(inputs[t]), label);
        }
        for (int t = 0; t < inputs.length; t++) {
            String label = "C1 Hash: " + Arrays.toString(inputs[t]);
            assertEquals(expected[t], solveC1Hash(inputs[t]), label);
        }
    }

    static void testC2LongestConsecutive() {
        assertEquals(4, solveC2LongestConsecutive(new int[]{100,4,200,1,3,2}),
            "C2: [100,4,200,1,3,2]");
        assertEquals(9, solveC2LongestConsecutive(new int[]{0,3,7,2,5,8,4,6,0,1}),
            "C2: [0,3,7,2,5,8,4,6,0,1]");
        assertEquals(0, solveC2LongestConsecutive(new int[]{}),
            "C2: []");
        assertEquals(1, solveC2LongestConsecutive(new int[]{1}),
            "C2: [1]");
        assertEquals(1, solveC2LongestConsecutive(new int[]{1,1,1}),
            "C2: [1,1,1]");
        assertEquals(11, solveC2LongestConsecutive(new int[]{9,1,4,7,3,-1,0,5,8,2,6}),
            "C2: [9,1,4,7,3,-1,0,5,8,2,6]");
    }

    static void testC3RepeatingMissing() {
        assertArrayEquals(new int[]{3,4}, solveC3RepeatingMissing(new int[]{3,1,2,5,3}),
            "C3: [3,1,2,5,3]");
        assertArrayEquals(new int[]{1,2}, solveC3RepeatingMissing(new int[]{1,1}),
            "C3: [1,1]");
        assertArrayEquals(new int[]{2,1}, solveC3RepeatingMissing(new int[]{2,2}),
            "C3: [2,2]");
        assertArrayEquals(new int[]{1,5}, solveC3RepeatingMissing(new int[]{4,3,6,2,1,1}),
            "C3: [4,3,6,2,1,1]");
        assertArrayEquals(new int[]{4,5}, solveC3RepeatingMissing(new int[]{1,2,3,4,4}),
            "C3: [1,2,3,4,4]");
    }

    // ── Main ────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 11: Hashing — The Secret Decoder Ring");
        System.out.println("==============================================\n");

        testW1FrequencyCount();
        testW2HighestLowestFreq();
        testW3FirstNonRepeating();
        testW4ValidAnagram();
        testW5Intersection();
        testP1GroupAnagrams();
        testP2MissingNumber();
        testP3LongestSubarraySumK();
        testP4CountSubarraysSumK();
        testP5SortCharsByFreq();
        testC1MissingNumberFourWays();
        testC2LongestConsecutive();
        testC3RepeatingMissing();

        System.out.println();
        if (failed == 0) {
            System.out.println("All " + passed + " tests passed!");
        } else {
            System.out.println(passed + " passed, " + failed + " failed.");
            System.exit(1);
        }
    }
}
