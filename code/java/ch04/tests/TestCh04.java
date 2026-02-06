package ch04.tests;

import java.util.*;

/**
 * Tests for Chapter 4: Functions
 * ===============================
 * Chapter 4: Functions
 *
 * This file tests every solve() method from Chapter 4 using the reference
 * solutions. We define each solve() here so the test is self-contained.
 *
 * Build and run:
 *   cd code/java
 *   javac ch04/tests/TestCh04.java
 *   java -ea ch04.tests.TestCh04
 *
 * The -ea flag enables assertions. Without it, assert statements are ignored!
 */
public class TestCh04 {

    // ── Reference solutions ─────────────────────────────────────────

    static String solveGreeting(String name) {
        return "Hello, " + name + "!";
    }

    static long solvePower(int base, int exponent) {
        long result = 1;
        for (int i = 0; i < exponent; i++) {
            result *= base;
        }
        return result;
    }

    static int minOfTwo(int a, int b) {
        if (a <= b) return a;
        return b;
    }

    static int solveMinOfThree(int a, int b, int c) {
        return minOfTwo(a, minOfTwo(b, c));
    }

    static String solveRepeatString(String s, int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(s);
        }
        return sb.toString();
    }

    static String solveRepeatStringDefault(String s) {
        return solveRepeatString(s, 3);
    }

    static int[] solveDoubleList(int[] nums) {
        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[i] = nums[i] * 2;
        }
        return result;
    }

    static Integer solveCalculator(int a, String op, int b) {
        switch (op) {
            case "+": return a + b;
            case "-": return a - b;
            case "*": return a * b;
            case "/":
                if (b == 0) return null;
                return a / b;
            default: return null;
        }
    }

    static boolean hasDigit(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (Character.isDigit(s.charAt(i))) return true;
        }
        return false;
    }

    static boolean hasUpper(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (Character.isUpperCase(s.charAt(i))) return true;
        }
        return false;
    }

    static String solvePasswordStrength(String password) {
        if (password.length() < 8) return "weak";
        boolean digit = hasDigit(password);
        boolean upper = hasUpper(password);
        if (digit && upper) return "strong";
        if (digit || upper) return "medium";
        return "weak";
    }

    static double cToF(double c) { return c * 9.0 / 5.0 + 32.0; }
    static double fToC(double f) { return (f - 32.0) * 5.0 / 9.0; }
    static double cToK(double c) { return c + 273.15; }
    static double kToC(double k) { return k - 273.15; }

    static double solveTemperature(double value, String from, String to) {
        if (from.equals(to)) return -1.0;
        if (from.equals("C") && to.equals("F")) return cToF(value);
        if (from.equals("F") && to.equals("C")) return fToC(value);
        if (from.equals("C") && to.equals("K")) return cToK(value);
        if (from.equals("K") && to.equals("C")) return kToC(value);
        if (from.equals("F") && to.equals("K")) return cToK(fToC(value));
        if (from.equals("K") && to.equals("F")) return cToF(kToC(value));
        return -1.0;
    }

    static double[] solveStats(int[] nums) {
        int min = nums[0], max = nums[0];
        long sum = 0;
        for (int n : nums) {
            if (n < min) min = n;
            if (n > max) max = n;
            sum += n;
        }
        double avg = (double) sum / nums.length;
        avg = Math.round(avg * 100.0) / 100.0;
        return new double[]{min, max, avg};
    }

    static boolean solvePrimeCheck(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    static List<Integer> solveApplyOperations(List<Integer> nums, List<String> operations) {
        List<Integer> result = new ArrayList<>(nums);
        for (String op : operations) {
            switch (op) {
                case "double":
                    for (int i = 0; i < result.size(); i++)
                        result.set(i, result.get(i) * 2);
                    break;
                case "negate":
                    for (int i = 0; i < result.size(); i++)
                        result.set(i, result.get(i) * -1);
                    break;
                case "sort":
                    Collections.sort(result);
                    break;
                case "reverse":
                    Collections.reverse(result);
                    break;
                case "square":
                    for (int i = 0; i < result.size(); i++)
                        result.set(i, result.get(i) * result.get(i));
                    break;
            }
        }
        return result;
    }

    // ── Warmup 01: Greeting ─────────────────────────────────────────

    static void testGreetingNormal() {
        assert solveGreeting("Maya").equals("Hello, Maya!")
            : "Expected 'Hello, Maya!'";
        System.out.println("  test_greeting_normal............. PASS");
    }

    static void testGreetingWorld() {
        assert solveGreeting("World").equals("Hello, World!")
            : "Expected 'Hello, World!'";
        System.out.println("  test_greeting_world.............. PASS");
    }

    static void testGreetingSingleChar() {
        assert solveGreeting("A").equals("Hello, A!")
            : "Expected 'Hello, A!'";
        System.out.println("  test_greeting_single_char........ PASS");
    }

    static void testGreetingLongName() {
        assert solveGreeting("Alexandra").equals("Hello, Alexandra!")
            : "Expected 'Hello, Alexandra!'";
        System.out.println("  test_greeting_long_name.......... PASS");
    }

    // ── Warmup 02: Power ────────────────────────────────────────────

    static void testPowerBasic() {
        assert solvePower(2, 10) == 1024
            : "Expected 1024, got " + solvePower(2, 10);
        System.out.println("  test_power_basic................. PASS");
    }

    static void testPowerZeroExponent() {
        assert solvePower(5, 0) == 1
            : "Expected 1, got " + solvePower(5, 0);
        System.out.println("  test_power_zero_exponent......... PASS");
    }

    static void testPowerOne() {
        assert solvePower(7, 1) == 7
            : "Expected 7, got " + solvePower(7, 1);
        System.out.println("  test_power_one................... PASS");
    }

    static void testPowerBaseOne() {
        assert solvePower(1, 100) == 1
            : "Expected 1";
        System.out.println("  test_power_base_one.............. PASS");
    }

    static void testPowerThreeFour() {
        assert solvePower(3, 4) == 81
            : "Expected 81, got " + solvePower(3, 4);
        System.out.println("  test_power_three_four............ PASS");
    }

    static void testPowerBaseZero() {
        assert solvePower(0, 5) == 0
            : "Expected 0";
        System.out.println("  test_power_base_zero............. PASS");
    }

    // ── Warmup 03: Min of Three ─────────────────────────────────────

    static void testMinBasic() {
        assert solveMinOfThree(3, 1, 2) == 1
            : "Expected 1";
        System.out.println("  test_min_basic................... PASS");
    }

    static void testMinAllEqual() {
        assert solveMinOfThree(7, 7, 7) == 7
            : "Expected 7";
        System.out.println("  test_min_all_equal............... PASS");
    }

    static void testMinNegatives() {
        assert solveMinOfThree(-5, -2, -8) == -8
            : "Expected -8";
        System.out.println("  test_min_negatives............... PASS");
    }

    static void testMinFirstSmallest() {
        assert solveMinOfThree(1, 5, 9) == 1
            : "Expected 1";
        System.out.println("  test_min_first_smallest.......... PASS");
    }

    static void testMinLastSmallest() {
        assert solveMinOfThree(9, 5, 1) == 1
            : "Expected 1";
        System.out.println("  test_min_last_smallest........... PASS");
    }

    // ── Warmup 04: Repeat String ────────────────────────────────────

    static void testRepeatBasic() {
        assert solveRepeatString("ha", 3).equals("hahaha")
            : "Expected 'hahaha'";
        System.out.println("  test_repeat_basic................ PASS");
    }

    static void testRepeatZero() {
        assert solveRepeatString("xyz", 0).equals("")
            : "Expected empty string";
        System.out.println("  test_repeat_zero................. PASS");
    }

    static void testRepeatOne() {
        assert solveRepeatString("hello", 1).equals("hello")
            : "Expected 'hello'";
        System.out.println("  test_repeat_one.................. PASS");
    }

    static void testRepeatFive() {
        assert solveRepeatString("ab", 5).equals("ababababab")
            : "Expected 'ababababab'";
        System.out.println("  test_repeat_five................. PASS");
    }

    static void testRepeatDefault() {
        assert solveRepeatStringDefault("go").equals("gogogo")
            : "Expected 'gogogo'";
        System.out.println("  test_repeat_default.............. PASS");
    }

    static void testRepeatDefaultSingle() {
        assert solveRepeatStringDefault("!").equals("!!!")
            : "Expected '!!!'";
        System.out.println("  test_repeat_default_single....... PASS");
    }

    // ── Warmup 05: Double List ──────────────────────────────────────

    static void testDoubleBasic() {
        assert Arrays.equals(solveDoubleList(new int[]{1, 2, 3, 4, 5}), new int[]{2, 4, 6, 8, 10})
            : "Expected [2, 4, 6, 8, 10]";
        System.out.println("  test_double_basic................ PASS");
    }

    static void testDoubleNegatives() {
        assert Arrays.equals(solveDoubleList(new int[]{-1, 0, 7}), new int[]{-2, 0, 14})
            : "Expected [-2, 0, 14]";
        System.out.println("  test_double_negatives............ PASS");
    }

    static void testDoubleSingle() {
        assert Arrays.equals(solveDoubleList(new int[]{42}), new int[]{84})
            : "Expected [84]";
        System.out.println("  test_double_single............... PASS");
    }

    static void testDoubleZeros() {
        assert Arrays.equals(solveDoubleList(new int[]{0, 0, 0}), new int[]{0, 0, 0})
            : "Expected [0, 0, 0]";
        System.out.println("  test_double_zeros................ PASS");
    }

    // ── Practice 01: Calculator ─────────────────────────────────────

    static void testCalcAdd() {
        assert solveCalculator(10, "+", 3).equals(13)
            : "Expected 13";
        System.out.println("  test_calc_add.................... PASS");
    }

    static void testCalcSubtract() {
        assert solveCalculator(10, "-", 3).equals(7)
            : "Expected 7";
        System.out.println("  test_calc_subtract............... PASS");
    }

    static void testCalcMultiply() {
        assert solveCalculator(10, "*", 3).equals(30)
            : "Expected 30";
        System.out.println("  test_calc_multiply............... PASS");
    }

    static void testCalcDivide() {
        assert solveCalculator(10, "/", 3).equals(3)
            : "Expected 3 (integer division)";
        System.out.println("  test_calc_divide................. PASS");
    }

    static void testCalcDivideByZero() {
        assert solveCalculator(10, "/", 0) == null
            : "Expected null for divide-by-zero";
        System.out.println("  test_calc_divide_by_zero......... PASS");
    }

    static void testCalcInvalidOp() {
        assert solveCalculator(10, "%", 3) == null
            : "Expected null for invalid operator";
        System.out.println("  test_calc_invalid_op............. PASS");
    }

    // ── Practice 02: Password Strength ──────────────────────────────

    static void testPasswordShort() {
        assert solvePasswordStrength("abc").equals("weak")
            : "Expected 'weak' for short password";
        System.out.println("  test_password_short.............. PASS");
    }

    static void testPasswordLongNoSpecial() {
        assert solvePasswordStrength("abcdefgh").equals("weak")
            : "Expected 'weak' for long but no digit/upper";
        System.out.println("  test_password_long_no_special.... PASS");
    }

    static void testPasswordWithDigit() {
        assert solvePasswordStrength("abcdefg1").equals("medium")
            : "Expected 'medium' for digit only";
        System.out.println("  test_password_with_digit......... PASS");
    }

    static void testPasswordWithUpper() {
        assert solvePasswordStrength("Abcdefgh").equals("medium")
            : "Expected 'medium' for upper only";
        System.out.println("  test_password_with_upper......... PASS");
    }

    static void testPasswordStrong() {
        assert solvePasswordStrength("Abcdefg1").equals("strong")
            : "Expected 'strong' for digit + upper";
        System.out.println("  test_password_strong............. PASS");
    }

    static void testPasswordShortWithBoth() {
        assert solvePasswordStrength("A1b").equals("weak")
            : "Expected 'weak' for short even with digit+upper";
        System.out.println("  test_password_short_with_both.... PASS");
    }

    // ── Practice 03: Temperature Conversion ─────────────────────────

    static void testTempCToF() {
        double result = solveTemperature(100.0, "C", "F");
        assert Math.abs(result - 212.0) < 0.01
            : "Expected 212.0, got " + result;
        System.out.println("  test_temp_c_to_f................. PASS");
    }

    static void testTempFToC() {
        double result = solveTemperature(32.0, "F", "C");
        assert Math.abs(result - 0.0) < 0.01
            : "Expected 0.0, got " + result;
        System.out.println("  test_temp_f_to_c................. PASS");
    }

    static void testTempCToK() {
        double result = solveTemperature(0.0, "C", "K");
        assert Math.abs(result - 273.15) < 0.01
            : "Expected 273.15, got " + result;
        System.out.println("  test_temp_c_to_k................. PASS");
    }

    static void testTempKToC() {
        double result = solveTemperature(273.15, "K", "C");
        assert Math.abs(result - 0.0) < 0.01
            : "Expected 0.0, got " + result;
        System.out.println("  test_temp_k_to_c................. PASS");
    }

    static void testTempFToK() {
        double result = solveTemperature(212.0, "F", "K");
        assert Math.abs(result - 373.15) < 0.01
            : "Expected 373.15, got " + result;
        System.out.println("  test_temp_f_to_k................. PASS");
    }

    static void testTempSameUnit() {
        double result = solveTemperature(100.0, "C", "C");
        assert result == -1.0
            : "Expected -1.0 for same-unit, got " + result;
        System.out.println("  test_temp_same_unit.............. PASS");
    }

    // ── Practice 04: Array Statistics ───────────────────────────────

    static void testStatsBasic() {
        double[] result = solveStats(new int[]{3, 1, 4, 1, 5});
        assert result[0] == 1.0 : "Expected min=1";
        assert result[1] == 5.0 : "Expected max=5";
        assert Math.abs(result[2] - 2.8) < 0.01 : "Expected avg=2.8, got " + result[2];
        System.out.println("  test_stats_basic................. PASS");
    }

    static void testStatsUniform() {
        double[] result = solveStats(new int[]{10, 20, 30});
        assert result[0] == 10.0 : "Expected min=10";
        assert result[1] == 30.0 : "Expected max=30";
        assert Math.abs(result[2] - 20.0) < 0.01 : "Expected avg=20.0";
        System.out.println("  test_stats_uniform............... PASS");
    }

    static void testStatsSingle() {
        double[] result = solveStats(new int[]{42});
        assert result[0] == 42.0 : "Expected min=42";
        assert result[1] == 42.0 : "Expected max=42";
        assert Math.abs(result[2] - 42.0) < 0.01 : "Expected avg=42.0";
        System.out.println("  test_stats_single................ PASS");
    }

    static void testStatsNegatives() {
        double[] result = solveStats(new int[]{-5, -1, -10, -3});
        assert result[0] == -10.0 : "Expected min=-10";
        assert result[1] == -1.0 : "Expected max=-1";
        assert Math.abs(result[2] - (-4.75)) < 0.01 : "Expected avg=-4.75, got " + result[2];
        System.out.println("  test_stats_negatives............. PASS");
    }

    static void testStatsRounding() {
        double[] result = solveStats(new int[]{1, 2, 3});
        assert Math.abs(result[2] - 2.0) < 0.01 : "Expected avg=2.0, got " + result[2];
        System.out.println("  test_stats_rounding.............. PASS");
    }

    // ── Challenge 01: Prime Check ───────────────────────────────────

    static void testPrime2() {
        assert solvePrimeCheck(2) == true
            : "2 should be prime";
        System.out.println("  test_prime_2..................... PASS");
    }

    static void testPrime17() {
        assert solvePrimeCheck(17) == true
            : "17 should be prime";
        System.out.println("  test_prime_17.................... PASS");
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

    static void testPrimeNegative() {
        assert solvePrimeCheck(-5) == false
            : "-5 should not be prime";
        System.out.println("  test_prime_negative.............. PASS");
    }

    static void testPrime97() {
        assert solvePrimeCheck(97) == true
            : "97 should be prime";
        System.out.println("  test_prime_97.................... PASS");
    }

    static void testPrime25() {
        assert solvePrimeCheck(25) == false
            : "25 should not be prime (5*5)";
        System.out.println("  test_prime_25.................... PASS");
    }

    // ── Challenge 02: Apply Operations ──────────────────────────────

    static void testOpsSortDouble() {
        List<Integer> result = solveApplyOperations(
            Arrays.asList(3, 1, 2), Arrays.asList("sort", "double"));
        assert result.equals(Arrays.asList(2, 4, 6))
            : "Expected [2, 4, 6], got " + result;
        System.out.println("  test_ops_sort_double............. PASS");
    }

    static void testOpsNegateSortReverse() {
        List<Integer> result = solveApplyOperations(
            Arrays.asList(5, -3, 7, 1), Arrays.asList("negate", "sort", "reverse"));
        assert result.equals(Arrays.asList(3, -1, -5, -7))
            : "Expected [3, -1, -5, -7], got " + result;
        System.out.println("  test_ops_negate_sort_reverse..... PASS");
    }

    static void testOpsSquare() {
        List<Integer> result = solveApplyOperations(
            Arrays.asList(2, -3, 4), Arrays.asList("square"));
        assert result.equals(Arrays.asList(4, 9, 16))
            : "Expected [4, 9, 16], got " + result;
        System.out.println("  test_ops_square.................. PASS");
    }

    static void testOpsEmpty() {
        List<Integer> result = solveApplyOperations(
            Arrays.asList(1, 2, 3), Collections.emptyList());
        assert result.equals(Arrays.asList(1, 2, 3))
            : "Expected [1, 2, 3] with no operations, got " + result;
        System.out.println("  test_ops_empty................... PASS");
    }

    static void testOpsUnknown() {
        List<Integer> result = solveApplyOperations(
            Arrays.asList(1, 2, 3), Arrays.asList("unknown", "double"));
        assert result.equals(Arrays.asList(2, 4, 6))
            : "Expected [2, 4, 6] (unknown ignored), got " + result;
        System.out.println("  test_ops_unknown................. PASS");
    }

    static void testOpsReverse() {
        List<Integer> result = solveApplyOperations(
            Arrays.asList(1, 2, 3, 4), Arrays.asList("reverse"));
        assert result.equals(Arrays.asList(4, 3, 2, 1))
            : "Expected [4, 3, 2, 1], got " + result;
        System.out.println("  test_ops_reverse................. PASS");
    }

    // ── Runner ──────────────────────────────────────────────────────

    public static void main(String[] args) {

        System.out.println("=== Chapter 4: Functions ===\n");

        System.out.println("--- Warmup Problems ---");

        System.out.println("=== Warmup 01: Greeting ===");
        testGreetingNormal();
        testGreetingWorld();
        testGreetingSingleChar();
        testGreetingLongName();
        System.out.println();

        System.out.println("=== Warmup 02: Power ===");
        testPowerBasic();
        testPowerZeroExponent();
        testPowerOne();
        testPowerBaseOne();
        testPowerThreeFour();
        testPowerBaseZero();
        System.out.println();

        System.out.println("=== Warmup 03: Min of Three ===");
        testMinBasic();
        testMinAllEqual();
        testMinNegatives();
        testMinFirstSmallest();
        testMinLastSmallest();
        System.out.println();

        System.out.println("=== Warmup 04: Repeat String ===");
        testRepeatBasic();
        testRepeatZero();
        testRepeatOne();
        testRepeatFive();
        testRepeatDefault();
        testRepeatDefaultSingle();
        System.out.println();

        System.out.println("=== Warmup 05: Double List ===");
        testDoubleBasic();
        testDoubleNegatives();
        testDoubleSingle();
        testDoubleZeros();
        System.out.println();

        System.out.println("--- Practice Problems ---");

        System.out.println("=== Practice 01: Calculator ===");
        testCalcAdd();
        testCalcSubtract();
        testCalcMultiply();
        testCalcDivide();
        testCalcDivideByZero();
        testCalcInvalidOp();
        System.out.println();

        System.out.println("=== Practice 02: Password Strength ===");
        testPasswordShort();
        testPasswordLongNoSpecial();
        testPasswordWithDigit();
        testPasswordWithUpper();
        testPasswordStrong();
        testPasswordShortWithBoth();
        System.out.println();

        System.out.println("=== Practice 03: Temperature Conversion ===");
        testTempCToF();
        testTempFToC();
        testTempCToK();
        testTempKToC();
        testTempFToK();
        testTempSameUnit();
        System.out.println();

        System.out.println("=== Practice 04: Array Statistics ===");
        testStatsBasic();
        testStatsUniform();
        testStatsSingle();
        testStatsNegatives();
        testStatsRounding();
        System.out.println();

        System.out.println("--- Challenge Problems ---");

        System.out.println("=== Challenge 01: Prime Check ===");
        testPrime2();
        testPrime17();
        testPrime4();
        testPrime1();
        testPrime0();
        testPrimeNegative();
        testPrime97();
        testPrime25();
        System.out.println();

        System.out.println("=== Challenge 02: Apply Operations ===");
        testOpsSortDouble();
        testOpsNegateSortReverse();
        testOpsSquare();
        testOpsEmpty();
        testOpsUnknown();
        testOpsReverse();
        System.out.println();

        System.out.println("All Chapter 4 tests passed!");
    }
}
