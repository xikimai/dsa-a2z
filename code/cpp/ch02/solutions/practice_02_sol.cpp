/*
 * Solution for Practice 02: Time Conversion
 * ============================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use integer division and modulo to break down total seconds:
 *   hours   = totalSeconds / 3600
 *   minutes = (totalSeconds % 3600) / 60
 *   seconds = totalSeconds % 60
 *
 * The key insight: first get hours by dividing by 3600 (seconds in an hour),
 * then use the remainder to figure out minutes and leftover seconds.
 *
 * TIME COMPLEXITY:  O(1) — a few divisions
 * SPACE COMPLEXITY: O(1) — no extra memory
 */

#include <iostream>
#include <tuple>  // for tuple
using namespace std;

/**
 * Convert totalSeconds into hours, minutes, and seconds.
 * Returns a tuple of (hours, minutes, seconds).
 */
tuple<int, int, int> solve(int totalSeconds) {
    int h = totalSeconds / 3600;
    int m = (totalSeconds % 3600) / 60;
    int s = totalSeconds % 60;
    return {h, m, s};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int totalSeconds;
    cin >> totalSeconds;
    auto [h, m, s] = solve(totalSeconds);
    cout << h << ":" << m << ":" << s << endl;
    return 0;
}
