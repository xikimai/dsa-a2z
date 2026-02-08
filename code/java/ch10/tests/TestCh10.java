package ch10.tests;

import java.util.*;

/**
 * Tests for Chapter 10: The Magic of Recursion
 *
 * Build and run:
 *   cd code/java
 *   javac ch10/tests/TestCh10.java
 *   java -ea ch10.tests.TestCh10
 */
public class TestCh10 {

    // ── Helper methods ───────────────────────────────────────────────

    static void assertEquals(long expected, long actual, String msg) {
        assert expected == actual
            : msg + " — expected " + expected + ", got " + actual;
    }

    static void assertEquals(int expected, int actual, String msg) {
        assert expected == actual
            : msg + " — expected " + expected + ", got " + actual;
    }

    static void assertBoolEquals(boolean expected, boolean actual, String msg) {
        assert expected == actual
            : msg + " — expected " + expected + ", got " + actual;
    }

    static void assertStringEquals(String expected, String actual, String msg) {
        assert expected.equals(actual)
            : msg + " — expected \"" + expected + "\", got \"" + actual + "\"";
    }

    static void assertListEquals(List<List<Integer>> expected, List<List<Integer>> actual, String msg) {
        assert expected.size() == actual.size()
            : msg + " — expected " + expected.size() + " items, got " + actual.size()
              + "\n  expected: " + expected + "\n  actual:   " + actual;
        for (int i = 0; i < expected.size(); i++) {
            assert expected.get(i).equals(actual.get(i))
                : msg + " — mismatch at index " + i
                  + "\n  expected: " + expected + "\n  actual:   " + actual;
        }
    }

    // ── Reference solutions ─────────────────────────────────────────

    // W1: Factorial
    static long solveFactorial(int n) {
        if (n == 0) return 1;
        return (long) n * solveFactorial(n - 1);
    }

    // W2: Sum First N
    static int solveSumFirstN(int n) {
        if (n == 0) return 0;
        return n + solveSumFirstN(n - 1);
    }

    // W3: Reverse String
    static String solveReverseString(String s) {
        if (s.length() <= 1) return s;
        return solveReverseString(s.substring(1)) + s.charAt(0);
    }

    // W4: Check Palindrome
    static boolean solveCheckPalindrome(String s) {
        if (s.length() <= 1) return true;
        if (s.charAt(0) != s.charAt(s.length() - 1)) return false;
        return solveCheckPalindrome(s.substring(1, s.length() - 1));
    }

    // W5: Power
    static long solvePower(int base, int exp) {
        if (exp == 0) return 1;
        return (long) base * solvePower(base, exp - 1);
    }

    // P1: Fibonacci (memoized)
    static int solveFibonacci(int n) {
        return fibHelper(n, new HashMap<>());
    }

    static int fibHelper(int n, HashMap<Integer, Integer> memo) {
        if (n <= 1) return n;
        if (memo.containsKey(n)) return memo.get(n);
        int result = fibHelper(n - 1, memo) + fibHelper(n - 2, memo);
        memo.put(n, result);
        return result;
    }

    // P2: Sum Digits
    static int solveSumDigits(int n) {
        n = Math.abs(n);
        if (n < 10) return n;
        return n % 10 + solveSumDigits(n / 10);
    }

    // P3: Count Occurrences
    static int solveCountOccurrences(int[] arr, int target) {
        return countHelper(arr, target, 0);
    }

    static int countHelper(int[] arr, int target, int idx) {
        if (idx == arr.length) return 0;
        int count = (arr[idx] == target) ? 1 : 0;
        return count + countHelper(arr, target, idx + 1);
    }

    // P4: Binary Search Recursive
    static int solveBinarySearchRecursive(int[] arr, int target) {
        return bsHelper(arr, target, 0, arr.length - 1);
    }

