package ch03.tests;

import java.util.*;

/**
 * Tests for Chapter 3: Decisions and Loops
 * ==========================================
 * Chapter 3: Decisions and Loops
 *
 * This file tests every solve() method from Chapter 3 using the reference
 * solutions. We define each solve() here so the test is self-contained.
 *
 * Build and run:
 *   cd code/java
 *   javac ch03/tests/TestCh03.java
 *   java -ea ch03.tests.TestCh03
 *
 * The -ea flag enables assertions. Without it, assert statements are ignored!
 */
public class TestCh03 {

    // ── Reference solutions ─────────────────────────────────────────

    static String solveEvenOdd(int n) {
        return (n % 2 == 0) ? "Even" : "Odd";
    }

    static int solveAbsoluteValue(int n) {
        if (n < 0) return -n;
        return n;
    }

    static int solveLargestOfThree(int a, int b, int c) {
        int max = a;
        if (b > max) max = b;
        if (c > max) max = c;
        return max;
    }

    static List<Integer> solveCountDown(int n) {
        List<Integer> result = new ArrayList<>();
        for (int i = n; i >= 1; i--) {
            result.add(i);
        }
        return result;
    }

    static int solveSum1ToN(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }

    static List<String> solveMultiplicationTable(int n) {
        List<String> table = new ArrayList<>();
        for (int i = 1; i <= 10; i++) {
            table.add(i + " x " + n + " = " + (i * n));
        }
        return table;
    }

