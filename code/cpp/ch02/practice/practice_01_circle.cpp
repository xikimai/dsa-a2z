/*
 * Practice 01: Circle Properties
 * ================================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given the radius of a circle, compute its area and circumference.
 *   area = pi * r * r
 *   circumference = 2 * pi * r
 *
 * INPUT FORMAT
 * ------------
 * A single line containing a double: the radius.
 *
 * OUTPUT FORMAT
 * -------------
 * Print two doubles separated by a space: area and circumference.
 *
 * CONSTRAINTS
 * -----------
 * 0 < radius <= 10^4
 *
 * EXAMPLES
 * --------
 * Input:  1
 * Output: 3.14159 6.28319  (approximately)
 *
 * Input:  5
 * Output: 78.5398 31.4159  (approximately)
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return {0.0, 0.0};" in the solve() function with your solution.
 * Use M_PI from <cmath> for the value of pi.
 * The main function handles input/output — don't change it.
 */

#include <iostream>
#include <cmath>     // for M_PI
#include <utility>   // for pair
using namespace std;

/**
 * Return a pair of (area, circumference) for a circle with the given radius.
 */
pair<double, double> solve(double radius) {
    // TODO: Replace this with your solution
    return {0.0, 0.0};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    double radius;
    cin >> radius;
    auto result = solve(radius);
    cout << result.first << " " << result.second << endl;
    return 0;
}