    static int bsHelper(int[] arr, int target, int lo, int hi) {
        if (lo > hi) return -1;
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) return bsHelper(arr, target, mid + 1, hi);
        return bsHelper(arr, target, lo, mid - 1);
    }

    // P5: Generate Subsets
    static List<List<Integer>> solveGenerateSubsets(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        subsetHelper(nums, 0, new ArrayList<>(), result);
        result.sort((a, b) -> {
            if (a.size() != b.size()) return a.size() - b.size();
            for (int i = 0; i < a.size(); i++) {
                if (!a.get(i).equals(b.get(i))) return a.get(i) - b.get(i);
            }
            return 0;
        });
        return result;
    }

    static void subsetHelper(int[] nums, int idx, List<Integer> current,
                             List<List<Integer>> result) {
        if (idx == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        subsetHelper(nums, idx + 1, current, result);
        current.add(nums[idx]);
        subsetHelper(nums, idx + 1, current, result);
        current.remove(current.size() - 1);
    }

    // C1: Fibonacci Three Ways
    static long solveFibNaive(int n) {
        if (n <= 1) return n;
        return solveFibNaive(n - 1) + solveFibNaive(n - 2);
    }

    static long solveFibMemo(int n) {
        return fibMemoHelper(n, new HashMap<>());
    }

    static long fibMemoHelper(int n, HashMap<Integer, Long> memo) {
        if (n <= 1) return n;
        if (memo.containsKey(n)) return memo.get(n);
        long result = fibMemoHelper(n - 1, memo) + fibMemoHelper(n - 2, memo);
        memo.put(n, result);
        return result;
    }

    static long solveFibIter(int n) {
        if (n <= 1) return n;
        long a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            long temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }

    // C2: Generate Permutations
    static List<List<Integer>> solveGeneratePermutations(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        permHelper(nums, used, new ArrayList<>(), result);
        return result;
    }

    static void permHelper(int[] nums, boolean[] used, List<Integer> current,
                           List<List<Integer>> result) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            current.add(nums[i]);
            permHelper(nums, used, current, result);
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }

    // C3: Combination Sum
    static List<List<Integer>> solveCombinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        comboHelper(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }

    static void comboHelper(int[] candidates, int remaining, int start,
                            List<Integer> current, List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(current));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remaining) break;
            current.add(candidates[i]);
            comboHelper(candidates, remaining - candidates[i], i, current, result);
            current.remove(current.size() - 1);
        }
    }

    // C4: Subset Sum
    static boolean solveSubsetSum(int[] nums, int target) {
        return ssHelper(nums, 0, target);
    }

    static boolean ssHelper(int[] nums, int idx, int remaining) {
        if (remaining == 0) return true;
        if (idx == nums.length || remaining < 0) return false;
        return ssHelper(nums, idx + 1, remaining - nums[idx])
            || ssHelper(nums, idx + 1, remaining);
    }

    // ── Warmup 01: Factorial ────────────────────────────────────────

    static void testFactorial() {
        System.out.println("=== Warmup 01: Factorial ===");
        assertEquals(1L, solveFactorial(0), "factorial(0)");
        System.out.println("  test_factorial_zero.............. PASS");

        assertEquals(1L, solveFactorial(1), "factorial(1)");
        System.out.println("  test_factorial_one............... PASS");

        assertEquals(120L, solveFactorial(5), "factorial(5)");
        System.out.println("  test_factorial_five.............. PASS");

        assertEquals(3628800L, solveFactorial(10), "factorial(10)");
        System.out.println("  test_factorial_ten............... PASS");

        assertEquals(2432902008176640000L, solveFactorial(20), "factorial(20)");
        System.out.println("  test_factorial_twenty............ PASS");
        System.out.println();
    }

    // ── Warmup 02: Sum First N ──────────────────────────────────────

    static void testSumFirstN() {
        System.out.println("=== Warmup 02: Sum First N ===");
        assertEquals(0, solveSumFirstN(0), "sum(0)");
        System.out.println("  test_sum_zero.................... PASS");

        assertEquals(1, solveSumFirstN(1), "sum(1)");
        System.out.println("  test_sum_one..................... PASS");

        assertEquals(15, solveSumFirstN(5), "sum(5)");
        System.out.println("  test_sum_five.................... PASS");

        assertEquals(5050, solveSumFirstN(100), "sum(100)");
        System.out.println("  test_sum_hundred................. PASS");
        System.out.println();
    }

    // ── Warmup 03: Reverse String ───────────────────────────────────

    static void testReverseString() {
        System.out.println("=== Warmup 03: Reverse String ===");
        assertStringEquals("olleh", solveReverseString("hello"), "reverse hello");
        System.out.println("  test_reverse_hello............... PASS");

        assertStringEquals("", solveReverseString(""), "reverse empty");
        System.out.println("  test_reverse_empty............... PASS");

        assertStringEquals("a", solveReverseString("a"), "reverse single");
        System.out.println("  test_reverse_single.............. PASS");

        assertStringEquals("dcba", solveReverseString("abcd"), "reverse abcd");
        System.out.println("  test_reverse_abcd................ PASS");
        System.out.println();
    }

    // ── Warmup 04: Check Palindrome ─────────────────────────────────

    static void testCheckPalindrome() {
        System.out.println("=== Warmup 04: Check Palindrome ===");
        assertBoolEquals(true, solveCheckPalindrome("racecar"), "palindrome racecar");
        System.out.println("  test_palindrome_racecar.......... PASS");

        assertBoolEquals(false, solveCheckPalindrome("hello"), "palindrome hello");
        System.out.println("  test_palindrome_hello............ PASS");

        assertBoolEquals(true, solveCheckPalindrome(""), "palindrome empty");
        System.out.println("  test_palindrome_empty............ PASS");

        assertBoolEquals(true, solveCheckPalindrome("a"), "palindrome single");
        System.out.println("  test_palindrome_single........... PASS");

        assertBoolEquals(true, solveCheckPalindrome("abba"), "palindrome abba");
        System.out.println("  test_palindrome_abba............. PASS");
        System.out.println();
    }

    // ── Warmup 05: Power ────────────────────────────────────────────

    static void testPower() {
        System.out.println("=== Warmup 05: Power ===");
        assertEquals(1L, solvePower(2, 0), "power(2,0)");
        System.out.println("  test_power_zero_exp.............. PASS");

        assertEquals(1024L, solvePower(2, 10), "power(2,10)");
        System.out.println("  test_power_2_10.................. PASS");

        assertEquals(81L, solvePower(3, 4), "power(3,4)");
        System.out.println("  test_power_3_4................... PASS");

        assertEquals(1L, solvePower(1, 20), "power(1,20)");
        System.out.println("  test_power_one_base.............. PASS");

        assertEquals(1L, solvePower(0, 0), "power(0,0)");
        System.out.println("  test_power_zero_zero............. PASS");
        System.out.println();
    }

    // ── Practice 01: Fibonacci ──────────────────────────────────────

    static void testFibonacci() {
        System.out.println("=== Practice 01: Fibonacci ===");
        assertEquals(0, solveFibonacci(0), "fib(0)");
        System.out.println("  test_fib_zero.................... PASS");

        assertEquals(1, solveFibonacci(1), "fib(1)");
        System.out.println("  test_fib_one..................... PASS");

        assertEquals(55, solveFibonacci(10), "fib(10)");
        System.out.println("  test_fib_ten..................... PASS");

        assertEquals(610, solveFibonacci(15), "fib(15)");
        System.out.println("  test_fib_fifteen................. PASS");
        System.out.println();
    }

    // ── Practice 02: Sum Digits ─────────────────────────────────────

    static void testSumDigits() {
        System.out.println("=== Practice 02: Sum Digits ===");
        assertEquals(15, solveSumDigits(12345), "sumDigits(12345)");
        System.out.println("  test_sum_digits_12345............ PASS");

        assertEquals(0, solveSumDigits(0), "sumDigits(0)");
        System.out.println("  test_sum_digits_zero............. PASS");

        assertEquals(27, solveSumDigits(999), "sumDigits(999)");
        System.out.println("  test_sum_digits_999.............. PASS");

        assertEquals(6, solveSumDigits(-123), "sumDigits(-123)");
        System.out.println("  test_sum_digits_negative......... PASS");
        System.out.println();
    }

    // ── Practice 03: Count Occurrences ──────────────────────────────

    static void testCountOccurrences() {
        System.out.println("=== Practice 03: Count Occurrences ===");
        assertEquals(3, solveCountOccurrences(new int[]{1,2,3,2,4,2}, 2), "count 2s");
        System.out.println("  test_count_multiple.............. PASS");

        assertEquals(0, solveCountOccurrences(new int[]{1,2,3}, 4), "count missing");
        System.out.println("  test_count_missing............... PASS");

        assertEquals(0, solveCountOccurrences(new int[]{}, 1), "count empty");
        System.out.println("  test_count_empty................. PASS");

        assertEquals(5, solveCountOccurrences(new int[]{7,7,7,7,7}, 7), "count all same");
        System.out.println("  test_count_all_same.............. PASS");
        System.out.println();
    }

    // ── Practice 04: Binary Search Recursive ────────────────────────

    static void testBinarySearchRecursive() {
        System.out.println("=== Practice 04: Binary Search Recursive ===");
        assertEquals(2, solveBinarySearchRecursive(new int[]{1,3,5,7,9}, 5), "bs found");
        System.out.println("  test_bs_found.................... PASS");

        assertEquals(-1, solveBinarySearchRecursive(new int[]{1,3,5,7,9}, 4), "bs not found");
        System.out.println("  test_bs_not_found................ PASS");

        assertEquals(-1, solveBinarySearchRecursive(new int[]{}, 1), "bs empty");
        System.out.println("  test_bs_empty.................... PASS");

        assertEquals(0, solveBinarySearchRecursive(new int[]{5}, 5), "bs single found");
        System.out.println("  test_bs_single_found............. PASS");

        assertEquals(0, solveBinarySearchRecursive(new int[]{1,3,5,7,9}, 1), "bs first");
        System.out.println("  test_bs_first.................... PASS");

        assertEquals(4, solveBinarySearchRecursive(new int[]{1,3,5,7,9}, 9), "bs last");
        System.out.println("  test_bs_last..................... PASS");
        System.out.println();
    }

    // ── Practice 05: Generate Subsets ───────────────────────────────

    static void testGenerateSubsets() {
        System.out.println("=== Practice 05: Generate Subsets ===");

        // Empty input
        List<List<Integer>> r1 = solveGenerateSubsets(new int[]{});
        List<List<Integer>> e1 = new ArrayList<>();
        e1.add(new ArrayList<>());
        assertListEquals(e1, r1, "subsets empty");
        System.out.println("  test_subsets_empty............... PASS");

        // Single element
        List<List<Integer>> r2 = solveGenerateSubsets(new int[]{1});
        List<List<Integer>> e2 = new ArrayList<>();
        e2.add(new ArrayList<>());
        e2.add(Arrays.asList(1));
        assertListEquals(e2, r2, "subsets single");
        System.out.println("  test_subsets_single.............. PASS");

        // Three elements
        List<List<Integer>> r3 = solveGenerateSubsets(new int[]{1, 2, 3});
        assertEquals(8, r3.size(), "subsets {1,2,3} count");
        List<List<Integer>> e3 = new ArrayList<>();
        e3.add(new ArrayList<>());
        e3.add(Arrays.asList(1));
        e3.add(Arrays.asList(2));
        e3.add(Arrays.asList(3));
        e3.add(Arrays.asList(1, 2));
        e3.add(Arrays.asList(1, 3));
        e3.add(Arrays.asList(2, 3));
        e3.add(Arrays.asList(1, 2, 3));
        assertListEquals(e3, r3, "subsets {1,2,3}");
        System.out.println("  test_subsets_three............... PASS");
        System.out.println();
    }

    // ── Challenge 01: Fibonacci Three Ways ──────────────────────────

    static void testFibonacciThreeWays() {
        System.out.println("=== Challenge 01: Fibonacci Three Ways ===");

        // Naive (small n only)
        assertEquals(55L, solveFibNaive(10), "fibNaive(10)");
        System.out.println("  test_fib_naive_10................ PASS");

        assertEquals(610L, solveFibNaive(15), "fibNaive(15)");
        System.out.println("  test_fib_naive_15................ PASS");

        // Memo (larger n)
        assertEquals(832040L, solveFibMemo(30), "fibMemo(30)");
        System.out.println("  test_fib_memo_30................. PASS");

        assertEquals(0L, solveFibMemo(0), "fibMemo(0)");
        System.out.println("  test_fib_memo_0.................. PASS");

        // Iterative (larger n)
        assertEquals(832040L, solveFibIter(30), "fibIter(30)");
        System.out.println("  test_fib_iter_30................. PASS");

        assertEquals(0L, solveFibIter(0), "fibIter(0)");
        System.out.println("  test_fib_iter_0.................. PASS");

        assertEquals(1L, solveFibIter(1), "fibIter(1)");
        System.out.println("  test_fib_iter_1.................. PASS");

        // Memo and iter agree
        assertEquals(solveFibMemo(25), solveFibIter(25), "memo==iter for n=25");
        System.out.println("  test_fib_memo_iter_agree......... PASS");
        System.out.println();
    }

    // ── Challenge 02: Generate Permutations ─────────────────────────

    static void testGeneratePermutations() {
        System.out.println("=== Challenge 02: Generate Permutations ===");

        // Single element
        List<List<Integer>> r1 = solveGeneratePermutations(new int[]{1});
        List<List<Integer>> e1 = new ArrayList<>();
        e1.add(Arrays.asList(1));
        assertListEquals(e1, r1, "perms single");
        System.out.println("  test_perms_single................ PASS");

        // Three elements
        List<List<Integer>> r2 = solveGeneratePermutations(new int[]{1, 2, 3});
        assertEquals(6, r2.size(), "perms {1,2,3} count");
        List<List<Integer>> e2 = new ArrayList<>();
        e2.add(Arrays.asList(1, 2, 3));
        e2.add(Arrays.asList(1, 3, 2));
        e2.add(Arrays.asList(2, 1, 3));
        e2.add(Arrays.asList(2, 3, 1));
        e2.add(Arrays.asList(3, 1, 2));
        e2.add(Arrays.asList(3, 2, 1));
        assertListEquals(e2, r2, "perms {1,2,3}");
        System.out.println("  test_perms_three................. PASS");

        // Two elements
        List<List<Integer>> r3 = solveGeneratePermutations(new int[]{1, 2});
        assertEquals(2, r3.size(), "perms {1,2} count");
        System.out.println("  test_perms_two................... PASS");
        System.out.println();
    }

    // ── Challenge 03: Combination Sum ───────────────────────────────

    static void testCombinationSum() {
        System.out.println("=== Challenge 03: Combination Sum ===");

        // Standard case
        List<List<Integer>> r1 = solveCombinationSum(new int[]{2, 3, 6, 7}, 7);
        List<List<Integer>> e1 = new ArrayList<>();
        e1.add(Arrays.asList(2, 2, 3));
        e1.add(Arrays.asList(7));
        assertListEquals(e1, r1, "combo {2,3,6,7} target 7");
        System.out.println("  test_combo_standard.............. PASS");

        // No solution
        List<List<Integer>> r2 = solveCombinationSum(new int[]{2}, 1);
        assertEquals(0, r2.size(), "combo {2} target 1");
        System.out.println("  test_combo_no_solution........... PASS");

        // Single candidate matches
        List<List<Integer>> r3 = solveCombinationSum(new int[]{1}, 1);
        List<List<Integer>> e3 = new ArrayList<>();
        e3.add(Arrays.asList(1));
        assertListEquals(e3, r3, "combo {1} target 1");
        System.out.println("  test_combo_single_match.......... PASS");

        // Multiple reuse
        List<List<Integer>> r4 = solveCombinationSum(new int[]{2, 3, 5}, 8);
        List<List<Integer>> e4 = new ArrayList<>();
        e4.add(Arrays.asList(2, 2, 2, 2));
        e4.add(Arrays.asList(2, 3, 3));
        e4.add(Arrays.asList(3, 5));
        assertListEquals(e4, r4, "combo {2,3,5} target 8");
        System.out.println("  test_combo_multiple_reuse........ PASS");
        System.out.println();
    }

    // ── Challenge 04: Subset Sum ────────────────────────────────────

    static void testSubsetSum() {
        System.out.println("=== Challenge 04: Subset Sum ===");

        assertBoolEquals(true, solveSubsetSum(new int[]{3, 34, 4, 12, 5, 2}, 9),
            "subset sum 9");
        System.out.println("  test_subset_sum_exists........... PASS");

        assertBoolEquals(false, solveSubsetSum(new int[]{3, 34, 4, 12, 5, 2}, 30),
            "subset sum 30");
        System.out.println("  test_subset_sum_not_exists....... PASS");

        assertBoolEquals(true, solveSubsetSum(new int[]{}, 0), "subset sum empty target 0");
        System.out.println("  test_subset_sum_empty_zero....... PASS");

        assertBoolEquals(false, solveSubsetSum(new int[]{}, 1), "subset sum empty target 1");
        System.out.println("  test_subset_sum_empty_nonzero.... PASS");

        assertBoolEquals(true, solveSubsetSum(new int[]{1, 2, 3}, 6), "subset sum all");
        System.out.println("  test_subset_sum_all.............. PASS");

        assertBoolEquals(true, solveSubsetSum(new int[]{5}, 5), "subset sum single match");
        System.out.println("  test_subset_sum_single_match..... PASS");

        assertBoolEquals(false, solveSubsetSum(new int[]{5}, 3), "subset sum single no match");
        System.out.println("  test_subset_sum_single_no_match.. PASS");
        System.out.println();
    }

    // ── Runner ───────────────────────────────────────────────────────

    public static void main(String[] args) {

        System.out.println("Testing Chapter 10...\n");

        System.out.println("--- Warmup Problems ---");
        testFactorial();
        testSumFirstN();
        testReverseString();
        testCheckPalindrome();
        testPower();

        System.out.println("--- Practice Problems ---");
        testFibonacci();
        testSumDigits();
        testCountOccurrences();
        testBinarySearchRecursive();
        testGenerateSubsets();

        System.out.println("--- Challenge Problems ---");
        testFibonacciThreeWays();
        testGeneratePermutations();
        testCombinationSum();
        testSubsetSum();

        System.out.println("All tests passed!");
    }
}
