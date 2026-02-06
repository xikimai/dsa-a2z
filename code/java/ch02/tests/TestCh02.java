package ch02.tests;

import java.util.Arrays;

/**
 * Tests for Chapter 2: Your First Programs
 * ==========================================
 * Chapter 2: Your First Programs — Speaking Three Languages
 *
 * This file tests every solve() method from Chapter 2 using the reference
 * solutions. We define each solve() here so the test is self-contained.
 *
 * Build and run:
 *   cd code/java
 *   javac ch02/tests/TestCh02.java
 *   java -ea ch02.tests.TestCh02
 *
 * The -ea flag enables assertions. Without it, assert statements are ignored!
 */
public class TestCh02 {

    // ── Reference solutions ─────────────────────────────────────────

    static String solveGreeting(String name) {
        return "Hello, " + name + "!";
    }

    static int solveRectangleArea(int length, int width) {
        return length * width;
    }

    static double solveCelsiusToFahrenheit(double celsius) {
        return celsius * 9.0 / 5.0 + 32.0;
    }

    static int[] solveSwap(int a, int b) {
        return new int[]{b, a};
    }

    static int solveLastDigit(int n) {
        return Math.abs(n) % 10;
    }

    static double[] solveCircle(double radius) {
        double area = Math.PI * radius * radius;
        double circumference = 2 * Math.PI * radius;
        return new double[]{area, circumference};
    }

    static int[] solveTimeConversion(int totalSeconds) {
        int hours = totalSeconds / 3600;
        int minutes = (totalSeconds % 3600) / 60;
        int seconds = totalSeconds % 60;
        return new int[]{hours, minutes, seconds};
    }

    static double solveDistance(double x1, double y1, double x2, double y2) {
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }

    static int[] solveExtractDigits(int n) {
        int hundreds = n / 100;
        int tens = (n / 10) % 10;
        int ones = n % 10;
        return new int[]{hundreds, tens, ones};
    }

    static double[] solveQuadratic(double a, double b, double c) {
        double disc = b * b - 4 * a * c;
        double numRoots;
        if (disc > 0) {
            numRoots = 2.0;
        } else if (disc == 0) {
            numRoots = 1.0;
        } else {
            numRoots = 0.0;
        }
        return new double[]{disc, numRoots};
    }

    // ── Helper for comparing doubles ────────────────────────────────

    static void assertDoubleEquals(double expected, double actual, String msg) {
        assert Math.abs(expected - actual) < 1e-9
            : msg + " — expected " + expected + ", got " + actual;
    }

    // ── Warmup 01: Greeting ─────────────────────────────────────────

    static void testGreetingBasic() {
        assert solveGreeting("Alex").equals("Hello, Alex!")
            : "Expected 'Hello, Alex!'";
        System.out.println("  test_greeting_basic.............. PASS");
    }

    static void testGreetingWorld() {
        assert solveGreeting("World").equals("Hello, World!")
            : "Expected 'Hello, World!'";
        System.out.println("  test_greeting_world.............. PASS");
    }

    static void testGreetingWithSpaces() {
        assert solveGreeting("Ada Lovelace").equals("Hello, Ada Lovelace!")
            : "Expected 'Hello, Ada Lovelace!'";
        System.out.println("  test_greeting_with_spaces........ PASS");
    }

    static void testGreetingSingleChar() {
        assert solveGreeting("A").equals("Hello, A!")
            : "Expected 'Hello, A!'";
        System.out.println("  test_greeting_single_char........ PASS");
    }

    // ── Warmup 02: Rectangle Area ───────────────────────────────────

    static void testRectangleBasic() {
        assert solveRectangleArea(5, 3) == 15
            : "Expected 15, got " + solveRectangleArea(5, 3);
        System.out.println("  test_rectangle_basic............. PASS");
    }

    static void testRectangleSquare() {
        assert solveRectangleArea(10, 10) == 100
            : "Expected 100";
        System.out.println("  test_rectangle_square............ PASS");
    }

    static void testRectangleUnit() {
        assert solveRectangleArea(1, 1) == 1
            : "Expected 1";
        System.out.println("  test_rectangle_unit.............. PASS");
    }

    static void testRectangleLarge() {
        assert solveRectangleArea(10000, 10000) == 100000000
            : "Expected 100000000";
        System.out.println("  test_rectangle_large............. PASS");
    }

