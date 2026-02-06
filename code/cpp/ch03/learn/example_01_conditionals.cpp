/*
 * Example 01: Conditionals
 * ========================
 * Chapter 3: Decisions and Loops
 *
 * This file shows you how to make decisions in C++ using if/else,
 * the ternary operator, switch statements, and logical operators.
 * Run this file and study the output to understand how each works.
 *
 * Build and run:
 *   g++ -std=c++17 -o example_01 example_01_conditionals.cpp && ./example_01
 */

#include <iostream>
#include <string>
using namespace std;

int main() {
    // ── 1. Basic if/else ──────────────────────────────────────────────────
    cout << "=== Basic if/else ===" << endl;

    int age = 14;
    if (age >= 18) {
        cout << "You can vote!" << endl;
    } else if (age >= 13) {
        cout << "You're a teenager." << endl;
    } else {
        cout << "You're a kid." << endl;
    }
    cout << endl;

    // ── 2. Comparison operators ───────────────────────────────────────────
    cout << "=== Comparison Operators ===" << endl;
    int a = 10, b = 20;
    cout << "a = " << a << ", b = " << b << endl;
    cout << "a == b: " << (a == b) << endl;   // 0 (false)
    cout << "a != b: " << (a != b) << endl;   // 1 (true)
    cout << "a < b:  " << (a < b) << endl;    // 1 (true)
    cout << "a >= b: " << (a >= b) << endl;   // 0 (false)
    cout << endl;

    // ── 3. Logical operators ──────────────────────────────────────────────
    cout << "=== Logical Operators ===" << endl;
    bool sunny = true;
    bool warm = false;

    cout << "sunny = " << boolalpha << sunny << ", warm = " << warm << endl;
    cout << "sunny && warm: " << (sunny && warm) << endl;  // false (AND)
    cout << "sunny || warm: " << (sunny || warm) << endl;  // true  (OR)
    cout << "!sunny:        " << (!sunny) << endl;         // false (NOT)
    cout << noboolalpha;

    // Short-circuit: C++ stops evaluating as soon as it knows the answer.
    // In (false && ...), the right side is never checked.
    // In (true || ...), the right side is never checked.
    cout << endl;

    // ── 4. Ternary operator ───────────────────────────────────────────────
    cout << "=== Ternary Operator ===" << endl;
    // condition ? value_if_true : value_if_false
    int score = 85;
    string grade = (score >= 90) ? "A" : (score >= 80) ? "B" : "C";
    cout << "Score " << score << " => Grade " << grade << endl;

    // The ternary is great for simple choices. For complex logic, use if/else.
    int x = 7;
    string parity = (x % 2 == 0) ? "even" : "odd";
    cout << x << " is " << parity << endl;
    cout << endl;

    // ── 5. switch statement ───────────────────────────────────────────────
    cout << "=== Switch Statement ===" << endl;
    // switch works with int, char, and enum types (not strings!).
    int dayNumber = 3;
    switch (dayNumber) {
        case 1:
            cout << "Monday" << endl;
            break;
        case 2:
            cout << "Tuesday" << endl;
            break;
        case 3:
            cout << "Wednesday" << endl;
            break;
        case 4:
            cout << "Thursday" << endl;
            break;
        case 5:
            cout << "Friday" << endl;
            break;
        default:
            cout << "Weekend!" << endl;
            break;
    }

    // Without 'break', execution falls through to the next case.
    // This is a common bug! Always include break unless you want fall-through.

    // switch with char:
    char letter = 'B';
    switch (letter) {
        case 'A':
            cout << "Excellent!" << endl;
            break;
        case 'B':
            cout << "Good job!" << endl;
            break;
        case 'C':
            cout << "Keep trying!" << endl;
            break;
        default:
            cout << "Unknown grade." << endl;
            break;
    }
    cout << endl;

    // ── 6. Nested if and common patterns ──────────────────────────────────
    cout << "=== Common Patterns ===" << endl;

    // Range checking:
    int temp = 72;
    if (temp < 32) {
        cout << "Freezing!" << endl;
    } else if (temp < 60) {
        cout << "Cold." << endl;
    } else if (temp < 80) {
        cout << "Nice." << endl;
    } else {
        cout << "Hot!" << endl;
    }

    // Checking multiple conditions:
    int n = 15;
    if (n % 3 == 0 && n % 5 == 0) {
        cout << n << " is divisible by both 3 and 5." << endl;
    } else if (n % 3 == 0) {
        cout << n << " is divisible by 3." << endl;
    } else if (n % 5 == 0) {
        cout << n << " is divisible by 5." << endl;
    }

    // Guard clause pattern (check bad input first):
    int divisor = 0;
    if (divisor == 0) {
        cout << "Cannot divide by zero!" << endl;
    } else {
        cout << "100 / " << divisor << " = " << 100 / divisor << endl;
    }
    cout << endl;

    cout << "Done! You've learned C++ conditionals." << endl;
    return 0;
}
