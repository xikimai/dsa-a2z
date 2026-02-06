/*
 * Solution for Practice 01: Circle Properties
 * ==============================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use the standard circle formulas:
 *   area = pi * r * r
 *   circumference = 2 * pi * r
 *
 * M_PI is a constant defined in <cmath> that gives a precise value of pi.
 *
 * TIME COMPLEXITY:  O(1) — a few multiplications
 * SPACE COMPLEXITY: O(1) — no extra memory
 */

#include <iostream>
#include <cmath>     // for M_PI
#include <utility>   // for pair
using namespace std;

/**
 * Return a pair of (area, circumference) for a circle with the given radius.
 */
pair<double, double> solve(double radius) {
    double area = M_PI * radius * radius;
    double circumference = 2.0 * M_PI * radius;
    return {area, circumference};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    double radius;
    cin >> radius;
    auto result = solve(radius);
    cout << result.first << " " << result.second << endl;
    return 0;
}
