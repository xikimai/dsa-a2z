package ch04.practice;

import java.util.Scanner;

/**
 * Practice 03: Temperature Conversion
 * ==============================
 * Chapter 4: Functions
 *
 * PROBLEM
 * -------
 * Write a temperature converter that handles conversions between
 * Celsius (C), Fahrenheit (F), and Kelvin (K).
 *
 * Use helper functions cToF(), fToC(), cToK(), kToC() to build
 * all six conversion paths.
 *
 * Formulas:
 *   C to F:  F = C * 9/5 + 32
 *   F to C:  C = (F - 32) * 5/9
 *   C to K:  K = C + 273.15
 *   K to C:  C = K - 273.15
 *
 * INPUT FORMAT
 * ------------
 * One line: value fromUnit toUnit
 * Example: 100 C F
 *
 * OUTPUT FORMAT
 * -------------
 * Print the converted value rounded to 2 decimal places.
 * Print -1.0 for invalid units or same-unit conversion.
 *
 * CONSTRAINTS
 * -----------
 * - value is a floating-point number
 * - fromUnit and toUnit are one of "C", "F", "K"
 *
 * EXAMPLES
 * --------
 * Input:  100 C F
 * Output: 212.00
 *
 * Input:  32 F C
 * Output: 0.00
 *
 * Input:  0 C K
 * Output: 273.15
 *
 * INSTRUCTIONS
 * ------------
 * 1. Implement cToF(), fToC(), cToK(), kToC() helpers.
 * 2. Build all 6 conversions by chaining helpers (e.g., F to K = fToC then cToK).
 * 3. Return -1.0 for invalid or same-unit conversion.
 * The main method handles input/output -- don't change it.
 */
public class Practice03Temperature {

    /** Convert Celsius to Fahrenheit. */
    public static double cToF(double c) {
        // TODO: Implement
        return 0.0;
    }

    /** Convert Fahrenheit to Celsius. */
    public static double fToC(double f) {
        // TODO: Implement
        return 0.0;
    }

    /** Convert Celsius to Kelvin. */
    public static double cToK(double c) {
        // TODO: Implement
        return 0.0;
    }

    /** Convert Kelvin to Celsius. */
    public static double kToC(double k) {
        // TODO: Implement
        return 0.0;
    }

    /**
     * Convert a temperature value between units.
     *
     * @param value    the temperature value
     * @param fromUnit the source unit ("C", "F", or "K")
     * @param toUnit   the target unit ("C", "F", or "K")
     * @return the converted value, or -1.0 for invalid/same-unit
     */
    public static double solve(double value, String fromUnit, String toUnit) {
        // TODO: Replace this with your solution
        return -1.0;
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
