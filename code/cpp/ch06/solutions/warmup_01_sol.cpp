/*
 * Solution -- Warmup 1: Count the Steps
 * ======================================
 * Chapter 6: How Fast Is Your Code?
 *
 * APPROACH:
 *   Simple conditional dispatch on the code_id string.
 *   Each pattern maps to a formula based on n.
 *
 * TIME COMPLEXITY:  O(1)
 * SPACE COMPLEXITY: O(1)
 */

#include <cmath>
#include <iostream>
#include <string>
using namespace std;

int solve(string code_id, int n) {
    if (code_id == "single_loop") return n;
    if (code_id == "double_loop") return n * n;
    if (code_id == "half_loop") return n / 2;
    if (code_id == "dependent_loop") return n * (n + 1) / 2;
    if (code_id == "log_loop") {
        if (n < 1) return 0;
        return (int)(log2(n));
    }
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    string code_id;
    int n;
    cin >> code_id >> n;
    cout << solve(code_id, n) << endl;
    return 0;
}
