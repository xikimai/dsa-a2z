/*
 * Challenge 1: Prime Check
 * ========================
 * Chapter 4: Functions
 *
 * PROBLEM:
 *   Check whether a number is prime. Implement THREE versions:
 *     - is_prime_v1: Brute force, check all divisors from 2 to n-1
 *     - is_prime_v2: Optimized, check divisors from 2 to sqrt(n)
 *     - is_prime_v3: Best, use 6k +/- 1 optimization
 *
 *   The solve() function should use is_prime_v3 (the best version).
 *
 * 6k +/- 1 TRICK:
 *   All primes > 3 are of the form 6k +/- 1. So after checking
 *   divisibility by 2 and 3, you only need to check divisors of
 *   the form 6k-1 and 6k+1 (i.e., 5, 7, 11, 13, 17, 19, ...).
 *
 * EXAMPLES:
 *   solve(2)     -> true
 *   solve(3)     -> true
 *   solve(4)     -> false
 *   solve(17)    -> true
 *   solve(1)     -> false
 *   solve(0)     -> false
 *   solve(-5)    -> false
 *   solve(97)    -> true
 *   solve(100003) -> true
 *
 * CONSTRAINTS:
 *   - n can be any integer
 *   - Use long long for i*i to avoid overflow with large numbers
 */

#include <iostream>
using namespace std;

// TODO: Write is_prime_v1, is_prime_v2, is_prime_v3

/**
 * Returns true if n is prime, false otherwise.
 * Uses is_prime_v3 (6k +/- 1 optimization).
 */
bool solve(int n) {
    // TODO: Replace this with your solution
    return false;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cout << (solve(n) ? "true" : "false") << endl;
    return 0;
}
