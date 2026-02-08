package ch12.learn;

/**
 * Example 01: Bit Manipulation Basics
 * ====================================
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * Demonstrates the fundamental bit operations in Java:
 *   Part 1 — Binary conversion (decimal to binary, binary to decimal)
 *   Part 2 — Bitwise operators (AND, OR, XOR, NOT, shifts)
 *   Part 3 — Bit checks (i-th bit, power of 2, count set bits)
 *   Part 4 — Brian Kernighan's algorithm step-by-step
 */
public class Example01BitBasics {

    public static void main(String[] args) {
        // Part 1: Binary Conversion
        System.out.println("=== Part 1: Binary Conversion ===");
        int[] nums = {0, 1, 5, 10, 42, 255, 1024};
        for (int n : nums) {
            System.out.printf("  %5d = %s%n", n, Integer.toBinaryString(n));
        }

        // Part 2: Bitwise Operators
        System.out.println("\n=== Part 2: Bitwise Operators ===");
        int a = 42, b = 15;
        System.out.printf("  a     = %8s  (%d)%n", Integer.toBinaryString(a), a);
        System.out.printf("  b     = %8s  (%d)%n", Integer.toBinaryString(b), b);
        System.out.printf("  a & b = %8s  (%d)%n", Integer.toBinaryString(a & b), a & b);
        System.out.printf("  a | b = %8s  (%d)%n", Integer.toBinaryString(a | b), a | b);
        System.out.printf("  a ^ b = %8s  (%d)%n", Integer.toBinaryString(a ^ b), a ^ b);
        System.out.printf("  ~a    = %d%n", ~a);
        System.out.printf("  a<<2  = %8s  (%d)%n", Integer.toBinaryString(a << 2), a << 2);
        System.out.printf("  a>>2  = %8s  (%d)%n", Integer.toBinaryString(a >> 2), a >> 2);

        // Part 3: Bit Checks
        System.out.println("\n=== Part 3: Bit Checks ===");
        int n = 42;
        System.out.printf("  n = %d = %s%n", n, Integer.toBinaryString(n));
        for (int i = 0; i < 8; i++) {
            int bit = (n >> i) & 1;
            System.out.printf("    bit %d: %d%s%n", i, bit, bit == 1 ? "  SET" : "");
        }

        System.out.println("\n  Power of 2 checks:");
        int[] checks = {0, 1, 2, 3, 4, 6, 8, 16, 24, 32, 64, 100, 128};
        for (int x : checks) {
            boolean isPow2 = x > 0 && (x & (x - 1)) == 0;
            System.out.printf("    %4d -> %s%n", x, isPow2 ? "YES" : "no");
        }

        // Part 4: Brian Kernighan's Algorithm
        System.out.println("\n=== Part 4: Brian Kernighan's Algorithm ===");
        for (int x : new int[]{42, 255, 0}) {
            int orig = x;
            int count = 0;
            System.out.printf("  n = %d = %s%n", orig, Integer.toBinaryString(orig));
            while (x != 0) {
                x &= (x - 1);
                count++;
            }
            System.out.printf("    Set bits: %d  (Integer.bitCount = %d)%n",
                count, Integer.bitCount(orig));
        }
    }
}
