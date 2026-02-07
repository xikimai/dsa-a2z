/*
 * Example 02: GCD Race & Number Theory Demos
 * ===========================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * This file demonstrates:
 *   Part 1: GCD by subtraction vs Euclidean (with timing)
 *   Part 2: Sieve of Eratosthenes (visual demo)
 *   Part 3: Binary exponentiation (fast power)
 *
 * Build & run:
 *   g++ -std=c++17 -o example_02 code/cpp/ch07/learn/example_02_gcd_race.cpp && ./example_02
 */

#include <chrono>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

// =====================================================================
// 1. GCD Race: Subtraction vs Euclidean
// =====================================================================
// Two ways to find the Greatest Common Divisor:
//   - Subtraction: Keep subtracting the smaller from the larger.
//     Simple but SLOW for numbers like gcd(1000000, 1).
//   - Euclidean: Use mod instead of subtraction. Much faster!

long long gcd_subtract(long long a, long long b) {
    if (a == 0) return b;
    if (b == 0) return a;
    while (a != b) {
        if (a > b) a -= b;
        else b -= a;
    }
    return a;
}

long long gcd_euclidean(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

void demo_gcd_race() {
    cout << "=== PART 1: GCD Race -- Subtraction vs Euclidean ===" << endl;
    cout << endl;

    struct TestCase {
        long long a, b;
        string label;
    };

    TestCase tests[] = {
        {48, 18, "Small numbers (48, 18)"},
        {12345, 6789, "Medium numbers (12345, 6789)"},
        {1000000, 1, "Worst case for subtraction (1000000, 1)"},
        {999999937LL, 999999929LL, "Two large primes"}
    };

    for (auto& tc : tests) {
        cout << "  " << tc.label << ":" << endl;

        // Time subtraction method (skip if worst case would be too slow)
        if (tc.a <= 1000000 && tc.b <= 1000000) {
            auto start = chrono::high_resolution_clock::now();
            long long result = gcd_subtract(tc.a, tc.b);
            auto end = chrono::high_resolution_clock::now();
            double elapsed = chrono::duration<double>(end - start).count();
            cout << "    Subtraction: gcd = " << result
                 << "  time = " << fixed << setprecision(6) << elapsed << "s" << endl;
        } else {
            cout << "    Subtraction: SKIPPED (would take too long!)" << endl;
        }

        // Time Euclidean method
        {
            auto start = chrono::high_resolution_clock::now();
            long long result = gcd_euclidean(tc.a, tc.b);
            auto end = chrono::high_resolution_clock::now();
            double elapsed = chrono::duration<double>(end - start).count();
            cout << "    Euclidean:   gcd = " << result
                 << "  time = " << fixed << setprecision(6) << elapsed << "s" << endl;
        }
        cout << endl;
    }
}

// =====================================================================
// 2. Sieve of Eratosthenes -- Visual Demo
// =====================================================================
// The sieve finds ALL primes up to n by "crossing out" multiples.
// It's one of the oldest algorithms in mathematics (circa 200 BC!).

void demo_sieve() {
    cout << "=== PART 2: Sieve of Eratosthenes ===" << endl;

    int n = 50;
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;

    cout << "  Finding all primes up to " << n << ":" << endl;
    cout << endl;

    for (int i = 2; (long long)i * i <= n; i++) {
        if (is_prime[i]) {
            cout << "  Sieving with " << i
                 << ": crossing out ";
            bool first = true;
            for (int j = i * i; j <= n; j += i) {
                if (is_prime[j]) {
                    if (!first) cout << ", ";
                    cout << j;
                    first = false;
                    is_prime[j] = false;
                }
            }
            if (first) cout << "(nothing new)";
            cout << endl;
        }
    }

    cout << endl << "  Primes up to " << n << ": ";
    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) cout << i << " ";
    }
    cout << endl;

    // Count primes up to larger numbers
    cout << endl << "  Prime counts:" << endl;
    int limits[] = {100, 1000, 10000, 100000};
    for (int limit : limits) {
        vector<bool> sieve(limit + 1, true);
        sieve[0] = sieve[1] = false;
        for (int i = 2; (long long)i * i <= limit; i++) {
            if (sieve[i]) {
                for (int j = i * i; j <= limit; j += i) sieve[j] = false;
            }
        }
        int count = 0;
        for (int i = 2; i <= limit; i++) if (sieve[i]) count++;
        cout << "    Primes up to " << setw(6) << limit << ": " << count << endl;
    }
    cout << endl;
}

// =====================================================================
// 3. Binary Exponentiation -- Fast Power
// =====================================================================
// Computing base^exp the naive way takes exp multiplications.
// Binary exponentiation does it in O(log exp) multiplications!
//
// The trick: break the exponent into binary.
//   2^13 = 2^(1101 in binary) = 2^8 * 2^4 * 2^1
//
// We use mod to keep numbers from overflowing.

long long power_naive(long long base, long long exp, long long mod) {
    long long result = 1;
    for (long long i = 0; i < exp; i++) {
        result = result * base % mod;
    }
    return result;
}

long long power_fast(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = result * base % mod;
        }
        exp /= 2;
        base = base * base % mod;
    }
    return result;
}

void demo_binary_exponentiation() {
    cout << "=== PART 3: Binary Exponentiation ===" << endl;

    long long mod = 1000000007;

    // Show step-by-step for a small example
    cout << "  Step-by-step: 2^13 mod " << mod << endl;
    long long base = 2, exp = 13;
    long long result = 1;
    long long b = base;
    int step = 0;
    long long e = exp;
    while (e > 0) {
        if (e % 2 == 1) {
            result = result * b % mod;
            cout << "    Step " << step << ": exp bit = 1, multiply by "
                 << b << " -> result = " << result << endl;
        } else {
            cout << "    Step " << step << ": exp bit = 0, skip" << endl;
        }
        e /= 2;
        b = b * b % mod;
        step++;
    }
    cout << "  Answer: 2^13 = " << result << endl;
    cout << endl;

    // Compare speeds
    cout << "  Speed comparison (base=2, mod=" << mod << "):" << endl;

    long long exponents[] = {100, 1000, 10000, 100000};
    for (long long exp_val : exponents) {
        // Naive
        auto start = chrono::high_resolution_clock::now();
        long long r1 = power_naive(2, exp_val, mod);
        auto end = chrono::high_resolution_clock::now();
        double t1 = chrono::duration<double>(end - start).count();

        // Fast
        start = chrono::high_resolution_clock::now();
        long long r2 = power_fast(2, exp_val, mod);
        end = chrono::high_resolution_clock::now();
        double t2 = chrono::duration<double>(end - start).count();

        cout << "    exp = " << setw(6) << exp_val
             << "  |  naive = " << fixed << setprecision(6) << t1 << "s"
             << "  |  fast = " << t2 << "s"
             << "  |  match = " << (r1 == r2 ? "YES" : "NO") << endl;
    }
    cout << endl;
}

// =====================================================================
// main -- run all demos
// =====================================================================
int main() {
    cout << "Chapter 7: GCD Race & Number Theory" << endl;
    cout << "====================================" << endl << endl;

    demo_gcd_race();
    demo_sieve();
    demo_binary_exponentiation();

    cout << "Key takeaway: the right algorithm makes ALL the difference." << endl;
    cout << "Euclidean GCD is O(log n) vs O(n) for subtraction." << endl;
    cout << "Binary exponentiation is O(log n) vs O(n) for naive power." << endl;
    return 0;
}
