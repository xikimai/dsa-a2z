package ch06.tests;

import java.util.*;

/**
 * Tests for Chapter 6: How Fast Is Your Code?
 * =============================================
 * Chapter 6: How Fast Is Your Code?
 *
 * This file tests every solve() method from Chapter 6 using the reference
 * solutions. We define each solve() here so the test is self-contained.
 *
 * Build and run:
 *   cd code/java
 *   javac ch06/tests/TestCh06.java
 *   java -ea ch06.tests.TestCh06
 *
 * The -ea flag enables assertions. Without it, assert statements are ignored!
 */
public class TestCh06 {

    // ── Helper methods ───────────────────────────────────────────────

    static void assertEquals(Object expected, Object actual, String msg) {
        assert Objects.equals(expected, actual)
            : msg + " — expected " + expected + ", got " + actual;
    }

    static void assertArrayEquals(int[] expected, int[] actual, String msg) {
        assert Arrays.equals(expected, actual)
            : msg + " — expected " + Arrays.toString(expected)
              + ", got " + Arrays.toString(actual);
    }

    // ── Reference solutions ─────────────────────────────────────────

    // W1: Count the Steps
    static int solveCountSteps(String codeId, int n) {
        switch (codeId) {
            case "single_loop":    return n;
            case "double_loop":    return n * n;
            case "half_loop":      return n / 2;
            case "dependent_loop": return n * (n + 1) / 2;
            case "log_loop":
                if (n < 2) return 0;
                return (int) (Math.log(n) / Math.log(2));
            default:               return 0;
        }
    }

    // W2: Is It Fast Enough?
    static boolean solveFastEnough(int n, String complexity) {
        long ops;
        long limit = 100_000_000L;
        switch (complexity) {
            case "1":       ops = 1; break;
            case "log_n":   ops = Math.max(1, (long) (Math.log(n) / Math.log(2))); break;
            case "n":       ops = n; break;
            case "n_log_n": ops = (long) n * Math.max(1, (long) (Math.log(n) / Math.log(2))); break;
            case "n^2":     ops = (long) n * n; break;
            case "n^3":     ops = (long) n * n * n; break;
            case "2^n":
                if (n > 30) return false;
                ops = 1L << n;
                break;
            default:        ops = Long.MAX_VALUE;
        }
        return ops < limit;
    }

    // W3: Mystery Complexity
    static String solveMysteryComplexity(int[] nValues, int[] counts) {
        boolean allConstant = true;
        boolean allLinear = true;
        boolean allQuadratic = true;

        for (int i = 1; i < nValues.length; i++) {
            double ratioN = (double) nValues[i] / nValues[i - 1];
            double ratioC = (double) counts[i] / counts[i - 1];

            if (Math.abs(ratioC - 1.0) > 0.3) allConstant = false;
            if (Math.abs(ratioC - ratioN) > ratioN * 0.3) allLinear = false;
            if (Math.abs(ratioC - ratioN * ratioN) > ratioN * ratioN * 0.3) allQuadratic = false;
        }

        if (allConstant) return "O(1)";
        if (allLinear) return "O(n)";
        if (allQuadratic) return "O(n^2)";
        return "O(log n)";
    }

