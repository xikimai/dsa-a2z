/*
 * Solution for Practice 03: Distance Between Two Points
 * ======================================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Apply the Euclidean distance formula:
 *   distance = sqrt((x2-x1)^2 + (y2-y1)^2)
 *
 * We compute the differences, square them, add them up, and take the
 * square root. No need for pow() — just multiply dx*dx.
 *
 * TIME COMPLEXITY:  O(1) — a few arithmetic operations + sqrt
 * SPACE COMPLEXITY: O(1) — no extra memory
 */

#include <iostream>
#include <cmath>  // for sqrt
using namespace std;

/**
 * Return the Euclidean distance between points (x1,y1) and (x2,y2).
 */
double solve(double x1, double y1, double x2, double y2) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    return sqrt(dx * dx + dy * dy);
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    double x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    cout << solve(x1, y1, x2, y2) << endl;
    return 0;
}
