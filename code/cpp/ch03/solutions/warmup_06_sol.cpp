/*
 * Solution for Warmup 06: Multiplication Table
 * ===============================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Loop from 1 to 10. For each i, build the string "i x n = i*n"
 * using to_string() for integer-to-string conversion.
 *
 * TIME COMPLEXITY:  O(1) — always exactly 10 iterations
 * SPACE COMPLEXITY: O(1) — the 10 strings in the result (constant size)
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> solve(int n) {
    vector<string> result;
    for (int i = 1; i <= 10; i++) {
        result.push_back(to_string(i) + " x " + to_string(n) + " = " + to_string(i * n));
    }
    return result;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    vector<string> result = solve(n);
    for (const string& line : result) {
        cout << line << endl;
    }
    return 0;
}
