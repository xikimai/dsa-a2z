package ch12.tests;

import java.util.*;

/**
 * Tests for Chapter 12: Bit Manipulation — The Language of Computers
 *
 * Build and run:
 *   cd code/java
 *   javac ch12/tests/TestCh12.java
 *   java -ea ch12.tests.TestCh12
 */
public class TestCh12 {

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

    static void assertListOfListEquals(List<List<Integer>> expected, List<List<Integer>> actual, String msg) {
        if (expected.equals(actual)) {
            passed++;
        } else {
            failed++;
            System.out.println("FAIL: " + msg + " — size expected " + expected.size() + ", got " + actual.size());
        }
    }

    // ── Reference solutions ─────────────────────────────────────────

    // W1: Binary Representation
    static String ref_binary_rep(int n) {
        if (n == 0) return "0";
        StringBuilder bits = new StringBuilder();
        while (n > 0) {
            bits.append(n % 2);
            n /= 2;
        }
        return bits.reverse().toString();
    }

    // W2: Count Set Bits
    static int ref_count_set_bits(int n) {
        int count = 0;
        while (n != 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    }

    // W3: Check Power of Two
    static boolean ref_power_of_two(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }

    // W4: Check i-th Bit
    static boolean ref_ith_bit(int n, int i) {
        return ((n >> i) & 1) == 1;
    }

    // P1: Single Number
    static int ref_single_number(int[] nums) {
        int result = 0;
        for (int x : nums) result ^= x;
        return result;
    }

    // P2: Toggle i-th Bit
    static int ref_toggle(int n, int i) {
        return n ^ (1 << i);
    }

    // P3: Set and Clear Bits
    static int ref_set_bit(int n, int i) { return n | (1 << i); }
    static int ref_clear_bit(int n, int i) { return n & ~(1 << i); }

    // P4: Power Set
    static List<List<Integer>> ref_power_set(int[] nums) {
        int n = nums.length;
        List<List<Integer>> result = new ArrayList<>();
        for (int mask = 0; mask < (1 << n); mask++) {
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 1) subset.add(nums[i]);
            }
            result.add(subset);
        }
        return result;
    }

    // C1: Single Number Three Ways
    static int ref_single_sort(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        for (int i = 0; i < sorted.length - 1; i += 2) {
            if (sorted[i] != sorted[i + 1]) return sorted[i];
        }
        return sorted[sorted.length - 1];
    }

    static int ref_single_hash(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);
        for (var e : freq.entrySet()) {
            if (e.getValue() == 1) return e.getKey();
        }
        return -1;
    }

    static int ref_single_xor(int[] nums) {
        int result = 0;
        for (int x : nums) result ^= x;
        return result;
    }

    // C2: Two Odd Occurring
    static int[] ref_two_odd(int[] nums) {
        int xorAll = 0;
        for (int x : nums) xorAll ^= x;
        int diffBit = xorAll & (-xorAll);
        int a = 0, b = 0;
        for (int x : nums) {
            if ((x & diffBit) != 0) a ^= x;
            else b ^= x;
        }
        if (a > b) { int t = a; a = b; b = t; }
        return new int[]{a, b};
    }

    // C3: Min Bit Flips
    static int ref_min_flips(int start, int goal) {
        int xor = start ^ goal;
        int count = 0;
        while (xor != 0) {
            xor &= (xor - 1);
            count++;
        }
        return count;
    }

    // ── Test methods ────────────────────────────────────────────────

    static void testW1BinaryRepresentation() {
        assertStringEquals("0", ref_binary_rep(0), "W1: 0");
        assertStringEquals("1", ref_binary_rep(1), "W1: 1");
        assertStringEquals("101", ref_binary_rep(5), "W1: 5");
        assertStringEquals("101010", ref_binary_rep(42), "W1: 42");
        assertStringEquals("11111111", ref_binary_rep(255), "W1: 255");
        assertStringEquals("10000000000", ref_binary_rep(1024), "W1: 1024");
        assertStringEquals(Integer.toBinaryString(1000000000), ref_binary_rep(1000000000), "W1: 10^9");
    }

    static void testW2CountSetBits() {
        assertEquals(0, ref_count_set_bits(0), "W2: 0");
        assertEquals(1, ref_count_set_bits(1), "W2: 1");
        assertEquals(3, ref_count_set_bits(42), "W2: 42");
        assertEquals(8, ref_count_set_bits(255), "W2: 255");
        assertEquals(10, ref_count_set_bits(1023), "W2: 1023");
        assertEquals(1, ref_count_set_bits(1024), "W2: 1024");
        assertEquals(Integer.bitCount(999999999), ref_count_set_bits(999999999), "W2: 10^9-1");
    }

    static void testW3CheckPowerOfTwo() {
        assertBoolEquals(true, ref_power_of_two(1), "W3: 1");
        assertBoolEquals(true, ref_power_of_two(2), "W3: 2");
        assertBoolEquals(true, ref_power_of_two(4), "W3: 4");
        assertBoolEquals(true, ref_power_of_two(1024), "W3: 1024");
        assertBoolEquals(false, ref_power_of_two(0), "W3: 0");
        assertBoolEquals(false, ref_power_of_two(3), "W3: 3");
        assertBoolEquals(false, ref_power_of_two(6), "W3: 6");
        assertBoolEquals(false, ref_power_of_two(-4), "W3: -4");
        assertBoolEquals(true, ref_power_of_two(1 << 20), "W3: 2^20");
        assertBoolEquals(false, ref_power_of_two((1 << 20) + 1), "W3: 2^20+1");
    }

    static void testW4CheckIthBit() {
        assertBoolEquals(true, ref_ith_bit(42, 1), "W4: 42 bit 1");
        assertBoolEquals(false, ref_ith_bit(42, 2), "W4: 42 bit 2");
        assertBoolEquals(true, ref_ith_bit(42, 3), "W4: 42 bit 3");
        assertBoolEquals(true, ref_ith_bit(42, 5), "W4: 42 bit 5");
        assertBoolEquals(false, ref_ith_bit(42, 6), "W4: 42 bit 6");
        assertBoolEquals(false, ref_ith_bit(0, 0), "W4: 0 bit 0");
        assertBoolEquals(true, ref_ith_bit(1, 0), "W4: 1 bit 0");
        assertBoolEquals(true, ref_ith_bit(16, 4), "W4: 16 bit 4");
    }

    static void testP1SingleNumber() {
        assertEquals(4, ref_single_number(new int[]{4, 1, 2, 1, 2}), "P1: [4,1,2,1,2]");
        assertEquals(1, ref_single_number(new int[]{2, 2, 1}), "P1: [2,2,1]");
        assertEquals(1, ref_single_number(new int[]{1}), "P1: [1]");
        assertEquals(5, ref_single_number(new int[]{1, 3, 5, 3, 1}), "P1: [1,3,5,3,1]");
        assertEquals(2, ref_single_number(new int[]{-1, 2, -1}), "P1: [-1,2,-1]");
        assertEquals(5, ref_single_number(new int[]{0, 5, 0}), "P1: [0,5,0]");
    }

    static void testP2ToggleIthBit() {
        assertEquals(43, ref_toggle(42, 0), "P2: 42 toggle 0");
        assertEquals(40, ref_toggle(42, 1), "P2: 42 toggle 1");
        assertEquals(8, ref_toggle(0, 3), "P2: 0 toggle 3");
        assertEquals(10, ref_toggle(42, 5), "P2: 42 toggle 5");
        assertEquals(42, ref_toggle(ref_toggle(42, 3), 3), "P2: double toggle");
        assertEquals(254, ref_toggle(255, 0), "P2: 255 toggle 0");
    }

    static void testP3SetAndClearBits() {
        assertEquals(43, ref_set_bit(42, 0), "P3: set 42 bit 0");
        assertEquals(42, ref_set_bit(42, 1), "P3: set 42 bit 1 (already set)");
        assertEquals(32, ref_set_bit(0, 5), "P3: set 0 bit 5");
        assertEquals(40, ref_clear_bit(42, 1), "P3: clear 42 bit 1");
        assertEquals(42, ref_clear_bit(42, 0), "P3: clear 42 bit 0 (already clear)");
        // Clear all bits of 255
        int n = 255;
        for (int i = 0; i < 8; i++) n = ref_clear_bit(n, i);
        assertEquals(0, n, "P3: clear all bits of 255");
        // Set then clear roundtrip
        int m = ref_set_bit(42, 0);
        assertEquals(43, m, "P3: set bit 0 of 42");
        m = ref_clear_bit(m, 0);
        assertEquals(42, m, "P3: clear bit 0 back");
    }

    static void testP4PowerSetBitmask() {
        List<List<Integer>> result3 = ref_power_set(new int[]{1, 2, 3});
        assertEquals(8, result3.size(), "P4: [1,2,3] size");
        assertListOfListEquals(
            Arrays.asList(
                Arrays.asList(), Arrays.asList(1), Arrays.asList(2), Arrays.asList(1,2),
                Arrays.asList(3), Arrays.asList(1,3), Arrays.asList(2,3), Arrays.asList(1,2,3)
            ),
            result3, "P4: [1,2,3]");
        assertListOfListEquals(
            Arrays.asList(Arrays.asList()),
            ref_power_set(new int[]{}), "P4: []");
        assertListOfListEquals(
            Arrays.asList(Arrays.asList(), Arrays.asList(5)),
            ref_power_set(new int[]{5}), "P4: [5]");
        assertListOfListEquals(
            Arrays.asList(Arrays.asList(), Arrays.asList(10), Arrays.asList(20), Arrays.asList(10,20)),
            ref_power_set(new int[]{10, 20}), "P4: [10,20]");
        // Count check
        assertEquals(16, ref_power_set(new int[]{1,2,3,4}).size(), "P4: [1,2,3,4] count");
    }

    static void testC1SingleNumberThreeWays() {
        int[][] inputs = {{4,1,2,1,2}, {2,2,1}, {1}, {1,3,5,3,1}, {-1,2,-1}};
        int[] expected = {4, 1, 1, 5, 2};

        for (int t = 0; t < inputs.length; t++) {
            String label = "C1 Sort: " + Arrays.toString(inputs[t]);
            assertEquals(expected[t], ref_single_sort(inputs[t].clone()), label);
        }
        for (int t = 0; t < inputs.length; t++) {
            String label = "C1 Hash: " + Arrays.toString(inputs[t]);
            assertEquals(expected[t], ref_single_hash(inputs[t].clone()), label);
        }
        for (int t = 0; t < inputs.length; t++) {
            String label = "C1 XOR: " + Arrays.toString(inputs[t]);
            assertEquals(expected[t], ref_single_xor(inputs[t].clone()), label);
        }
    }

    static void testC2TwoOddOccurring() {
        assertArrayEquals(new int[]{7, 9}, ref_two_odd(new int[]{2, 4, 7, 9, 2, 4}),
            "C2: [2,4,7,9,2,4]");
        assertArrayEquals(new int[]{3, 4}, ref_two_odd(new int[]{1, 2, 3, 2, 1, 4}),
            "C2: [1,2,3,2,1,4]");
        assertArrayEquals(new int[]{5, 10}, ref_two_odd(new int[]{5, 10}),
            "C2: [5,10]");
        assertArrayEquals(new int[]{100, 200}, ref_two_odd(new int[]{1, 1, 2, 2, 3, 3, 100, 200}),
            "C2: [1,1,2,2,3,3,100,200]");
        assertArrayEquals(new int[]{7, 9}, ref_two_odd(new int[]{7, 7, 7, 9, 3, 3}),
            "C2: [7,7,7,9,3,3]");
        assertArrayEquals(new int[]{11, 22}, ref_two_odd(new int[]{999999, 888888, 999999, 777777, 888888, 777777, 11, 22}),
            "C2: large numbers");
    }

    static void testC3MinBitFlips() {
        assertEquals(3, ref_min_flips(10, 7), "C3: 10 -> 7");
        assertEquals(3, ref_min_flips(3, 4), "C3: 3 -> 4");
        assertEquals(0, ref_min_flips(0, 0), "C3: 0 -> 0");
        assertEquals(0, ref_min_flips(42, 42), "C3: 42 -> 42");
        assertEquals(8, ref_min_flips(0, 255), "C3: 0 -> 255");
        assertEquals(1, ref_min_flips(8, 0), "C3: 8 -> 0");
        assertEquals(10, ref_min_flips(1023, 0), "C3: 1023 -> 0");
    }

    // ── Main ────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 12: Bit Manipulation — The Language of Computers");
        System.out.println("=========================================================\n");

        testW1BinaryRepresentation();
        testW2CountSetBits();
        testW3CheckPowerOfTwo();
        testW4CheckIthBit();
        testP1SingleNumber();
        testP2ToggleIthBit();
        testP3SetAndClearBits();
        testP4PowerSetBitmask();
        testC1SingleNumberThreeWays();
        testC2TwoOddOccurring();
        testC3MinBitFlips();

        System.out.println();
        if (failed == 0) {
            System.out.println("All " + passed + " tests passed!");
        } else {
            System.out.println(passed + " passed, " + failed + " failed.");
            System.exit(1);
        }
    }
}
