/*
 * Example 02: Loops and Patterns
 * ==============================
 * Chapter 3: Decisions and Loops
 *
 * This file shows you for loops, while loops, nested loops, break/continue,
 * and how to print simple patterns. These are the building blocks for
 * competitive programming!
 *
 * Build and run:
 *   g++ -std=c++17 -o example_02 example_02_loops_patterns.cpp && ./example_02
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    // ── 1. for loop ───────────────────────────────────────────────────────
    cout << "=== for loop ===" << endl;

    // Count from 1 to 5:
    for (int i = 1; i <= 5; i++) {
        cout << i << " ";
    }
    cout << endl;

    // Count from 10 down to 1:
    for (int i = 10; i >= 1; i--) {
        cout << i << " ";
    }
    cout << endl;

    // Step by 2:
    for (int i = 0; i <= 10; i += 2) {
        cout << i << " ";
    }
    cout << endl;
    cout << endl;

    // ── 2. while loop ────────────────────────────────────────────────────
    cout << "=== while loop ===" << endl;

    // while is best when you don't know how many iterations upfront.
    int num = 12345;
    cout << "Digits of " << num << " (reversed): ";
    while (num > 0) {
        cout << num % 10 << " ";
        num /= 10;
    }
    cout << endl;

    // do-while: always runs at least once.
    int count = 0;
    do {
        count++;
    } while (count < 0);  // condition is false, but body ran once!
    cout << "do-while ran " << count << " time(s)" << endl;
    cout << endl;

    // ── 3. break and continue ─────────────────────────────────────────────
    cout << "=== break and continue ===" << endl;

    // break: exit the loop immediately
    cout << "First multiple of 7 after 50: ";
    for (int i = 51; ; i++) {  // infinite loop — break will stop it
        if (i % 7 == 0) {
            cout << i << endl;
            break;
        }
    }

    // continue: skip the rest of this iteration, go to the next one
    cout << "Odd numbers from 1-10: ";
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) continue;  // skip even numbers
        cout << i << " ";
    }
    cout << endl;
    cout << endl;

    // ── 4. Nested loops ──────────────────────────────────────────────────
    cout << "=== Nested Loops ===" << endl;

    // Multiplication table (3x3):
    cout << "3x3 multiplication table:" << endl;
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            cout << i * j << "\t";
        }
        cout << endl;
    }
    cout << endl;

    // ── 5. Pattern: Right triangle of stars ───────────────────────────────
    cout << "=== Pattern: Right Triangle (left-aligned) ===" << endl;
    int n = 5;
    for (int row = 1; row <= n; row++) {
        for (int col = 1; col <= row; col++) {
            cout << "*";
        }
        cout << endl;
    }
    cout << endl;

    // ── 6. Pattern: Right triangle (right-aligned) ────────────────────────
    cout << "=== Pattern: Right Triangle (right-aligned) ===" << endl;
    for (int row = 1; row <= n; row++) {
        // Print spaces first, then stars
        for (int s = 1; s <= n - row; s++) {
            cout << " ";
        }
        for (int col = 1; col <= row; col++) {
            cout << "*";
        }
        cout << endl;
    }
    cout << endl;

    // ── 7. Pattern: Number pyramid ────────────────────────────────────────
    cout << "=== Pattern: Number Triangle ===" << endl;
    for (int row = 1; row <= n; row++) {
        for (int col = 1; col <= row; col++) {
            cout << col;
        }
        cout << endl;
    }
    cout << endl;

    // ── 8. Building strings in loops ──────────────────────────────────────
    cout << "=== Building Strings ===" << endl;

    // Instead of printing directly, you can build a string:
    string stars = "";
    for (int i = 0; i < 10; i++) {
        stars += "*";
    }
    cout << "10 stars: " << stars << endl;

    // Building a vector in a loop:
    vector<int> squares;
    for (int i = 1; i <= 5; i++) {
        squares.push_back(i * i);
    }
    cout << "Squares: ";
    for (int val : squares) {  // range-based for loop (C++11)
        cout << val << " ";
    }
    cout << endl;
    cout << endl;

    // ── 9. Common loop pitfalls ───────────────────────────────────────────
    cout << "=== Common Pitfalls ===" << endl;
    cout << "1. Off-by-one: 'i < n' gives 0..n-1 (n items)." << endl;
    cout << "   'i <= n' gives 0..n (n+1 items)." << endl;
    cout << "2. Infinite loop: forgetting to update the loop variable." << endl;
    cout << "3. Integer overflow: looping up to a huge number without long long." << endl;
    cout << "4. Modifying the loop variable inside the body (usually a bug)." << endl;
    cout << endl;

    cout << "Done! You've learned C++ loops and patterns." << endl;
    return 0;
}