    // W4: Sum to N
    static int[] solveSumToN(int n) {
        int loopResult = 0;
        for (int i = 1; i <= n; i++) loopResult += i;

        int formulaResult = n * (n + 1) / 2;

        int nestedResult = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                nestedResult++;
            }
        }
        return new int[]{loopResult, formulaResult, nestedResult};
    }

    // P1: Contains Duplicate
    static boolean solveContainsDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for (int n : nums) {
            if (!seen.add(n)) return true;
        }
        return false;
    }

    // P2: Max Subarray Brute
    static int solveMaxSubarrayBrute(int[] nums) {
        if (nums.length == 0) return 0;
        int maxSum = nums[0];
        for (int i = 0; i < nums.length; i++) {
            int currentSum = 0;
            for (int j = i; j < nums.length; j++) {
                currentSum += nums[j];
                if (currentSum > maxSum) maxSum = currentSum;
            }
        }
        return maxSum;
    }

    // P3: Sorted Squares
    static int[] solveSortedSquares(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int left = 0, right = n - 1;
        int pos = n - 1;
        while (left <= right) {
            int leftSq = nums[left] * nums[left];
            int rightSq = nums[right] * nums[right];
            if (leftSq > rightSq) {
                result[pos] = leftSq;
                left++;
            } else {
                result[pos] = rightSq;
                right--;
            }
            pos--;
        }
        return result;
    }

    // P4: Majority Element
    static int solveMajorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;
        for (int n : nums) {
            if (count == 0) candidate = n;
            count += (n == candidate) ? 1 : -1;
        }
        return candidate;
    }

    // C1: Two Sum — Three Ways
    static int[] solveTwoSumBrute(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) return new int[]{i, j};
            }
        }
        return new int[]{-1, -1};
    }

    static int[] solveTwoSumSort(int[] nums, int target) {
        int n = nums.length;
        int[][] indexed = new int[n][2];
        for (int i = 0; i < n; i++) {
            indexed[i][0] = nums[i];
            indexed[i][1] = i;
        }
        Arrays.sort(indexed, (a, b) -> Integer.compare(a[0], b[0]));
        int left = 0, right = n - 1;
        while (left < right) {
            int sum = indexed[left][0] + indexed[right][0];
            if (sum == target) {
                int ii = Math.min(indexed[left][1], indexed[right][1]);
                int jj = Math.max(indexed[left][1], indexed[right][1]);
                return new int[]{ii, jj};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[]{-1, -1};
    }

    static int[] solveTwoSumHash(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{-1, -1};
    }

    // C2: Performance Showdown
    static long computeOps(String complexity, int n) {
        switch (complexity) {
            case "1":       return 1;
            case "log_n":   return Math.max(1, (long) (Math.log(n) / Math.log(2)));
            case "n":       return n;
            case "n_log_n": return (long) n * Math.max(1, (long) (Math.log(n) / Math.log(2)));
            case "n^2":     return (long) n * n;
            case "n^3":     return (long) n * n * n;
            case "2^n":
                if (n > 30) return Long.MAX_VALUE;
                return 1L << n;
            default:        return Long.MAX_VALUE;
        }
    }

    static String solvePerformanceShowdown(String complexityA, String complexityB, int n) {
        long opsA = computeOps(complexityA, n);
        long opsB = computeOps(complexityB, n);
        if (opsA < opsB) return "A";
        if (opsB < opsA) return "B";
        return "TIE";
    }

    // ── Warmup 01: Count the Steps ─────────────────────────────────

    static void testCountStepsSingleLoop() {
        assertEquals(100, solveCountSteps("single_loop", 100),
            "single_loop with n=100");
        System.out.println("  test_count_steps_single_loop..... PASS");
    }

    static void testCountStepsDoubleLoop() {
        assertEquals(100, solveCountSteps("double_loop", 10),
            "double_loop with n=10");
        System.out.println("  test_count_steps_double_loop..... PASS");
    }

    static void testCountStepsHalfLoop() {
        assertEquals(50, solveCountSteps("half_loop", 100),
            "half_loop with n=100");
        System.out.println("  test_count_steps_half_loop....... PASS");
    }

    static void testCountStepsHalfLoopOdd() {
        assertEquals(3, solveCountSteps("half_loop", 7),
            "half_loop with n=7");
        System.out.println("  test_count_steps_half_loop_odd... PASS");
    }

    static void testCountStepsDependentLoop() {
        assertEquals(10, solveCountSteps("dependent_loop", 4),
            "dependent_loop with n=4");
        System.out.println("  test_count_steps_dependent....... PASS");
    }

    static void testCountStepsLogLoop16() {
        assertEquals(4, solveCountSteps("log_loop", 16),
            "log_loop with n=16");
        System.out.println("  test_count_steps_log_16.......... PASS");
    }

    static void testCountStepsLogLoop1() {
        assertEquals(0, solveCountSteps("log_loop", 1),
            "log_loop with n=1");
        System.out.println("  test_count_steps_log_1........... PASS");
    }

    static void testCountStepsLogLoop1024() {
        assertEquals(10, solveCountSteps("log_loop", 1024),
            "log_loop with n=1024");
        System.out.println("  test_count_steps_log_1024........ PASS");
    }

    // ── Warmup 02: Is It Fast Enough? ──────────────────────────────

    static void testFastEnoughN2Small() {
        assertEquals(true, solveFastEnough(1000, "n^2"),
            "n^2 with n=1000");
        System.out.println("  test_fast_enough_n2_small........ PASS");
    }

    static void testFastEnoughN2Large() {
        assertEquals(false, solveFastEnough(100000, "n^2"),
            "n^2 with n=100000");
        System.out.println("  test_fast_enough_n2_large........ PASS");
    }

    static void testFastEnoughN2Boundary() {
        assertEquals(false, solveFastEnough(10000, "n^2"),
            "n^2 with n=10000 (exactly 10^8, not strictly less)");
        System.out.println("  test_fast_enough_n2_boundary..... PASS");
    }

    static void testFastEnoughN2JustUnder() {
        assertEquals(true, solveFastEnough(9999, "n^2"),
            "n^2 with n=9999");
        System.out.println("  test_fast_enough_n2_just_under... PASS");
    }

    static void testFastEnough2nSmall() {
        assertEquals(true, solveFastEnough(20, "2^n"),
            "2^n with n=20");
        System.out.println("  test_fast_enough_2n_small........ PASS");
    }

    static void testFastEnough2nLarge() {
        assertEquals(false, solveFastEnough(30, "2^n"),
            "2^n with n=30");
        System.out.println("  test_fast_enough_2n_large........ PASS");
    }

    static void testFastEnoughLinear() {
        assertEquals(true, solveFastEnough(1000000, "n"),
            "n with n=1000000");
        System.out.println("  test_fast_enough_linear.......... PASS");
    }

    // ── Warmup 03: Mystery Complexity ──────────────────────────────

    static void testMysteryConstant() {
        assertEquals("O(1)",
            solveMysteryComplexity(
                new int[]{1, 10, 100, 1000},
                new int[]{5, 5, 5, 5}),
            "Constant complexity");
        System.out.println("  test_mystery_constant............ PASS");
    }

    static void testMysteryLogN() {
        assertEquals("O(log n)",
            solveMysteryComplexity(
                new int[]{1, 2, 4, 8, 16},
                new int[]{0, 1, 2, 3, 4}),
            "Logarithmic complexity");
        System.out.println("  test_mystery_log_n............... PASS");
    }

    static void testMysteryLinear() {
        assertEquals("O(n)",
            solveMysteryComplexity(
                new int[]{100, 200, 400, 800},
                new int[]{100, 200, 400, 800}),
            "Linear complexity");
        System.out.println("  test_mystery_linear.............. PASS");
    }

    static void testMysteryQuadratic() {
        assertEquals("O(n^2)",
            solveMysteryComplexity(
                new int[]{10, 20, 40, 80},
                new int[]{100, 400, 1600, 6400}),
            "Quadratic complexity");
        System.out.println("  test_mystery_quadratic........... PASS");
    }

    // ── Warmup 04: Sum to N ────────────────────────────────────────

    static void testSumToN10() {
        assertArrayEquals(new int[]{55, 55, 55}, solveSumToN(10),
            "Sum 1..10");
        System.out.println("  test_sum_to_n_10................. PASS");
    }

    static void testSumToN1() {
        assertArrayEquals(new int[]{1, 1, 1}, solveSumToN(1),
            "Sum 1..1");
        System.out.println("  test_sum_to_n_1.................. PASS");
    }

    static void testSumToN100() {
        assertArrayEquals(new int[]{5050, 5050, 5050}, solveSumToN(100),
            "Sum 1..100");
        System.out.println("  test_sum_to_n_100................ PASS");
    }

    static void testSumToN0() {
        assertArrayEquals(new int[]{0, 0, 0}, solveSumToN(0),
            "Sum 1..0");
        System.out.println("  test_sum_to_n_0.................. PASS");
    }

    // ── Practice 01: Contains Duplicate ─────────────────────────────

    static void testContainsDupTrue() {
        assertEquals(true, solveContainsDuplicate(new int[]{1, 2, 3, 1}),
            "Contains dup {1,2,3,1}");
        System.out.println("  test_contains_dup_true........... PASS");
    }

    static void testContainsDupFalse() {
        assertEquals(false, solveContainsDuplicate(new int[]{1, 2, 3, 4}),
            "No dup {1,2,3,4}");
        System.out.println("  test_contains_dup_false.......... PASS");
    }

    static void testContainsDupEmpty() {
        assertEquals(false, solveContainsDuplicate(new int[]{}),
            "Empty array");
        System.out.println("  test_contains_dup_empty.......... PASS");
    }

    static void testContainsDupSingle() {
        assertEquals(false, solveContainsDuplicate(new int[]{1}),
            "Single element");
        System.out.println("  test_contains_dup_single......... PASS");
    }

    static void testContainsDupPair() {
        assertEquals(true, solveContainsDuplicate(new int[]{1, 1}),
            "Pair {1,1}");
        System.out.println("  test_contains_dup_pair........... PASS");
    }

    // ── Practice 02: Max Subarray Brute ─────────────────────────────

    static void testMaxSubarrayClassic() {
        assertEquals(6, solveMaxSubarrayBrute(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}),
            "Classic max subarray");
        System.out.println("  test_max_subarray_classic........ PASS");
    }

    static void testMaxSubarraySingle() {
        assertEquals(1, solveMaxSubarrayBrute(new int[]{1}),
            "Single element");
        System.out.println("  test_max_subarray_single......... PASS");
    }

    static void testMaxSubarrayAllNegative() {
        assertEquals(-1, solveMaxSubarrayBrute(new int[]{-1, -2, -3}),
            "All negative");
        System.out.println("  test_max_subarray_all_negative... PASS");
    }

    static void testMaxSubarrayAllPositive() {
        assertEquals(23, solveMaxSubarrayBrute(new int[]{5, 4, -1, 7, 8}),
            "Mostly positive");
        System.out.println("  test_max_subarray_all_positive... PASS");
    }

    static void testMaxSubarrayEmpty() {
        assertEquals(0, solveMaxSubarrayBrute(new int[]{}),
            "Empty array");
        System.out.println("  test_max_subarray_empty.......... PASS");
    }

    // ── Practice 03: Sorted Squares ─────────────────────────────────

    static void testSortedSquaresMixed() {
        assertArrayEquals(new int[]{0, 1, 9, 16, 100},
            solveSortedSquares(new int[]{-4, -1, 0, 3, 10}),
            "Mixed negatives and positives");
        System.out.println("  test_sorted_squares_mixed........ PASS");
    }

    static void testSortedSquaresAllNeg() {
        assertArrayEquals(new int[]{1, 4, 9},
            solveSortedSquares(new int[]{-3, -2, -1}),
            "All negatives");
        System.out.println("  test_sorted_squares_all_neg...... PASS");
    }

    static void testSortedSquaresAllPos() {
        assertArrayEquals(new int[]{0, 1, 4, 9},
            solveSortedSquares(new int[]{0, 1, 2, 3}),
            "All non-negative");
        System.out.println("  test_sorted_squares_all_pos...... PASS");
    }

    static void testSortedSquaresEmpty() {
        assertArrayEquals(new int[]{},
            solveSortedSquares(new int[]{}),
            "Empty array");
        System.out.println("  test_sorted_squares_empty........ PASS");
    }

    static void testSortedSquaresSymmetric() {
        assertArrayEquals(new int[]{25, 25},
            solveSortedSquares(new int[]{-5, 5}),
            "Symmetric {-5, 5}");
        System.out.println("  test_sorted_squares_symmetric.... PASS");
    }

    // ── Practice 04: Majority Element ───────────────────────────────

    static void testMajority3() {
        assertEquals(3, solveMajorityElement(new int[]{3, 2, 3}),
            "Majority of {3,2,3}");
        System.out.println("  test_majority_3.................. PASS");
    }

    static void testMajority2() {
        assertEquals(2, solveMajorityElement(new int[]{2, 2, 1, 1, 1, 2, 2}),
            "Majority of {2,2,1,1,1,2,2}");
        System.out.println("  test_majority_2.................. PASS");
    }

    static void testMajoritySingle() {
        assertEquals(1, solveMajorityElement(new int[]{1}),
            "Majority of {1}");
        System.out.println("  test_majority_single............. PASS");
    }

    static void testMajority6() {
        assertEquals(6, solveMajorityElement(new int[]{6, 6, 6, 7, 7}),
            "Majority of {6,6,6,7,7}");
        System.out.println("  test_majority_6.................. PASS");
    }

    // ── Challenge 01: Two Sum — Three Ways ──────────────────────────

    static void testTwoSumBruteBasic() {
        assertArrayEquals(new int[]{0, 1},
            solveTwoSumBrute(new int[]{2, 7, 11, 15}, 9),
            "Brute: {2,7,11,15} target 9");
        System.out.println("  test_two_sum_brute_basic......... PASS");
    }

    static void testTwoSumBruteDups() {
        assertArrayEquals(new int[]{0, 1},
            solveTwoSumBrute(new int[]{3, 3}, 6),
            "Brute: {3,3} target 6");
        System.out.println("  test_two_sum_brute_dups.......... PASS");
    }

    static void testTwoSumBruteNone() {
        assertArrayEquals(new int[]{-1, -1},
            solveTwoSumBrute(new int[]{1, 2, 3}, 10),
            "Brute: no solution");
        System.out.println("  test_two_sum_brute_none.......... PASS");
    }

    static void testTwoSumBruteMid() {
        assertArrayEquals(new int[]{1, 2},
            solveTwoSumBrute(new int[]{1, 5, 3, 8}, 8),
            "Brute: {1,5,3,8} target 8");
        System.out.println("  test_two_sum_brute_mid........... PASS");
    }

    static void testTwoSumSortBasic() {
        assertArrayEquals(new int[]{0, 1},
            solveTwoSumSort(new int[]{2, 7, 11, 15}, 9),
            "Sort: {2,7,11,15} target 9");
        System.out.println("  test_two_sum_sort_basic.......... PASS");
    }

    static void testTwoSumSortDups() {
        assertArrayEquals(new int[]{0, 1},
            solveTwoSumSort(new int[]{3, 3}, 6),
            "Sort: {3,3} target 6");
        System.out.println("  test_two_sum_sort_dups........... PASS");
    }

    static void testTwoSumSortNone() {
        assertArrayEquals(new int[]{-1, -1},
            solveTwoSumSort(new int[]{1, 2, 3}, 10),
            "Sort: no solution");
        System.out.println("  test_two_sum_sort_none........... PASS");
    }

    static void testTwoSumSortMid() {
        assertArrayEquals(new int[]{1, 2},
            solveTwoSumSort(new int[]{1, 5, 3, 8}, 8),
            "Sort: {1,5,3,8} target 8");
        System.out.println("  test_two_sum_sort_mid............ PASS");
    }

    static void testTwoSumHashBasic() {
        assertArrayEquals(new int[]{0, 1},
            solveTwoSumHash(new int[]{2, 7, 11, 15}, 9),
            "Hash: {2,7,11,15} target 9");
        System.out.println("  test_two_sum_hash_basic.......... PASS");
    }

    static void testTwoSumHashDups() {
        assertArrayEquals(new int[]{0, 1},
            solveTwoSumHash(new int[]{3, 3}, 6),
            "Hash: {3,3} target 6");
        System.out.println("  test_two_sum_hash_dups........... PASS");
    }

    static void testTwoSumHashNone() {
        assertArrayEquals(new int[]{-1, -1},
            solveTwoSumHash(new int[]{1, 2, 3}, 10),
            "Hash: no solution");
        System.out.println("  test_two_sum_hash_none........... PASS");
    }

    static void testTwoSumHashMid() {
        assertArrayEquals(new int[]{1, 2},
            solveTwoSumHash(new int[]{1, 5, 3, 8}, 8),
            "Hash: {1,5,3,8} target 8");
        System.out.println("  test_two_sum_hash_mid............ PASS");
    }

    // ── Challenge 02: Performance Showdown ──────────────────────────

    static void testShowdownBwins() {
        assertEquals("B", solvePerformanceShowdown("n^2", "n_log_n", 1000),
            "n^2 vs n_log_n at n=1000");
        System.out.println("  test_showdown_b_wins............. PASS");
    }

    static void testShowdownTie() {
        assertEquals("TIE", solvePerformanceShowdown("n", "n", 100),
            "n vs n at n=100");
        System.out.println("  test_showdown_tie................ PASS");
    }

    static void testShowdownAwins() {
        assertEquals("A", solvePerformanceShowdown("1", "log_n", 1000000),
            "1 vs log_n at n=1000000");
        System.out.println("  test_showdown_a_wins............. PASS");
    }

    static void testShowdownCubicVsQuadratic() {
        assertEquals("A", solvePerformanceShowdown("n^2", "n^3", 10),
            "n^2 vs n^3 at n=10");
        System.out.println("  test_showdown_cubic_vs_quad...... PASS");
    }

    // ── Runner ───────────────────────────────────────────────────────

    public static void main(String[] args) {

        System.out.println("Testing Chapter 6...\n");

        System.out.println("--- Warmup Problems ---");

        System.out.println("=== Warmup 01: Count the Steps ===");
        testCountStepsSingleLoop();
        testCountStepsDoubleLoop();
        testCountStepsHalfLoop();
        testCountStepsHalfLoopOdd();
        testCountStepsDependentLoop();
        testCountStepsLogLoop16();
        testCountStepsLogLoop1();
        testCountStepsLogLoop1024();
        System.out.println();

        System.out.println("=== Warmup 02: Is It Fast Enough? ===");
        testFastEnoughN2Small();
        testFastEnoughN2Large();
        testFastEnoughN2Boundary();
        testFastEnoughN2JustUnder();
        testFastEnough2nSmall();
        testFastEnough2nLarge();
        testFastEnoughLinear();
        System.out.println();

        System.out.println("=== Warmup 03: Mystery Complexity ===");
        testMysteryConstant();
        testMysteryLogN();
        testMysteryLinear();
        testMysteryQuadratic();
        System.out.println();

        System.out.println("=== Warmup 04: Sum to N ===");
        testSumToN10();
        testSumToN1();
        testSumToN100();
        testSumToN0();
        System.out.println();

        System.out.println("--- Practice Problems ---");

        System.out.println("=== Practice 01: Contains Duplicate ===");
        testContainsDupTrue();
        testContainsDupFalse();
        testContainsDupEmpty();
        testContainsDupSingle();
        testContainsDupPair();
        System.out.println();

        System.out.println("=== Practice 02: Max Subarray Brute ===");
        testMaxSubarrayClassic();
        testMaxSubarraySingle();
        testMaxSubarrayAllNegative();
        testMaxSubarrayAllPositive();
        testMaxSubarrayEmpty();
        System.out.println();

        System.out.println("=== Practice 03: Sorted Squares ===");
        testSortedSquaresMixed();
        testSortedSquaresAllNeg();
        testSortedSquaresAllPos();
        testSortedSquaresEmpty();
        testSortedSquaresSymmetric();
        System.out.println();

        System.out.println("=== Practice 04: Majority Element ===");
        testMajority3();
        testMajority2();
        testMajoritySingle();
        testMajority6();
        System.out.println();

        System.out.println("--- Challenge Problems ---");

        System.out.println("=== Challenge 01: Two Sum — Three Ways ===");
        testTwoSumBruteBasic();
        testTwoSumBruteDups();
        testTwoSumBruteNone();
        testTwoSumBruteMid();
        System.out.println();
        testTwoSumSortBasic();
        testTwoSumSortDups();
        testTwoSumSortNone();
        testTwoSumSortMid();
        System.out.println();
        testTwoSumHashBasic();
        testTwoSumHashDups();
        testTwoSumHashNone();
        testTwoSumHashMid();
        System.out.println();

        System.out.println("=== Challenge 02: Performance Showdown ===");
        testShowdownBwins();
        testShowdownTie();
        testShowdownAwins();
        testShowdownCubicVsQuadratic();
        System.out.println();

        System.out.println("All tests passed!");
    }
}
