/*
 * Practice 3: Temperature Converter
 * ==================================
 * Chapter 4: Functions
 *
 * PROBLEM:
 *   Convert between Celsius (C), Fahrenheit (F), and Kelvin (K).
 *   Write helper functions: c_to_f, f_to_c, c_to_k, k_to_c.
 *   Use helpers to build the general solve() converter.
 *   Round result to 1 decimal place.
 *
 * FORMULAS:
 *   C to F: F = C * 9/5 + 32
 *   F to C: C = (F - 32) * 5/9
 *   C to K: K = C + 273.15
 *   K to C: C = K - 273.15
 *
 * EXAMPLES:
 *   solve(100.0, "C", "F")  -> 212.0
 *   solve(32.0, "F", "C")   -> 0.0
 *   solve(0.0, "C", "K")    -> 273.2   (273.15 rounds to 273.2)
 *   solve(300.0, "K", "F")  -> 80.3
 *   solve(50.0, "C", "C")   -> 50.0    (same unit)
 *   solve(50.0, "X", "C")   -> -1.0    (invalid unit)
 *
 * CONSTRAINTS:
 *   - Valid units: "C", "F", "K"
 *   - Return -1.0 for invalid units
 *   - Round to 1 decimal place using: round(result * 10.0) / 10.0
 */

#include <cmath>
#include <iostream>
#include <string>
using namespace std;

// TODO: Write helpers: c_to_f, f_to_c, c_to_k, k_to_c

/**
 * Converts temperature from one unit to another.
 * Returns -1.0 for invalid units.
 */
double solve(double value, string from_unit, string to_unit) {
    // TODO: Replace this with your solution
    return -1.0;
}

// -- Do not change anything below this line --------------------------
int main() {
    double value;
    string from_unit, to_unit;
    cin >> value >> from_unit >> to_unit;
    double result = solve(value, from_unit, to_unit);
    cout << result << endl;
    return 0;
}
