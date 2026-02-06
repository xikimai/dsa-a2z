/*
 * Solution for Challenge 01: Diamond Pattern
 * ============================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * A diamond of size n has (2*n - 1) total rows.
 * The widest row (the middle) has (2*n - 1) stars.
 *
 * Upper half (rows 1..n): row i has (2*i - 1) stars, centered
 *   with (n - i) leading spaces.
 * Lower half (rows n+1..2n-1): mirror of the upper half.
 *   Row j maps to i = 2*n - j, giving (2*i - 1) stars and (n - i) spaces.
 *
 * No trailing spaces, no trailing newline.
 *
 * TIME COMPLEXITY:  O(n^2) — nested iteration
 * SPACE COMPLEXITY: O(n^2) — for the output string
 */

#include <iostream>
#include <string>
using namespace std;

string solve(int n) {
    string result;
    int totalRows = 2 * n - 1;
    for (int row = 1; row <= totalRows; row++) {
        if (row > 1) result += "\n";
        // Mirror: rows after center map back
        int i = (row <= n) ? row : (2 * n - row);
        int spaces = n - i;
        int stars = 2 * i - 1;
        result += string(spaces, ' ') + string(stars, '*');
    }
    return result;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
