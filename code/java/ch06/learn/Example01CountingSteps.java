package ch06.learn;

/**
 * Example 01: Counting Steps
 * ==============================
 * Chapter 6: How Fast Is Your Code?
 *
 * This file demonstrates how different algorithms take different numbers
 * of steps to complete. We'll measure real time using System.nanoTime()
 * to SEE the difference between O(1), O(n), O(n^2), and O(log n).
 *
 * Build and run:
 *   cd code/java
 *   javac ch06/learn/Example01CountingSteps.java
 *   java ch06.learn.Example01CountingSteps
 */
public class Example01CountingSteps {

    // ── 1. O(1) — Constant Time ─────────────────────────────────────
    // No matter how big n is, this always does the same work.

    static void demoConstant() {
        System.out.println("=== Part 1: O(1) — Constant Time ===");
        System.out.println("Formula: sum = n * (n + 1) / 2");
        System.out.println();

        int[] sizes = {100, 10_000, 1_000_000, 100_000_000};
        for (int n : sizes) {
            long start = System.nanoTime();
            long sum = (long) n * (n + 1) / 2;
            long elapsed = System.nanoTime() - start;
            System.out.printf("  n = %,11d  ->  sum = %,20d  (%,d ns)%n", n, sum, elapsed);
        }
        System.out.println("  Notice: time barely changes — that's O(1)!");
        System.out.println();
    }

    // ── 2. O(n) — Linear Time ───────────────────────────────────────
    // Double n, double the time.

    static void demoLinear() {
        System.out.println("=== Part 2: O(n) — Linear Time ===");
        System.out.println("Loop: add 1 + 2 + ... + n");
        System.out.println();

        int[] sizes = {10_000, 100_000, 1_000_000};
        for (int n : sizes) {
            long start = System.nanoTime();
            long sum = 0;
            for (int i = 1; i <= n; i++) {
                sum += i;
            }
            long elapsed = System.nanoTime() - start;
            System.out.printf("  n = %,10d  ->  sum = %,15d  (%,d ns)%n", n, sum, elapsed);
        }
        System.out.println("  Notice: 10x more n => roughly 10x more time.");
        System.out.println();
    }

    // ── 3. O(n^2) — Quadratic Time ──────────────────────────────────
    // Double n, quadruple the time. Gets painful fast!

    static void demoQuadratic() {
        System.out.println("=== Part 3: O(n^2) — Quadratic Time ===");
        System.out.println("Nested loop: for each i, loop through all j");
        System.out.println();

        int[] sizes = {1_000, 5_000, 10_000};
        for (int n : sizes) {
            long start = System.nanoTime();
            long count = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    count++;
                }
            }
            long elapsed = System.nanoTime() - start;
            System.out.printf("  n = %,6d  ->  steps = %,15d  (%,d ns)%n", n, count, elapsed);
        }
        System.out.println("  Notice: 5x more n => ~25x more time. 10x => ~100x!");
        System.out.println();
    }

    // ── 4. O(log n) — Logarithmic Time ──────────────────────────────
    // Keep halving. Even huge n finishes in very few steps.

    static void demoLogarithmic() {
        System.out.println("=== Part 4: O(log n) — Logarithmic Time ===");
        System.out.println("Halving: start at n, keep dividing by 2");
        System.out.println();

        int[] sizes = {100, 10_000, 1_000_000, 100_000_000};
        for (int n : sizes) {
            long start = System.nanoTime();
            int steps = 0;
            int current = n;
            while (current > 1) {
                current /= 2;
                steps++;
            }
            long elapsed = System.nanoTime() - start;
            System.out.printf("  n = %,11d  ->  steps = %,4d  (%,d ns)%n", n, steps, elapsed);
        }
        System.out.println("  Notice: even 100 million only needs ~27 steps!");
        System.out.println();
    }

    // ── Main ─────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 6: Counting Steps — Time Complexity Demo");
        System.out.println("================================================\n");

        demoConstant();
        demoLinear();
        demoQuadratic();
        demoLogarithmic();

        System.out.println("KEY TAKEAWAY:");
        System.out.println("  O(1) < O(log n) < O(n) < O(n^2)");
        System.out.println("  Choosing the right algorithm can make your code");
        System.out.println("  run in milliseconds instead of hours!");
    }
}
