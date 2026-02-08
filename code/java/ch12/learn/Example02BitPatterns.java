package ch12.learn;

import java.util.*;

/**
 * Example 02: Bit Manipulation Patterns
 * =======================================
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * Demonstrates:
 *   Part 1 — XOR tricks (swap, single number)
 *   Part 2 — Bitmask as set operations
 *   Part 3 — Power set generation
 *   Part 4 — Two odd-occurring numbers
 */
public class Example02BitPatterns {

    public static void main(String[] args) {
        // Part 1: XOR Tricks
        System.out.println("=== Part 1: XOR Tricks ===");
        int a = 42, b = 99;
        System.out.printf("  Before swap: a=%d, b=%d%n", a, b);
        a ^= b; b ^= a; a ^= b;
        System.out.printf("  After swap:  a=%d, b=%d%n", a, b);

        int[] nums = {4, 1, 2, 1, 2};
        int single = 0;
        for (int x : nums) single ^= x;
        System.out.printf("  Single number in %s: %d%n", Arrays.toString(nums), single);

        // Part 2: Bitmask as Set
        System.out.println("\n=== Part 2: Bitmask as Set ===");
        String[] elements = {"A", "B", "C", "D"};
        int mask = 0;
        mask |= (1 << 0); // Add A
        System.out.printf("  Add A:  mask=%s%n", maskToSet(mask, elements));
        mask |= (1 << 2); // Add C
        System.out.printf("  Add C:  mask=%s%n", maskToSet(mask, elements));
        mask ^= (1 << 1); // Toggle B
        System.out.printf("  Tog B:  mask=%s%n", maskToSet(mask, elements));
        mask &= ~(1 << 0); // Remove A
        System.out.printf("  Rem A:  mask=%s%n", maskToSet(mask, elements));

        // Part 3: Power Set
        System.out.println("\n=== Part 3: Power Set ===");
        int[] elems = {1, 2, 3};
        int n = elems.length;
        for (int m = 0; m < (1 << n); m++) {
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (((m >> i) & 1) == 1) subset.add(elems[i]);
            }
            System.out.printf("  mask=%s -> %s%n",
                String.format("%" + n + "s", Integer.toBinaryString(m)).replace(' ', '0'),
                subset);
        }

        // Part 4: Two Odd-Occurring Numbers
        System.out.println("\n=== Part 4: Two Odd-Occurring Numbers ===");
        int[] arr = {2, 4, 7, 9, 2, 4};
        int xorAll = 0;
        for (int x : arr) xorAll ^= x;
        int diffBit = xorAll & (-xorAll);
        int p = 0, q = 0;
        for (int x : arr) {
            if ((x & diffBit) != 0) p ^= x;
            else q ^= x;
        }
        if (p > q) { int t = p; p = q; q = t; }
        System.out.printf("  Input: %s%n", Arrays.toString(arr));
        System.out.printf("  Two odd-occurring: [%d, %d]%n", p, q);
    }

    static String maskToSet(int mask, String[] elements) {
        StringBuilder sb = new StringBuilder("{");
        boolean first = true;
        for (int i = 0; i < elements.length; i++) {
            if (((mask >> i) & 1) == 1) {
                if (!first) sb.append(", ");
                sb.append(elements[i]);
                first = false;
            }
        }
        sb.append("}");
        return sb.toString();
    }
}
