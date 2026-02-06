/*
 * Solution -- Challenge 2: Performance Showdown
 * ===============================================
 * Chapter 6: How Fast Is Your Code?
 *
 * APPROACH:
 *   Map each complexity string to its operation count (as double to
 *   handle large values), then compare. Return "A" if A has fewer
 *   ops, "B" if B has fewer, "TIE" if equal.
 *
 * TIME COMPLEXITY:  O(1)
 * SPACE COMPLEXITY: O(1)
 */

#include <cmath>
#include <iostream>
#include <string>
using namespace std;

static double get_ops(string complexity, int n) {
    if (complexity == "1") return 1.0;
    if (complexity == "log_n") return log2((double)n);
    if (complexity == "n") return (double)n;
    if (complexity == "n_log_n") return (double)n * log2((double)n);
    if (complexity == "n^2") return (double)n * n;
    if (complexity == "n^3") return (double)n * n * n;
    if (complexity == "2^n") return pow(2.0, n);
    return 0.0;
}

string solve(string complexity_a, string complexity_b, int n) {
    double ops_a = get_ops(complexity_a, n);
    double ops_b = get_ops(complexity_b, n);

    if (ops_a < ops_b) return "A";
    if (ops_b < ops_a) return "B";
    return "TIE";
}

// -- Do not change anything below this line --------------------------
int main() {
    string a, b;
    int n;
    cin >> a >> b >> n;
    cout << solve(a, b, n) << endl;
    return 0;
}
