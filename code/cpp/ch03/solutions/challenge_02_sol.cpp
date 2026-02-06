/*
 * Solution for Challenge 02: Prime Check
 * ========================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * 1. Numbers <= 1 are not prime.
 * 2. 2 is prime (the only even prime).
 * 3. Even numbers > 2 are not prime.
 * 4. Check odd divisors from 3 up to sqrt(n). If any divides n, it's
 *    not prime. Otherwise it is prime.
 *
 * Why only up to sqrt(n)? If n = a * b and both a,b > sqrt(n), then
 * a * b > n, which is a contradiction. So at least one factor must be
 * <= sqrt(n).
 *
 * TIME COMPLEXITY:  O(sqrt(n)) — check divisors up to sqrt(n)
 * SPACE COMPLEXITY: O(1) — no extra memory
 */

#include <iostream>
#include <string>
using namespace std;

bool solve(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; (long long)i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    int n;
    cin >> n;
    cout << (solve(n) ? "true" : "false") << endl;
    return 0;
}
