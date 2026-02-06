/*
 * Solution -- Warmup 2: Is It Fast Enough?
 * =========================================
 * Chapter 6: How Fast Is Your Code?
 *
 * APPROACH:
 *   Compute the number of operations for the given complexity class
 *   using long long arithmetic.  Return true if ops < 10^8.
 *   Special case: for "2^n", if n > 30 return false immediately
 *   (since 2^31 already exceeds 10^8).
 *
 * TIME COMPLEXITY:  O(1)
 * SPACE COMPLEXITY: O(1)
 */

#include <cmath>
#include <iostream>
#include <string>
using namespace std;

bool solve(int n, string complexity) {
    long long limit = 100000000LL;  // 10^8
    long long ops = 0;

    if (complexity == "1") {
        ops = 1;
    } else if (complexity == "log_n") {
        ops = (long long)(log2(n));
    } else if (complexity == "n") {
        ops = (long long)n;
    } else if (complexity == "n_log_n") {
        ops = (long long)((double)n * log2(n));
    } else if (complexity == "n^2") {
        ops = (long long)n * n;
    } else if (complexity == "n^3") {
        ops = (long long)n * n * n;
    } else if (complexity == "2^n") {
        if (n > 30) return false;
        ops = 1LL << n;
    }

    return ops < limit;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    string complexity;
    cin >> n >> complexity;
    cout << (solve(n, complexity) ? "true" : "false") << endl;
    return 0;
}
