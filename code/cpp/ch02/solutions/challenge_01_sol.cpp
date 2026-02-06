/*
 * Solution for Challenge 01: Extract Digits
 * ===========================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use integer division and modulo to extract each digit position:
 *   hundreds = n / 100        (e.g., 123 / 100 = 1)
 *   tens     = (n / 10) % 10  (e.g., 123 / 10 = 12, 12 % 10 = 2)
 *   ones     = n % 10         (e.g., 123 % 10 = 3)
 *
 * This is a fundamental technique — you'll use it a LOT in competitive
 * programming whenever you need to work with individual digits.
 *
 * TIME COMPLEXITY:  O(1) — three operations
 * SPACE COMPLEXITY: O(1) — no extra memory
 */

#include <iostream>
#include <tuple>  // for tuple
using namespace std;

/**
 * Extract the hundreds, tens, and ones digits of a 3-digit number.
 * Returns a tuple of (hundreds, tens, ones).
 */
tuple<int, int, int> solve(int n) {
    int hundreds = n / 100;
    int tens = (n / 10) % 10;
    int ones = n % 10;
    return {hundreds, tens, ones};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    auto [h, t, o] = solve(n);
    cout << h << " " << t << " " << o << endl;
    return 0;
}
