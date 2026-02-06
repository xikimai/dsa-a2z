package ch01.tests;

/**
 * Tests for Warmup 01: Sum of Two Numbers
 * ========================================
 * Chapter 1: The Coder's Toolkit
 *
 * This file tests the solve() method. We define solve() here with
 * the reference solution so the test is self-contained.
 *
 * Build and run:
 *   cd code/java
 *   javac ch01/tests/TestWarmup01.java
 *   java ch01.tests.TestWarmup01
 */
public class TestWarmup01 {

    // Reference solution for testing
    static int solve(int a, int b) {
        return a + b;
    }

    // ── Test cases ─────────────────────────────────────────────────

    static void testSumPositive() {
        assert solve(1, 2) == 3 : "Expected 3, got " + solve(1, 2);
        System.out.println("  test_sum_positive............ PASS");
    }

    static void testSumZeros() {
        assert solve(0, 0) == 0 : "Expected 0, got " + solve(0, 0);
        System.out.println("  test_sum_zeros............... PASS");
    }

    static void testSumNegativePositive() {
        assert solve(-5, 5) == 0 : "Expected 0, got " + solve(-5, 5);
        System.out.println("  test_sum_negative_positive... PASS");
    }

    static void testSumLarge() {
        assert solve(1000000, 2000000) == 3000000
            : "Expected 3000000, got " + solve(1000000, 2000000);
        System.out.println("  test_sum_large............... PASS");
    }

    static void testSumNegatives() {
        assert solve(-100, -200) == -300
            : "Expected -300, got " + solve(-100, -200);
        System.out.println("  test_sum_negatives........... PASS");
    }

    // ── Runner ─────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("=== Warmup 01: Sum of Two Numbers ===");

        testSumPositive();
        testSumZeros();
        testSumNegativePositive();
        testSumLarge();
        testSumNegatives();

        System.out.println();
        System.out.println("All tests passed!");
    }
}
