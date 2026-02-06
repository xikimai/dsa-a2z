/*
 * Warmup 04: Count Down
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * PROBLEM
 * -------
 * Given a positive integer n, return a vector containing the countdown
 * from n down to 1: [n, n-1, n-2, ..., 2, 1].
 *
 * INPUT FORMAT
 * ------------
 * A single line containing a positive integer n.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the numbers from n down to 1, each on a separate line.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= n <= 1000
 *
 * EXAMPLES
 * --------
 * Input:  5
 * Output: 5 4 3 2 1
 *
 * Input:  1
 * Output: 1
 *
 * Input:  3
 * Output: 3 2 1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the body of solve() with your solution.
 * The main() function handles I/O -- don't change it.
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Return a vector counting down from n to 1.
 */
vector<int> solve(int n) {
    // TODO: Replace this with your solution
    return {};
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    vector<int> result = solve(n);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
