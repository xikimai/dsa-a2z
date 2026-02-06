/*
 * Solution — Challenge 1: Prime Check
 * ====================================
 * Chapter 4: Functions
 *
 * APPROACH:
 *   Three progressively better primality tests:
 *     v1: Check every number from 2 to n-1.          O(n)
 *     v2: Check from 2 to sqrt(n).                   O(sqrt(n))
 *     v3: Check 2, 3, then only 6k +/- 1 up to sqrt. O(sqrt(n)) with ~3x fewer checks
 *
 *   The 6k+/-1 trick works because every integer is of the form
 *   6k+0, 6k+1, 6k+2, 6k+3, 6k+4, or 6k+5.
 *   - 6k+0, 6k+2, 6k+4 are divisible by 2
 *   - 6k+3 is divisible by 3
 *   So primes > 3 must be 6k+1 or 6k+5 (which is 6k-1).
 *
 * TIME COMPLEXITY:  O(sqrt(n)) for v3
 * SPACE COMPLEXITY: O(1)
 */

#include <iostream>
using namespace std;

bool is_prime_v1(int n) {
    if (n < 2) return false;
    for (int i = 2; i < n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

bool is_prime_v2(int n) {
    if (n < 2) return false;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

bool is_prime_v3(int n) {
    if (n < 2) return false;
    if (n < 4) return true;        // 2 and 3 are prime
    if (n % 2 == 0) return false;   // even numbers > 2
    if (n % 3 == 0) return false;   // multiples of 3 > 3

    // Check 6k-1 and 6k+1 up to sqrt(n)
    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0) return false;       // 6k - 1
        if (n % (i + 2) == 0) return false; // 6k + 1
    }
    return true;
}

bool solve(int n) {
    return is_prime_v3(n);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cout << (solve(n) ? "true" : "false") << endl;
    return 0;
}
