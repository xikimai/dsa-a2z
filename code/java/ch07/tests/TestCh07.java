package ch07.tests;

import java.util.*;

/**
 * Tests for Chapter 7: Number Wizardry — Math for Programmers
 *
 * Build and run:
 *   cd code/java
 *   javac ch07/tests/TestCh07.java
 *   java -ea ch07.tests.TestCh07
 */
public class TestCh07 {

    // ── Helper methods ───────────────────────────────────────────────

    static void assertEquals(Object expected, Object actual, String msg) {
        assert Objects.equals(expected, actual)
            : msg + " — expected " + expected + ", got " + actual;
    }

    static void assertArrayEquals(long[] expected, long[] actual, String msg) {
        assert Arrays.equals(expected, actual)
            : msg + " — expected " + Arrays.toString(expected)
              + ", got " + Arrays.toString(actual);
    }

    static void assertListEquals(List<?> expected, List<?> actual, String msg) {
        assert expected.equals(actual)
            : msg + " — expected " + expected + ", got " + actual;
    }

    // ── Reference solutions ─────────────────────────────────────────

    // W1: Count Digits
    static int solveCountDigits(long n) {
        n = Math.abs(n);
        if (n == 0) return 1;
        int count = 0;
        while (n > 0) { count++; n /= 10; }
        return count;
    }

    // W2: Reverse Number
    static long solveReverseNumber(long n) {
        long sign = n < 0 ? -1 : 1;
        n = Math.abs(n);
        long reversed = 0;
        while (n > 0) {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }
        return sign * reversed;
    }

    // W3: Sum of Digits
    static int solveSumOfDigits(long n) {
        n = Math.abs(n);
        int sum = 0;
        while (n > 0) { sum += (int)(n % 10); n /= 10; }
        return sum;
    }

    // W4: Palindrome Number
    static boolean solvePalindrome(long n) {
        if (n < 0) return false;
        long original = n;
        long reversed = 0;
        while (n > 0) {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }
        return original == reversed;
    }

    // W5: Armstrong Number
    static boolean solveArmstrong(long n) {
        if (n < 0) return false;
        int numDigits = String.valueOf(n).length();
        long temp = n, sum = 0;
        while (temp > 0) {
            long d = temp % 10;
            sum += (long) Math.pow(d, numDigits);
            temp /= 10;
        }
        return sum == n;
    }

    // P1: All Divisors
    static List<Integer> solveAllDivisors(int n) {
        List<Integer> divs = new ArrayList<>();
        for (int i = 1; (long)i * i <= n; i++) {
            if (n % i == 0) {
                divs.add(i);
                if (i != n / i) divs.add(n / i);
            }
        }
        Collections.sort(divs);
        return divs;
    }

    // P2: GCD and LCM
    static long gcdHelper(long a, long b) {
        while (b != 0) { long t = b; b = a % b; a = t; }
        return a;
    }

    static long[] solveGcdLcm(long a, long b) {
        long g = gcdHelper(a, b);
        long lcm = (g == 0) ? 0 : a / g * b;
        return new long[]{g, lcm};
    }

