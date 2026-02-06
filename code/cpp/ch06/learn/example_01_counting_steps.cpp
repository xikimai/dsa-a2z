/*
 * Example 01: Counting Steps
 * ==========================
 * Chapter 6: How Fast Is Your Code?
 *
 * This file walks through four complexity classes by computing the
 * sum 1 + 2 + ... + n in different ways, timing each one.
 *   Part 1: O(1)     — formula
 *   Part 2: O(n)     — single loop
 *   Part 3: O(n^2)   — nested loops
 *   Part 4: O(log n) — halving
 *
 * Build & run:
 *   g++ -std=c++17 -o example_01 code/cpp/ch06/learn/example_01_counting_steps.cpp && ./example_01
 */

#include <chrono>
#include <iomanip>
#include <iostream>
using namespace std;

// =====================================================================
// 1. O(1) — Constant time (formula)
// =====================================================================
// The sum 1 + 2 + ... + n can be computed instantly with a formula.
// No matter how large n is, it takes the same amount of work.

void demo_constant() {
    cout << "=== PART 1: O(1) -- Formula ===" << endl;

    long long sizes[] = {1000, 1000000, 1000000000};
    for (long long n : sizes) {
        auto start = chrono::high_resolution_clock::now();
        long long result = n * (n + 1) / 2;
        auto end = chrono::high_resolution_clock::now();
        double elapsed = chrono::duration<double>(end - start).count();
        cout << "  n = " << setw(13) << n
             << "  |  sum = " << setw(20) << result
             << "  |  time = " << fixed << setprecision(6) << elapsed << "s" << endl;
    }
    cout << endl;
}

// =====================================================================
// 2. O(n) — Linear time (loop)
// =====================================================================
// Adding numbers one by one takes time proportional to n.
// Double n, and the time roughly doubles.

void demo_linear() {
    cout << "=== PART 2: O(n) -- Loop ===" << endl;

    int sizes[] = {10000, 100000, 1000000};
    for (int n : sizes) {
        auto start = chrono::high_resolution_clock::now();
        long long total = 0;
        for (int i = 1; i <= n; i++) {
            total += i;
        }
        auto end = chrono::high_resolution_clock::now();
        double elapsed = chrono::duration<double>(end - start).count();
        cout << "  n = " << setw(10) << n
             << "  |  sum = " << setw(15) << total
             << "  |  time = " << fixed << setprecision(6) << elapsed << "s" << endl;
    }
    cout << endl;
}

// =====================================================================
// 3. O(n^2) — Quadratic time (nested loops)
// =====================================================================
// For each number i from 1 to n, we add 1 exactly i times using
// an inner loop.  Intentionally slow to show the effect.
// Double n, and the time roughly quadruples.

void demo_quadratic() {
    cout << "=== PART 3: O(n^2) -- Nested Loops ===" << endl;

    int sizes[] = {1000, 5000, 10000};
    for (int n : sizes) {
        auto start = chrono::high_resolution_clock::now();
        long long total = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                total += 1;
            }
        }
        auto end = chrono::high_resolution_clock::now();
        double elapsed = chrono::duration<double>(end - start).count();
        cout << "  n = " << setw(6) << n
             << "  |  sum = " << setw(12) << total
             << "  |  time = " << fixed << setprecision(6) << elapsed << "s" << endl;
    }
    cout << endl;
}

// =====================================================================
// 4. O(log n) — Logarithmic time (halving)
// =====================================================================
// Repeatedly halving a number reaches 0 in about log2(n) steps.
// Even for n = 1 billion, that's only about 30 steps!

void demo_logarithmic() {
    cout << "=== PART 4: O(log n) -- Halving ===" << endl;

    long long sizes[] = {1000, 1000000, 1000000000};
    for (long long n : sizes) {
        auto start = chrono::high_resolution_clock::now();
        int steps = 0;
        long long val = n;
        while (val > 0) {
            val /= 2;
            steps++;
        }
        auto end = chrono::high_resolution_clock::now();
        double elapsed = chrono::duration<double>(end - start).count();
        cout << "  n = " << setw(13) << n
             << "  |  steps = " << setw(3) << steps
             << "  |  time = " << fixed << setprecision(6) << elapsed << "s" << endl;
    }
    cout << endl;
}

// =====================================================================
// main — run all the demos
// =====================================================================
int main() {
    demo_constant();
    demo_linear();
    demo_quadratic();
    demo_logarithmic();

    cout << "Notice how O(1) and O(log n) are nearly instant for ANY n," << endl;
    cout << "while O(n^2) gets painful fast.  That's why complexity matters!" << endl;
    return 0;
}