    // ── Warmup 03: Celsius to Fahrenheit ────────────────────────────

    static void testCelsiusFreezing() {
        assertDoubleEquals(32.0, solveCelsiusToFahrenheit(0.0),
            "Freezing point");
        System.out.println("  test_celsius_freezing............ PASS");
    }

    static void testCelsiusBoiling() {
        assertDoubleEquals(212.0, solveCelsiusToFahrenheit(100.0),
            "Boiling point");
        System.out.println("  test_celsius_boiling............. PASS");
    }

    static void testCelsiusBody() {
        assertDoubleEquals(98.6, solveCelsiusToFahrenheit(37.0),
            "Body temperature");
        System.out.println("  test_celsius_body................ PASS");
    }

    static void testCelsiusNegative() {
        assertDoubleEquals(-40.0, solveCelsiusToFahrenheit(-40.0),
            "-40 is same in both scales");
        System.out.println("  test_celsius_negative............ PASS");
    }

    static void testCelsiusAbsoluteZero() {
        assertDoubleEquals(-459.67, solveCelsiusToFahrenheit(-273.15),
            "Absolute zero");
        System.out.println("  test_celsius_absolute_zero....... PASS");
    }

    // ── Warmup 04: Swap ─────────────────────────────────────────────

    static void testSwapBasic() {
        int[] result = solveSwap(3, 7);
        assert result[0] == 7 && result[1] == 3
            : "Expected [7, 3], got " + Arrays.toString(result);
        System.out.println("  test_swap_basic.................. PASS");
    }

    static void testSwapNegative() {
        int[] result = solveSwap(-1, 5);
        assert result[0] == 5 && result[1] == -1
            : "Expected [5, -1]";
        System.out.println("  test_swap_negative............... PASS");
    }

    static void testSwapZeros() {
        int[] result = solveSwap(0, 0);
        assert result[0] == 0 && result[1] == 0
            : "Expected [0, 0]";
        System.out.println("  test_swap_zeros.................. PASS");
    }

    static void testSwapSame() {
        int[] result = solveSwap(42, 42);
        assert result[0] == 42 && result[1] == 42
            : "Expected [42, 42]";
        System.out.println("  test_swap_same................... PASS");
    }

    // ── Warmup 05: Last Digit ───────────────────────────────────────

    static void testLastDigitPositive() {
        assert solveLastDigit(1234) == 4
            : "Expected 4, got " + solveLastDigit(1234);
        System.out.println("  test_last_digit_positive......... PASS");
    }

    static void testLastDigitNegative() {
        assert solveLastDigit(-567) == 7
            : "Expected 7";
        System.out.println("  test_last_digit_negative......... PASS");
    }

    static void testLastDigitZero() {
        assert solveLastDigit(0) == 0
            : "Expected 0";
        System.out.println("  test_last_digit_zero............. PASS");
    }

    static void testLastDigitTen() {
        assert solveLastDigit(10) == 0
            : "Expected 0";
        System.out.println("  test_last_digit_ten.............. PASS");
    }

    static void testLastDigitSingleDigit() {
        assert solveLastDigit(9) == 9
            : "Expected 9";
        System.out.println("  test_last_digit_single........... PASS");
    }

    // ── Practice 01: Circle Properties ──────────────────────────────

    static void testCircleUnitRadius() {
        double[] result = solveCircle(1.0);
        assertDoubleEquals(Math.PI, result[0], "Unit circle area");
        assertDoubleEquals(2 * Math.PI, result[1], "Unit circle circumference");
        System.out.println("  test_circle_unit_radius.......... PASS");
    }

    static void testCircleRadius5() {
        double[] result = solveCircle(5.0);
        assertDoubleEquals(78.53981633974483, result[0], "Circle area r=5");
        assertDoubleEquals(31.41592653589793, result[1], "Circle circ r=5");
        System.out.println("  test_circle_radius_5............. PASS");
    }

    static void testCircleSmallRadius() {
        double[] result = solveCircle(0.5);
        assertDoubleEquals(0.7853981633974483, result[0], "Circle area r=0.5");
        assertDoubleEquals(3.141592653589793, result[1], "Circle circ r=0.5");
        System.out.println("  test_circle_small_radius......... PASS");
    }