    // P3: Modular Exponentiation
    static long solveModExp(long base, long exp, long mod) {
        long result = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) result = result * base % mod;
            exp /= 2;
            base = base * base % mod;
        }
        return result;
    }

    // P4: Prime Factorization
    static List<int[]> solvePrimeFactors(long n) {
        List<int[]> factors = new ArrayList<>();
        for (long d = 2; d * d <= n; d++) {
            if (n % d == 0) {
                int count = 0;
                while (n % d == 0) { count++; n /= d; }
                factors.add(new int[]{(int)d, count});
            }
        }
        if (n > 1) factors.add(new int[]{(int)n, 1});
        return factors;
    }

    // P5: Trailing Zeros
    static int solveTrailingZeros(int n) {
        int count = 0;
        long p = 5;
        while (p <= n) { count += (int)(n / p); p *= 5; }
        return count;
    }

    // C1: GCD Three Ways
    static long solveGcdSubtract(long a, long b) {
        if (a == 0) return b;
        if (b == 0) return a;
        while (a != b) {
            if (a > b) a -= b; else b -= a;
        }
        return a;
    }

    static long solveGcdEuclidean(long a, long b) {
        while (b != 0) { long t = b; b = a % b; a = t; }
        return a;
    }

    static long[] solveGcdExtended(long a, long b) {
        if (b == 0) return new long[]{a, 1, 0};
        long[] r = solveGcdExtended(b, a % b);
        long x = r[2];
        long y = r[1] - (a / b) * r[2];
        return new long[]{r[0], x, y};
    }

    // C2: Sieve
    static List<Integer> solveSieve(int n) {
        List<Integer> primes = new ArrayList<>();
        if (n < 2) return primes;
        boolean[] isP = new boolean[n + 1];
        Arrays.fill(isP, true);
        isP[0] = isP[1] = false;
        for (int i = 2; (long)i * i <= n; i++) {
            if (isP[i]) {
                for (int j = i * i; j <= n; j += i) isP[j] = false;
            }
        }
        for (int i = 2; i <= n; i++) if (isP[i]) primes.add(i);
        return primes;
    }

    // C3: GCD Pair Sum
    static long solveGcdPairSum(int[] nums) {
        long total = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                total += gcdHelper(nums[i], nums[j]);
            }
        }
        return total;
    }

    // ── Warmup 01: Count Digits ──────────────────────────────────────

    static void testCountDigits5() {
        assertEquals(5, solveCountDigits(12345), "count digits 12345");
        System.out.println("  test_count_digits_5.............. PASS");
    }
    static void testCountDigitsZero() {
        assertEquals(1, solveCountDigits(0), "count digits 0");
        System.out.println("  test_count_digits_zero........... PASS");
    }
    static void testCountDigitsNeg() {
        assertEquals(2, solveCountDigits(-42), "count digits -42");
        System.out.println("  test_count_digits_negative....... PASS");
    }
    static void testCountDigitsSingle() {
        assertEquals(1, solveCountDigits(7), "count digits 7");
        System.out.println("  test_count_digits_single......... PASS");
    }
    static void testCountDigitsTen() {
        assertEquals(10, solveCountDigits(1000000000L), "count digits 10^9");
        System.out.println("  test_count_digits_ten............ PASS");
    }

    // ── Warmup 02: Reverse Number ────────────────────────────────────

    static void testReverseBasic() {
        assertEquals(54321L, solveReverseNumber(12345), "reverse 12345");
        System.out.println("  test_reverse_basic............... PASS");
    }
    static void testReverseNeg() {
        assertEquals(-321L, solveReverseNumber(-123), "reverse -123");
        System.out.println("  test_reverse_negative............ PASS");
    }
    static void testReverseTrailing() {
        assertEquals(21L, solveReverseNumber(1200), "reverse 1200");
        System.out.println("  test_reverse_trailing............ PASS");
    }
    static void testReverseZero() {
        assertEquals(0L, solveReverseNumber(0), "reverse 0");
        System.out.println("  test_reverse_zero................ PASS");
    }

    // ── Warmup 03: Sum of Digits ─────────────────────────────────────

    static void testSumDigitsBasic() {
        assertEquals(15, solveSumOfDigits(12345), "sum digits 12345");
        System.out.println("  test_sum_digits_basic............ PASS");
    }
    static void testSumDigitsZero() {
        assertEquals(0, solveSumOfDigits(0), "sum digits 0");
        System.out.println("  test_sum_digits_zero............. PASS");
    }
    static void testSumDigitsNeg() {
        assertEquals(15, solveSumOfDigits(-456), "sum digits -456");
        System.out.println("  test_sum_digits_negative......... PASS");
    }
    static void testSumDigitsNines() {
        assertEquals(27, solveSumOfDigits(999), "sum digits 999");
        System.out.println("  test_sum_digits_nines............ PASS");
    }

    // ── Warmup 04: Palindrome ────────────────────────────────────────

    static void testPalindrome121() {
        assertEquals(true, solvePalindrome(121), "palindrome 121");
        System.out.println("  test_palindrome_121.............. PASS");
    }
    static void testPalindromeNeg() {
        assertEquals(false, solvePalindrome(-121), "palindrome -121");
        System.out.println("  test_palindrome_negative......... PASS");
    }
    static void testPalindrome10() {
        assertEquals(false, solvePalindrome(10), "palindrome 10");
        System.out.println("  test_palindrome_10............... PASS");
    }
    static void testPalindromeZero() {
        assertEquals(true, solvePalindrome(0), "palindrome 0");
        System.out.println("  test_palindrome_zero............. PASS");
    }
    static void testPalindrome1001() {
        assertEquals(true, solvePalindrome(1001), "palindrome 1001");
        System.out.println("  test_palindrome_1001............. PASS");
    }

    // ── Warmup 05: Armstrong ─────────────────────────────────────────

    static void testArmstrong153() {
        assertEquals(true, solveArmstrong(153), "armstrong 153");
        System.out.println("  test_armstrong_153................ PASS");
    }
    static void testArmstrong370() {
        assertEquals(true, solveArmstrong(370), "armstrong 370");
        System.out.println("  test_armstrong_370................ PASS");
    }
    static void testArmstrong9474() {
        assertEquals(true, solveArmstrong(9474), "armstrong 9474");
        System.out.println("  test_armstrong_9474............... PASS");
    }
    static void testArmstrong100() {
        assertEquals(false, solveArmstrong(100), "armstrong 100");
        System.out.println("  test_armstrong_100................ PASS");
    }
    static void testArmstrong1() {
        assertEquals(true, solveArmstrong(1), "armstrong 1");
        System.out.println("  test_armstrong_1.................. PASS");
    }
    static void testArmstrong0() {
        assertEquals(true, solveArmstrong(0), "armstrong 0");
        System.out.println("  test_armstrong_0.................. PASS");
    }

    // ── Practice 01: All Divisors ────────────────────────────────────

    static void testDivisors36() {
        assertListEquals(Arrays.asList(1,2,3,4,6,9,12,18,36), solveAllDivisors(36), "divisors 36");
        System.out.println("  test_divisors_36................. PASS");
    }
    static void testDivisors1() {
        assertListEquals(Arrays.asList(1), solveAllDivisors(1), "divisors 1");
        System.out.println("  test_divisors_1.................. PASS");
    }
    static void testDivisors7() {
        assertListEquals(Arrays.asList(1,7), solveAllDivisors(7), "divisors 7");
        System.out.println("  test_divisors_7.................. PASS");
    }
    static void testDivisors12() {
        assertListEquals(Arrays.asList(1,2,3,4,6,12), solveAllDivisors(12), "divisors 12");
        System.out.println("  test_divisors_12................. PASS");
    }

    // ── Practice 02: GCD and LCM ────────────────────────────────────

    static void testGcdLcm12_18() {
        assertArrayEquals(new long[]{6, 36}, solveGcdLcm(12, 18), "gcd/lcm 12,18");
        System.out.println("  test_gcd_lcm_12_18............... PASS");
    }
    static void testGcdLcm7_13() {
        assertArrayEquals(new long[]{1, 91}, solveGcdLcm(7, 13), "gcd/lcm 7,13");
        System.out.println("  test_gcd_lcm_7_13................ PASS");
    }
    static void testGcdLcm0_5() {
        assertArrayEquals(new long[]{5, 0}, solveGcdLcm(0, 5), "gcd/lcm 0,5");
        System.out.println("  test_gcd_lcm_0_5................. PASS");
    }
    static void testGcdLcm100_75() {
        assertArrayEquals(new long[]{25, 300}, solveGcdLcm(100, 75), "gcd/lcm 100,75");
        System.out.println("  test_gcd_lcm_100_75.............. PASS");
    }

    // ── Practice 03: Mod Exponentiation ──────────────────────────────

    static void testModExpSmall() {
        assertEquals(1024L, solveModExp(2, 10, 1000000007), "2^10 mod 10^9+7");
        System.out.println("  test_mod_exp_small............... PASS");
    }
    static void testModExpMedium() {
        assertEquals(1048576L, solveModExp(2, 20, 1000000007), "2^20 mod 10^9+7");
        System.out.println("  test_mod_exp_medium.............. PASS");
    }
    static void testModExpZero() {
        assertEquals(1L, solveModExp(123456789, 0, 1000000007), "x^0 mod m");
        System.out.println("  test_mod_exp_zero................ PASS");
    }
    static void testModExpLarge() {
        assertEquals(976371285L, solveModExp(2, 100, 1000000007), "2^100 mod 10^9+7");
        System.out.println("  test_mod_exp_large............... PASS");
    }

    // ── Practice 04: Prime Factorization ─────────────────────────────

    static void testFactors12() {
        List<int[]> result = solvePrimeFactors(12);
        assert result.size() == 2 : "12 should have 2 prime factors";
        assert result.get(0)[0] == 2 && result.get(0)[1] == 2 : "12: 2^2";
        assert result.get(1)[0] == 3 && result.get(1)[1] == 1 : "12: 3^1";
        System.out.println("  test_factors_12.................. PASS");
    }
    static void testFactors1() {
        assert solvePrimeFactors(1).isEmpty() : "1 has no prime factors";
        System.out.println("  test_factors_1................... PASS");
    }
    static void testFactors7() {
        List<int[]> result = solvePrimeFactors(7);
        assert result.size() == 1 && result.get(0)[0] == 7 && result.get(0)[1] == 1
            : "7 is prime";
        System.out.println("  test_factors_7................... PASS");
    }
    static void testFactors360() {
        List<int[]> result = solvePrimeFactors(360);
        assert result.size() == 3 : "360 = 2^3 * 3^2 * 5^1";
        assert result.get(0)[0] == 2 && result.get(0)[1] == 3 : "360: 2^3";
        assert result.get(1)[0] == 3 && result.get(1)[1] == 2 : "360: 3^2";
        assert result.get(2)[0] == 5 && result.get(2)[1] == 1 : "360: 5^1";
        System.out.println("  test_factors_360................. PASS");
    }

    // ── Practice 05: Trailing Zeros ──────────────────────────────────

    static void testTrailingZeros5() {
        assertEquals(1, solveTrailingZeros(5), "trailing zeros 5!");
        System.out.println("  test_trailing_zeros_5............ PASS");
    }
    static void testTrailingZeros10() {
        assertEquals(2, solveTrailingZeros(10), "trailing zeros 10!");
        System.out.println("  test_trailing_zeros_10........... PASS");
    }
    static void testTrailingZeros25() {
        assertEquals(6, solveTrailingZeros(25), "trailing zeros 25!");
        System.out.println("  test_trailing_zeros_25........... PASS");
    }
    static void testTrailingZeros100() {
        assertEquals(24, solveTrailingZeros(100), "trailing zeros 100!");
        System.out.println("  test_trailing_zeros_100.......... PASS");
    }
    static void testTrailingZeros0() {
        assertEquals(0, solveTrailingZeros(0), "trailing zeros 0!");
        System.out.println("  test_trailing_zeros_0............ PASS");
    }

    // ── Challenge 01: GCD Three Ways ─────────────────────────────────

    static void testGcdSubtract() {
        assertEquals(6L, solveGcdSubtract(48, 18), "subtract 48,18");
        assertEquals(1L, solveGcdSubtract(7, 13), "subtract 7,13");
        assertEquals(10L, solveGcdSubtract(10, 10), "subtract 10,10");
        System.out.println("  test_gcd_subtract................ PASS");
    }
    static void testGcdEuclidean() {
        assertEquals(6L, solveGcdEuclidean(48, 18), "euclidean 48,18");
        assertEquals(1L, solveGcdEuclidean(7, 13), "euclidean 7,13");
        assertEquals(5L, solveGcdEuclidean(0, 5), "euclidean 0,5");
        assertEquals(1L, solveGcdEuclidean(1000000000L, 999999999L), "euclidean large");
        System.out.println("  test_gcd_euclidean............... PASS");
    }
    static void testGcdExtended() {
        long[] r1 = solveGcdExtended(35, 15);
        assertEquals(5L, r1[0], "ext gcd(35,15) gcd");
        assert 35 * r1[1] + 15 * r1[2] == 5 : "ext gcd(35,15) Bezout";

        long[] r2 = solveGcdExtended(7, 11);
        assertEquals(1L, r2[0], "ext gcd(7,11) gcd");
        assert 7 * r2[1] + 11 * r2[2] == 1 : "ext gcd(7,11) Bezout";

        long[] r3 = solveGcdExtended(6, 6);
        assertEquals(6L, r3[0], "ext gcd(6,6) gcd");
        assert 6 * r3[1] + 6 * r3[2] == 6 : "ext gcd(6,6) Bezout";
        System.out.println("  test_gcd_extended................ PASS");
    }

    // ── Challenge 02: Sieve ──────────────────────────────────────────

    static void testSieve10() {
        assertListEquals(Arrays.asList(2,3,5,7), solveSieve(10), "sieve 10");
        System.out.println("  test_sieve_10.................... PASS");
    }
    static void testSieve1() {
        assertListEquals(Collections.emptyList(), solveSieve(1), "sieve 1");
        System.out.println("  test_sieve_1..................... PASS");
    }
    static void testSieve2() {
        assertListEquals(Arrays.asList(2), solveSieve(2), "sieve 2");
        System.out.println("  test_sieve_2..................... PASS");
    }
    static void testSieve30() {
        assertListEquals(
            Arrays.asList(2,3,5,7,11,13,17,19,23,29), solveSieve(30), "sieve 30");
        System.out.println("  test_sieve_30.................... PASS");
    }

    // ── Challenge 03: GCD Pair Sum ───────────────────────────────────

    static void testGcdPairBasic() {
        assertEquals(6L, solveGcdPairSum(new int[]{2, 4, 6}), "gcd pair [2,4,6]");
        System.out.println("  test_gcd_pair_basic.............. PASS");
    }
    static void testGcdPairThrees() {
        assertEquals(9L, solveGcdPairSum(new int[]{3, 6, 9}), "gcd pair [3,6,9]");
        System.out.println("  test_gcd_pair_threes............. PASS");
    }
    static void testGcdPairLarger() {
        assertEquals(24L, solveGcdPairSum(new int[]{12, 18, 24}), "gcd pair [12,18,24]");
        System.out.println("  test_gcd_pair_larger............. PASS");
    }
    static void testGcdPairSingle() {
        assertEquals(0L, solveGcdPairSum(new int[]{7}), "gcd pair single");
        System.out.println("  test_gcd_pair_single............. PASS");
    }
    static void testGcdPairCoprimes() {
        assertEquals(6L, solveGcdPairSum(new int[]{2, 3, 5, 7}), "gcd pair coprimes");
        System.out.println("  test_gcd_pair_coprimes........... PASS");
    }

    // ── Runner ───────────────────────────────────────────────────────

    public static void main(String[] args) {

        System.out.println("Testing Chapter 7...\n");

        System.out.println("--- Warmup Problems ---");

        System.out.println("=== Warmup 01: Count Digits ===");
        testCountDigits5();
        testCountDigitsZero();
        testCountDigitsNeg();
        testCountDigitsSingle();
        testCountDigitsTen();
        System.out.println();

        System.out.println("=== Warmup 02: Reverse Number ===");
        testReverseBasic();
        testReverseNeg();
        testReverseTrailing();
        testReverseZero();
        System.out.println();

        System.out.println("=== Warmup 03: Sum of Digits ===");
        testSumDigitsBasic();
        testSumDigitsZero();
        testSumDigitsNeg();
        testSumDigitsNines();
        System.out.println();

        System.out.println("=== Warmup 04: Palindrome ===");
        testPalindrome121();
        testPalindromeNeg();
        testPalindrome10();
        testPalindromeZero();
        testPalindrome1001();
        System.out.println();

        System.out.println("=== Warmup 05: Armstrong ===");
        testArmstrong153();
        testArmstrong370();
        testArmstrong9474();
        testArmstrong100();
        testArmstrong1();
        testArmstrong0();
        System.out.println();

        System.out.println("--- Practice Problems ---");

        System.out.println("=== Practice 01: All Divisors ===");
        testDivisors36();
        testDivisors1();
        testDivisors7();
        testDivisors12();
        System.out.println();

        System.out.println("=== Practice 02: GCD and LCM ===");
        testGcdLcm12_18();
        testGcdLcm7_13();
        testGcdLcm0_5();
        testGcdLcm100_75();
        System.out.println();

        System.out.println("=== Practice 03: Mod Exponentiation ===");
        testModExpSmall();
        testModExpMedium();
        testModExpZero();
        testModExpLarge();
        System.out.println();

        System.out.println("=== Practice 04: Prime Factorization ===");
        testFactors12();
        testFactors1();
        testFactors7();
        testFactors360();
        System.out.println();

        System.out.println("=== Practice 05: Trailing Zeros ===");
        testTrailingZeros5();
        testTrailingZeros10();
        testTrailingZeros25();
        testTrailingZeros100();
        testTrailingZeros0();
        System.out.println();

        System.out.println("--- Challenge Problems ---");

        System.out.println("=== Challenge 01: GCD Three Ways ===");
        testGcdSubtract();
        testGcdEuclidean();
        testGcdExtended();
        System.out.println();

        System.out.println("=== Challenge 02: Sieve ===");
        testSieve10();
        testSieve1();
        testSieve2();
        testSieve30();
        System.out.println();

        System.out.println("=== Challenge 03: GCD Pair Sum ===");
        testGcdPairBasic();
        testGcdPairThrees();
        testGcdPairLarger();
        testGcdPairSingle();
        testGcdPairCoprimes();
        System.out.println();

        System.out.println("All tests passed!");
    }
}
