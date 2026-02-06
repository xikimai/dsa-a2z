/*
 * Solution — Practice 3: Temperature Converter
 * =============================================
 * Chapter 4: Functions
 *
 * APPROACH:
 *   Convert everything through Celsius as the intermediate unit.
 *   - If from_unit is "F" or "K", convert to Celsius first.
 *   - If to_unit is "F" or "K", convert from Celsius.
 *   - Round to 1 decimal place at the end.
 *
 * TIME COMPLEXITY:  O(1)
 * SPACE COMPLEXITY: O(1)
 */

#include <cmath>
#include <iostream>
#include <string>
using namespace std;

double c_to_f(double c) {
    return c * 9.0 / 5.0 + 32.0;
}

double f_to_c(double f) {
    return (f - 32.0) * 5.0 / 9.0;
}

double c_to_k(double c) {
    return c + 273.15;
}

double k_to_c(double k) {
    return k - 273.15;
}

double solve(double value, string from_unit, string to_unit) {
    // Validate units
    if (from_unit != "C" && from_unit != "F" && from_unit != "K") return -1.0;
    if (to_unit != "C" && to_unit != "F" && to_unit != "K") return -1.0;

    // Same unit — no conversion needed
    if (from_unit == to_unit) {
        return round(value * 10.0) / 10.0;
    }

    // Step 1: Convert to Celsius
    double celsius = value;
    if (from_unit == "F") celsius = f_to_c(value);
    if (from_unit == "K") celsius = k_to_c(value);

    // Step 2: Convert from Celsius to target
    double result = celsius;
    if (to_unit == "F") result = c_to_f(celsius);
    if (to_unit == "K") result = c_to_k(celsius);

    // Round to 1 decimal place
    return round(result * 10.0) / 10.0;
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