    static void testCircleLargeRadius() {
        double[] result = solveCircle(100.0);
        assertDoubleEquals(Math.PI * 10000.0, result[0], "Circle area r=100");
        assertDoubleEquals(200.0 * Math.PI, result[1], "Circle circ r=100");
        System.out.println("  test_circle_large_radius......... PASS");
    }

    // ── Practice 02: Time Conversion ────────────────────────────────

    static void testTimeBasic() {
        int[] result = solveTimeConversion(3661);
        assert result[0] == 1 && result[1] == 1 && result[2] == 1
            : "Expected [1, 1, 1], got " + Arrays.toString(result);
        System.out.println("  test_time_basic.................. PASS");
    }

    static void testTimeZero() {
        int[] result = solveTimeConversion(0);
        assert result[0] == 0 && result[1] == 0 && result[2] == 0
            : "Expected [0, 0, 0]";
        System.out.println("  test_time_zero................... PASS");
    }

    static void testTimeExactHours() {
        int[] result = solveTimeConversion(7200);
        assert result[0] == 2 && result[1] == 0 && result[2] == 0
            : "Expected [2, 0, 0]";
        System.out.println("  test_time_exact_hours............ PASS");
    }

    static void testTimeMinutesAndSeconds() {
        int[] result = solveTimeConversion(90);
        assert result[0] == 0 && result[1] == 1 && result[2] == 30
            : "Expected [0, 1, 30]";
        System.out.println("  test_time_minutes_seconds........ PASS");
    }

    static void testTimeLarge() {
        int[] result = solveTimeConversion(86399);
        assert result[0] == 23 && result[1] == 59 && result[2] == 59
            : "Expected [23, 59, 59]";
        System.out.println("  test_time_large.................. PASS");
    }

    // ── Practice 03: Distance ───────────────────────────────────────

    static void testDistance345() {
        assertDoubleEquals(5.0, solveDistance(0.0, 0.0, 3.0, 4.0),
            "3-4-5 triangle");
        System.out.println("  test_distance_345................ PASS");
    }

    static void testDistanceSamePoint() {
        assertDoubleEquals(0.0, solveDistance(1.0, 1.0, 1.0, 1.0),
            "Same point");
        System.out.println("  test_distance_same_point......... PASS");
    }

    static void testDistanceNegative() {
        assertDoubleEquals(5.0, solveDistance(-1.0, -1.0, 2.0, 3.0),
            "Negative coords");
        System.out.println("  test_distance_negative........... PASS");
    }

    static void testDistanceHorizontal() {
        assertDoubleEquals(10.0, solveDistance(0.0, 0.0, 10.0, 0.0),
            "Horizontal line");
        System.out.println("  test_distance_horizontal......... PASS");
    }

    static void testDistanceVertical() {
        assertDoubleEquals(7.0, solveDistance(3.0, 0.0, 3.0, 7.0),
            "Vertical line");
        System.out.println("  test_distance_vertical........... PASS");
    }

    // ── Challenge 01: Extract Digits ────────────────────────────────

    static void testExtractBasic() {
        int[] result = solveExtractDigits(123);
        assert result[0] == 1 && result[1] == 2 && result[2] == 3
            : "Expected [1, 2, 3], got " + Arrays.toString(result);
        System.out.println("  test_extract_basic............... PASS");
    }

    static void testExtractWithZero() {
        int[] result = solveExtractDigits(507);
        assert result[0] == 5 && result[1] == 0 && result[2] == 7
            : "Expected [5, 0, 7]";
        System.out.println("  test_extract_with_zero........... PASS");
    }

    static void testExtractAllNines() {
        int[] result = solveExtractDigits(999);
        assert result[0] == 9 && result[1] == 9 && result[2] == 9
            : "Expected [9, 9, 9]";
        System.out.println("  test_extract_all_nines........... PASS");
    }

    static void testExtractMinimum() {
        int[] result = solveExtractDigits(100);
        assert result[0] == 1 && result[1] == 0 && result[2] == 0
            : "Expected [1, 0, 0]";
        System.out.println("  test_extract_minimum............. PASS");
    }

    static void testExtractMiddleZero() {
        int[] result = solveExtractDigits(305);
        assert result[0] == 3 && result[1] == 0 && result[2] == 5
            : "Expected [3, 0, 5]";
        System.out.println("  test_extract_middle_zero......... PASS");
    }

