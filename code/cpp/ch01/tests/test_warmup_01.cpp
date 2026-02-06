/*
 * Tests for Warmup 01: Sum of Two Numbers
 * ========================================
 * Chapter 1: The Coder's Toolkit
 *
 * This file tests the solve() function from the solution file.
 * We include the solution directly so the tests can call solve().
 *
 * Build and run:
 *   cd code/cpp
 *   make test-ch01
 *
 * Or manually:
 *   g++ -std=c++17 -o test_warmup_01 ch01/tests/test_warmup_01.cpp
 *   ./test_warmup_01
 */

#include <cassert>
#include <iostream>
using namespace std;

// ── We define solve() here so students can paste their implementation ──
// When the student is ready, they replace the body of this function
// with their own solution from warmup_01_sum.cpp.
//
// For automated testing via `make test-ch01`, this file is self-contained.

int solve(int a, int b) {
    // Reference solution for testing
    return a + b;
}

// ── Test cases ─────────────────────────────────────────────────────────

void test_sum_positive() {
    assert(solve(1, 2) == 3);
    cout << "  test_sum_positive............ PASS" << endl;
}

void test_sum_zeros() {
    assert(solve(0, 0) == 0);
    cout << "  test_sum_zeros............... PASS" << endl;
}

void test_sum_negative_positive() {
    assert(solve(-5, 5) == 0);
    cout << "  test_sum_negative_positive... PASS" << endl;
}

void test_sum_large() {
    assert(solve(1000000, 2000000) == 3000000);
    cout << "  test_sum_large............... PASS" << endl;
}

void test_sum_negatives() {
    assert(solve(-100, -200) == -300);
    cout << "  test_sum_negatives........... PASS" << endl;
}

// ── Runner ─────────────────────────────────────────────────────────────

int main() {
    cout << "=== Warmup 01: Sum of Two Numbers ===" << endl;

    test_sum_positive();
    test_sum_zeros();
    test_sum_negative_positive();
    test_sum_large();
    test_sum_negatives();

    cout << endl;
    cout << "All tests passed!" << endl;
    return 0;
}