    static List<String> solveFizzbuzz(int n) {
        List<String> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) result.add("FizzBuzz");
            else if (i % 3 == 0) result.add("Fizz");
            else if (i % 5 == 0) result.add("Buzz");
            else result.add(String.valueOf(i));
        }
        return result;
    }

    static int solveDigitCount(int n) {
        if (n == 0) return 1;
        int count = 0;
        if (n < 0) n = -n;
        while (n > 0) {
            n /= 10;
            count++;
        }
        return count;
    }

    static int solveReverseNumber(int n) {
        int sign = (n < 0) ? -1 : 1;
        int num = (n < 0) ? -n : n;
        int reversed = 0;
        while (num > 0) {
            reversed = reversed * 10 + num % 10;
            num /= 10;
        }
        return sign * reversed;
    }

    static String solveRightTriangle(int n) {
        StringBuilder sb = new StringBuilder();
        for (int row = 1; row <= n; row++) {
            for (int s = 0; s < n - row; s++) sb.append(' ');
            for (int s = 0; s < row; s++) sb.append('*');
            if (row < n) sb.append('\n');
        }
        return sb.toString();
    }

    static String solveDiamond(int n) {
        int totalRows = 2 * n - 1;
        StringBuilder sb = new StringBuilder();
        for (int r = 1; r <= totalRows; r++) {
            int dist = Math.abs(r - n);
            for (int s = 0; s < dist; s++) sb.append(' ');
            for (int s = 0; s < 2 * (n - dist) - 1; s++) sb.append('*');
            if (r < totalRows) sb.append('\n');
        }
        return sb.toString();
    }

    static boolean solvePrimeCheck(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }

    static List<Integer> solveCollatz(int n) {
        List<Integer> seq = new ArrayList<>();
        seq.add(n);
        while (n != 1) {
            if (n % 2 == 0) n = n / 2;
            else n = 3 * n + 1;
            seq.add(n);
        }
        return seq;
    }

    // ── Warmup 01: Even or Odd ────────────────────────────────────

    static void testEvenOddEven() {
        assert solveEvenOdd(4).equals("Even")
            : "Expected 'Even' for 4";
        System.out.println("  test_even_odd_even............... PASS");
    }

    static void testEvenOddOdd() {
        assert solveEvenOdd(7).equals("Odd")
            : "Expected 'Odd' for 7";
        System.out.println("  test_even_odd_odd................ PASS");
    }

    static void testEvenOddZero() {
        assert solveEvenOdd(0).equals("Even")
            : "Expected 'Even' for 0";
        System.out.println("  test_even_odd_zero............... PASS");
    }

    static void testEvenOddNegative() {
        assert solveEvenOdd(-3).equals("Odd")
            : "Expected 'Odd' for -3";
        System.out.println("  test_even_odd_negative........... PASS");
    }

    static void testEvenOddOne() {
        assert solveEvenOdd(1).equals("Odd")
            : "Expected 'Odd' for 1";
        System.out.println("  test_even_odd_one................ PASS");
    }

    // ── Warmup 02: Absolute Value ─────────────────────────────────

    static void testAbsPositive() {
        assert solveAbsoluteValue(5) == 5
            : "Expected 5, got " + solveAbsoluteValue(5);
        System.out.println("  test_abs_positive................ PASS");
    }

    static void testAbsNegative() {
        assert solveAbsoluteValue(-5) == 5
            : "Expected 5, got " + solveAbsoluteValue(-5);
        System.out.println("  test_abs_negative................ PASS");
    }

    static void testAbsZero() {
        assert solveAbsoluteValue(0) == 0
            : "Expected 0";
        System.out.println("  test_abs_zero.................... PASS");
    }

    static void testAbsLargeNeg() {
        assert solveAbsoluteValue(-100) == 100
            : "Expected 100";
        System.out.println("  test_abs_large_negative.......... PASS");
    }

    static void testAbsOne() {
        assert solveAbsoluteValue(1) == 1
            : "Expected 1";
        System.out.println("  test_abs_one..................... PASS");
    }

    // ── Warmup 03: Largest of Three ───────────────────────────────

    static void testLargestAscending() {
        assert solveLargestOfThree(1, 2, 3) == 3
            : "Expected 3";
        System.out.println("  test_largest_ascending........... PASS");
    }

    static void testLargestDescending() {
        assert solveLargestOfThree(3, 2, 1) == 3
            : "Expected 3";
        System.out.println("  test_largest_descending.......... PASS");
    }

    static void testLargestAllEqual() {
        assert solveLargestOfThree(5, 5, 5) == 5
            : "Expected 5";
        System.out.println("  test_largest_all_equal........... PASS");
    }

    static void testLargestNegatives() {
        assert solveLargestOfThree(-1, -2, -3) == -1
            : "Expected -1";
        System.out.println("  test_largest_negatives........... PASS");
    }

    static void testLargestTied() {
        assert solveLargestOfThree(10, 5, 10) == 10
            : "Expected 10";
        System.out.println("  test_largest_tied................ PASS");
    }

    // ── Warmup 04: Count Down ─────────────────────────────────────

    static void testCountDown5() {
        assert solveCountDown(5).equals(Arrays.asList(5, 4, 3, 2, 1))
            : "Expected [5, 4, 3, 2, 1]";
        System.out.println("  test_countdown_5................. PASS");
    }

    static void testCountDown1() {
        assert solveCountDown(1).equals(Arrays.asList(1))
            : "Expected [1]";
        System.out.println("  test_countdown_1................. PASS");
    }

    static void testCountDown3() {
        assert solveCountDown(3).equals(Arrays.asList(3, 2, 1))
            : "Expected [3, 2, 1]";
        System.out.println("  test_countdown_3................. PASS");
    }

    // ── Warmup 05: Sum 1 to N ────────────────────────────────────

    static void testSum5() {
        assert solveSum1ToN(5) == 15
            : "Expected 15, got " + solveSum1ToN(5);
        System.out.println("  test_sum_5....................... PASS");
    }

    static void testSum1() {
        assert solveSum1ToN(1) == 1
            : "Expected 1";
        System.out.println("  test_sum_1....................... PASS");
    }

    static void testSum10() {
        assert solveSum1ToN(10) == 55
            : "Expected 55";
        System.out.println("  test_sum_10...................... PASS");
    }

    static void testSum100() {
        assert solveSum1ToN(100) == 5050
            : "Expected 5050";
        System.out.println("  test_sum_100..................... PASS");
    }

    static void testSum0() {
        assert solveSum1ToN(0) == 0
            : "Expected 0";
        System.out.println("  test_sum_0....................... PASS");
    }

    // ── Warmup 06: Multiplication Table ───────────────────────────

    static void testMultTableFirst() {
        List<String> table = solveMultiplicationTable(7);
        assert table.get(0).equals("1 x 7 = 7")
            : "Expected '1 x 7 = 7', got '" + table.get(0) + "'";
        System.out.println("  test_mult_table_first............ PASS");
    }

    static void testMultTableLast() {
        List<String> table = solveMultiplicationTable(7);
        assert table.get(9).equals("10 x 7 = 70")
            : "Expected '10 x 7 = 70', got '" + table.get(9) + "'";
        System.out.println("  test_mult_table_last............. PASS");
    }

    static void testMultTableSize() {
        List<String> table = solveMultiplicationTable(7);
        assert table.size() == 10
            : "Expected size 10, got " + table.size();
        System.out.println("  test_mult_table_size............. PASS");
    }

    static void testMultTableMiddle() {
        List<String> table = solveMultiplicationTable(3);
        assert table.get(4).equals("5 x 3 = 15")
            : "Expected '5 x 3 = 15', got '" + table.get(4) + "'";
        System.out.println("  test_mult_table_middle........... PASS");
    }

    // ── Practice 01: FizzBuzz ─────────────────────────────────────

    static void testFizzbuzz15() {
        List<String> result = solveFizzbuzz(15);
        assert result.get(14).equals("FizzBuzz")
            : "Expected 'FizzBuzz' at index 14, got '" + result.get(14) + "'";
        System.out.println("  test_fizzbuzz_15................. PASS");
    }

    static void testFizzbuzzFizz() {
        List<String> result = solveFizzbuzz(15);
        assert result.get(2).equals("Fizz")
            : "Expected 'Fizz' at index 2, got '" + result.get(2) + "'";
        System.out.println("  test_fizzbuzz_fizz............... PASS");
    }

    static void testFizzbuzzBuzz() {
        List<String> result = solveFizzbuzz(15);
        assert result.get(4).equals("Buzz")
            : "Expected 'Buzz' at index 4, got '" + result.get(4) + "'";
        System.out.println("  test_fizzbuzz_buzz............... PASS");
    }

    static void testFizzbuzzNumber() {
        List<String> result = solveFizzbuzz(15);
        assert result.get(0).equals("1")
            : "Expected '1' at index 0, got '" + result.get(0) + "'";
        System.out.println("  test_fizzbuzz_number............. PASS");
    }

    static void testFizzbuzzSize() {
        List<String> result = solveFizzbuzz(15);
        assert result.size() == 15
            : "Expected size 15, got " + result.size();
        System.out.println("  test_fizzbuzz_size............... PASS");
    }

    // ── Practice 02: Digit Count ──────────────────────────────────

    static void testDigitCount5Digits() {
        assert solveDigitCount(12345) == 5
            : "Expected 5, got " + solveDigitCount(12345);
        System.out.println("  test_digit_count_5_digits........ PASS");
    }

    static void testDigitCountZero() {
        assert solveDigitCount(0) == 1
            : "Expected 1, got " + solveDigitCount(0);
        System.out.println("  test_digit_count_zero............ PASS");
    }

    static void testDigitCountSingle() {
        assert solveDigitCount(9) == 1
            : "Expected 1";
        System.out.println("  test_digit_count_single.......... PASS");
    }

    static void testDigitCountNegative() {
        assert solveDigitCount(-42) == 2
            : "Expected 2, got " + solveDigitCount(-42);
        System.out.println("  test_digit_count_negative........ PASS");
    }

    static void testDigitCountMillion() {
        assert solveDigitCount(1000000) == 7
            : "Expected 7, got " + solveDigitCount(1000000);
        System.out.println("  test_digit_count_million......... PASS");
    }

    // ── Practice 03: Reverse Number ───────────────────────────────

    static void testReverse1234() {
        assert solveReverseNumber(1234) == 4321
            : "Expected 4321, got " + solveReverseNumber(1234);
        System.out.println("  test_reverse_1234................ PASS");
    }

    static void testReverseTrailingZeros() {
        assert solveReverseNumber(1200) == 21
            : "Expected 21, got " + solveReverseNumber(1200);
        System.out.println("  test_reverse_trailing_zeros...... PASS");
    }

    static void testReverseSingleDigit() {
        assert solveReverseNumber(5) == 5
            : "Expected 5";
        System.out.println("  test_reverse_single_digit........ PASS");
    }

    static void testReverseNegative() {
        assert solveReverseNumber(-123) == -321
            : "Expected -321, got " + solveReverseNumber(-123);
        System.out.println("  test_reverse_negative............ PASS");
    }

    static void testReverseZero() {
        assert solveReverseNumber(0) == 0
            : "Expected 0";
        System.out.println("  test_reverse_zero................ PASS");
    }

    // ── Practice 04: Right-Aligned Triangle ───────────────────────

    static void testTriangle1() {
        assert solveRightTriangle(1).equals("*")
            : "Expected '*', got '" + solveRightTriangle(1) + "'";
        System.out.println("  test_triangle_1.................. PASS");
    }

    static void testTriangle3() {
        String expected = "  *\n **\n***";
        assert solveRightTriangle(3).equals(expected)
            : "Expected:\n" + expected + "\nGot:\n" + solveRightTriangle(3);
        System.out.println("  test_triangle_3.................. PASS");
    }

    static void testTriangle4() {
        String expected = "   *\n  **\n ***\n****";
        assert solveRightTriangle(4).equals(expected)
            : "Expected:\n" + expected + "\nGot:\n" + solveRightTriangle(4);
        System.out.println("  test_triangle_4.................. PASS");
    }

    static void testTriangleNoTrailingNewline() {
        String result = solveRightTriangle(3);
        assert !result.endsWith("\n")
            : "Should not end with a trailing newline";
        System.out.println("  test_triangle_no_trailing_nl..... PASS");
    }

    // ── Challenge 01: Diamond ─────────────────────────────────────

    static void testDiamond1() {
        assert solveDiamond(1).equals("*")
            : "Expected '*', got '" + solveDiamond(1) + "'";
        System.out.println("  test_diamond_1................... PASS");
    }

    static void testDiamond2() {
        String expected = " *\n***\n *";
        assert solveDiamond(2).equals(expected)
            : "Expected:\n" + expected + "\nGot:\n" + solveDiamond(2);
        System.out.println("  test_diamond_2................... PASS");
    }

    static void testDiamond3() {
        String expected = "  *\n ***\n*****\n ***\n  *";
        String result = solveDiamond(3);
        assert result.split("\n").length == 5
            : "Expected 5 lines, got " + result.split("\n").length;
        assert result.equals(expected)
            : "Expected:\n" + expected + "\nGot:\n" + result;
        System.out.println("  test_diamond_3................... PASS");
    }

    static void testDiamondNoTrailingNewline() {
        String result = solveDiamond(3);
        assert !result.endsWith("\n")
            : "Should not end with a trailing newline";
        System.out.println("  test_diamond_no_trailing_nl...... PASS");
    }

    static void testDiamondNoTrailingSpaces() {
        String result = solveDiamond(3);
        for (String line : result.split("\n")) {
            assert line.equals(line.stripTrailing())
                : "Line has trailing spaces: '" + line + "'";
        }
        System.out.println("  test_diamond_no_trailing_spaces.. PASS");
    }

    // ── Challenge 02: Prime Check ─────────────────────────────────

    static void testPrime2() {
        assert solvePrimeCheck(2) == true
            : "2 should be prime";
        System.out.println("  test_prime_2..................... PASS");
    }

    static void testPrime3() {
        assert solvePrimeCheck(3) == true
            : "3 should be prime";
        System.out.println("  test_prime_3..................... PASS");
    }

    static void testPrime4() {
        assert solvePrimeCheck(4) == false
            : "4 should not be prime";
        System.out.println("  test_prime_4..................... PASS");
    }

    static void testPrime1() {
        assert solvePrimeCheck(1) == false
            : "1 should not be prime";
        System.out.println("  test_prime_1..................... PASS");
    }

    static void testPrime0() {
        assert solvePrimeCheck(0) == false
            : "0 should not be prime";
        System.out.println("  test_prime_0..................... PASS");
    }

    static void testPrime17() {
        assert solvePrimeCheck(17) == true
            : "17 should be prime";
        System.out.println("  test_prime_17.................... PASS");
    }

    static void testPrime25() {
        assert solvePrimeCheck(25) == false
            : "25 should not be prime (5*5)";
        System.out.println("  test_prime_25.................... PASS");
    }

    static void testPrime97() {
        assert solvePrimeCheck(97) == true
            : "97 should be prime";
        System.out.println("  test_prime_97.................... PASS");
    }

    static void testPrimeNegative() {
        assert solvePrimeCheck(-5) == false
            : "-5 should not be prime";
        System.out.println("  test_prime_negative.............. PASS");
    }

    // ── Challenge 03: Collatz ─────────────────────────────────────

    static void testCollatz6() {
        List<Integer> expected = Arrays.asList(6, 3, 10, 5, 16, 8, 4, 2, 1);
        assert solveCollatz(6).equals(expected)
            : "Expected " + expected + ", got " + solveCollatz(6);
        System.out.println("  test_collatz_6................... PASS");
    }

    static void testCollatz1() {
        assert solveCollatz(1).equals(Arrays.asList(1))
            : "Expected [1]";
        System.out.println("  test_collatz_1................... PASS");
    }

    static void testCollatz2() {
        assert solveCollatz(2).equals(Arrays.asList(2, 1))
            : "Expected [2, 1]";
        System.out.println("  test_collatz_2................... PASS");
    }

    static void testCollatzEndsAt1() {
        List<Integer> result = solveCollatz(27);
        assert result.get(result.size() - 1) == 1
            : "Collatz sequence should always end at 1";
        System.out.println("  test_collatz_ends_at_1........... PASS");
    }

    static void testCollatzStartsAtN() {
        assert solveCollatz(42).get(0) == 42
            : "Collatz sequence should start at n";
        System.out.println("  test_collatz_starts_at_n......... PASS");
    }

    // ── Runner ──────────────────────────────────────────────────────

    public static void main(String[] args) {

        System.out.println("=== Warmup 01: Even or Odd ===");
        testEvenOddEven();
        testEvenOddOdd();
        testEvenOddZero();
        testEvenOddNegative();
        testEvenOddOne();
        System.out.println();

        System.out.println("=== Warmup 02: Absolute Value ===");
        testAbsPositive();
        testAbsNegative();
        testAbsZero();
        testAbsLargeNeg();
        testAbsOne();
        System.out.println();

        System.out.println("=== Warmup 03: Largest of Three ===");
        testLargestAscending();
        testLargestDescending();
        testLargestAllEqual();
        testLargestNegatives();
        testLargestTied();
        System.out.println();

        System.out.println("=== Warmup 04: Count Down ===");
        testCountDown5();
        testCountDown1();
        testCountDown3();
        System.out.println();

        System.out.println("=== Warmup 05: Sum 1 to N ===");
        testSum5();
        testSum1();
        testSum10();
        testSum100();
        testSum0();
        System.out.println();

        System.out.println("=== Warmup 06: Multiplication Table ===");
        testMultTableFirst();
        testMultTableLast();
        testMultTableSize();
        testMultTableMiddle();
        System.out.println();

        System.out.println("=== Practice 01: FizzBuzz ===");
        testFizzbuzz15();
        testFizzbuzzFizz();
        testFizzbuzzBuzz();
        testFizzbuzzNumber();
        testFizzbuzzSize();
        System.out.println();

        System.out.println("=== Practice 02: Digit Count ===");
        testDigitCount5Digits();
        testDigitCountZero();
        testDigitCountSingle();
        testDigitCountNegative();
        testDigitCountMillion();
        System.out.println();

        System.out.println("=== Practice 03: Reverse Number ===");
        testReverse1234();
        testReverseTrailingZeros();
        testReverseSingleDigit();
        testReverseNegative();
        testReverseZero();
        System.out.println();

        System.out.println("=== Practice 04: Right-Aligned Triangle ===");
        testTriangle1();
        testTriangle3();
        testTriangle4();
        testTriangleNoTrailingNewline();
        System.out.println();

        System.out.println("=== Challenge 01: Diamond ===");
        testDiamond1();
        testDiamond2();
        testDiamond3();
        testDiamondNoTrailingNewline();
        testDiamondNoTrailingSpaces();
        System.out.println();

        System.out.println("=== Challenge 02: Prime Check ===");
        testPrime2();
        testPrime3();
        testPrime4();
        testPrime1();
        testPrime0();
        testPrime17();
        testPrime25();
        testPrime97();
        testPrimeNegative();
        System.out.println();

        System.out.println("=== Challenge 03: Collatz ===");
        testCollatz6();
        testCollatz1();
        testCollatz2();
        testCollatzEndsAt1();
        testCollatzStartsAtN();
        System.out.println();

        System.out.println("All Chapter 3 tests passed!");
    }
}