    // ── Challenge 02: Quadratic Discriminant ────────────────────────

    static void testQuadraticTwoRoots() {
        double[] result = solveQuadratic(1.0, -3.0, 2.0);
        assertDoubleEquals(1.0, result[0], "Discriminant for x^2-3x+2");
        assertDoubleEquals(2.0, result[1], "Should have 2 roots");
        System.out.println("  test_quadratic_two_roots......... PASS");
    }

    static void testQuadraticOneRoot() {
        double[] result = solveQuadratic(1.0, 2.0, 1.0);
        assertDoubleEquals(0.0, result[0], "Discriminant for x^2+2x+1");
        assertDoubleEquals(1.0, result[1], "Should have 1 root");
        System.out.println("  test_quadratic_one_root.......... PASS");
    }

    static void testQuadraticNoRoots() {
        double[] result = solveQuadratic(1.0, 1.0, 1.0);
        assertDoubleEquals(-3.0, result[0], "Discriminant for x^2+x+1");
        assertDoubleEquals(0.0, result[1], "Should have 0 roots");
        System.out.println("  test_quadratic_no_roots.......... PASS");
    }

    static void testQuadraticLargeDisc() {
        double[] result = solveQuadratic(1.0, 10.0, 1.0);
        assertDoubleEquals(96.0, result[0], "Discriminant for x^2+10x+1");
        assertDoubleEquals(2.0, result[1], "Should have 2 roots");
        System.out.println("  test_quadratic_large_disc........ PASS");
    }

    static void testQuadraticNegativeCoeffs() {
        double[] result = solveQuadratic(2.0, -4.0, 2.0);
        assertDoubleEquals(0.0, result[0], "Discriminant for 2x^2-4x+2");
        assertDoubleEquals(1.0, result[1], "Should have 1 root");
        System.out.println("  test_quadratic_negative_coeffs... PASS");
    }

    // ── Runner ──────────────────────────────────────────────────────

    public static void main(String[] args) {

        System.out.println("=== Warmup 01: Greeting ===");
        testGreetingBasic();
        testGreetingWorld();
        testGreetingWithSpaces();
        testGreetingSingleChar();
        System.out.println();

        System.out.println("=== Warmup 02: Rectangle Area ===");
        testRectangleBasic();
        testRectangleSquare();
        testRectangleUnit();
        testRectangleLarge();
        System.out.println();

        System.out.println("=== Warmup 03: Celsius to Fahrenheit ===");
        testCelsiusFreezing();
        testCelsiusBoiling();
        testCelsiusBody();
        testCelsiusNegative();
        testCelsiusAbsoluteZero();
        System.out.println();

        System.out.println("=== Warmup 04: Swap ===");
        testSwapBasic();
        testSwapNegative();
        testSwapZeros();
        testSwapSame();
        System.out.println();

        System.out.println("=== Warmup 05: Last Digit ===");
        testLastDigitPositive();
        testLastDigitNegative();
        testLastDigitZero();
        testLastDigitTen();
        testLastDigitSingleDigit();
        System.out.println();

        System.out.println("=== Practice 01: Circle Properties ===");
        testCircleUnitRadius();
        testCircleRadius5();
        testCircleSmallRadius();
        testCircleLargeRadius();
        System.out.println();

        System.out.println("=== Practice 02: Time Conversion ===");
        testTimeBasic();
        testTimeZero();
        testTimeExactHours();
        testTimeMinutesAndSeconds();
        testTimeLarge();
        System.out.println();

        System.out.println("=== Practice 03: Distance ===");
        testDistance345();
        testDistanceSamePoint();
        testDistanceNegative();
        testDistanceHorizontal();
        testDistanceVertical();
        System.out.println();

        System.out.println("=== Challenge 01: Extract Digits ===");
        testExtractBasic();
        testExtractWithZero();
        testExtractAllNines();
        testExtractMinimum();
        testExtractMiddleZero();
        System.out.println();

        System.out.println("=== Challenge 02: Quadratic Discriminant ===");
        testQuadraticTwoRoots();
        testQuadraticOneRoot();
        testQuadraticNoRoots();
        testQuadraticLargeDisc();
        testQuadraticNegativeCoeffs();
        System.out.println();

        System.out.println("All Chapter 2 tests passed!");
    }
}
