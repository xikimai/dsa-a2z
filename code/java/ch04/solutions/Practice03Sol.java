package ch04.solutions;

import java.util.Scanner;

/**
 * Solution for Practice 03: Temperature Conversion
 * ==================================================
 * Chapter 4: Functions
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Define four base conversion helpers: cToF, fToC, cToK, kToC.
 * Build all six paths by chaining:
 *   F -> K = fToC then cToK
 *   K -> F = kToC then cToF
 * Return -1.0 for same-unit or invalid conversions.
 *
 * TIME COMPLEXITY:  O(1)
 * SPACE COMPLEXITY: O(1)
 */
public class Practice03Sol {

    public static double cToF(double c) {
        return c * 9.0 / 5.0 + 32.0;
    }

    public static double fToC(double f) {
        return (f - 32.0) * 5.0 / 9.0;
    }

    public static double cToK(double c) {
        return c + 273.15;
    }

    public static double kToC(double k) {
        return k - 273.15;
    }

    public static double solve(double value, String fromUnit, String toUnit) {
        if (fromUnit.equals(toUnit)) return -1.0;

        if (fromUnit.equals("C") && toUnit.equals("F")) return cToF(value);
        if (fromUnit.equals("F") && toUnit.equals("C")) return fToC(value);
        if (fromUnit.equals("C") && toUnit.equals("K")) return cToK(value);
        if (fromUnit.equals("K") && toUnit.equals("C")) return kToC(value);
        if (fromUnit.equals("F") && toUnit.equals("K")) return cToK(fToC(value));
        if (fromUnit.equals("K") && toUnit.equals("F")) return cToF(kToC(value));

        return -1.0;  // invalid unit
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double value = sc.nextDouble();
        String fromUnit = sc.next();
        String toUnit = sc.next();
        double result = solve(value, fromUnit, toUnit);
        System.out.printf("%.2f%n", result);
        sc.close();
    }
}
