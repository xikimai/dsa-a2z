package ch02.practice;

import java.util.Scanner;

/**
 * Warmup 03: Celsius to Fahrenheit
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given a temperature in Celsius, convert it to Fahrenheit.
 * Formula: F = C * 9.0 / 5.0 + 32.0
 *
 * INPUT FORMAT
 * ------------
 * A single line containing one double: the temperature in Celsius.
 *
 * OUTPUT FORMAT
 * -------------
 * Print a single double — the temperature in Fahrenheit.
 *
 * CONSTRAINTS
 * -----------
 * -273.15 <= celsius <= 10^6
 *
 * EXAMPLES
 * --------
 * Input:  0.0
 * Output: 32.0
 *
 * Input:  100.0
 * Output: 212.0
 *
 * Input:  37.0
 * Output: 98.6
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0.0;" in the solve() method with your solution.
 * The main method handles input/output — don't change it.
 */
public class Warmup03CelsiusToFahrenheit {

    /**
     * Convert Celsius to Fahrenheit.
     *
     * @param celsius the temperature in Celsius
     * @return the temperature in Fahrenheit
     */
    public static double solve(double celsius) {
        // TODO: Replace this with your solution
        return 0.0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double celsius = scanner.nextDouble();
        System.out.println(solve(celsius));
        scanner.close();
    }
}
