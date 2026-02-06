/*
 * Example 02: Advanced Functions
 * ==============================
 * Chapter 4: Functions
 *
 * This file covers more advanced function concepts in C++:
 *   1. Pass by value vs pass by reference
 *   2. Scope and shadowing
 *   3. Function overloading
 *   4. Lambda functions
 *
 * Build & run:
 *   g++ -std=c++17 -o example_02 code/cpp/ch04/learn/example_02_advanced_functions.cpp && ./example_02
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// ═══════════════════════════════════════════════════════════════════
// 1. Pass by value vs pass by reference
// ═══════════════════════════════════════════════════════════════════

// PASS BY VALUE: the function gets a COPY. The original is untouched.
void double_value(int n) {
    n = n * 2;
    cout << "  Inside double_value: n = " << n << endl;
}

// PASS BY REFERENCE: the '&' means we get the ACTUAL variable.
// Changes here affect the original.
void double_ref(int& n) {
    n = n * 2;
    cout << "  Inside double_ref: n = " << n << endl;
}

// With vectors, pass-by-value copies the ENTIRE vector (slow for big data).
void add_one_copy(vector<int> nums) {
    for (int& x : nums) {
        x += 1;
    }
    cout << "  Inside add_one_copy: [";
    for (int i = 0; i < (int)nums.size(); i++) {
        if (i > 0) cout << ", ";
        cout << nums[i];
    }
    cout << "]" << endl;
}

// Pass-by-reference modifies the original AND avoids the copy.
void add_one_ref(vector<int>& nums) {
    for (int& x : nums) {
        x += 1;
    }
    cout << "  Inside add_one_ref: [";
    for (int i = 0; i < (int)nums.size(); i++) {
        if (i > 0) cout << ", ";
        cout << nums[i];
    }
    cout << "]" << endl;
}

// CONST REFERENCE: "I promise not to modify it, but don't copy it either."
// This is the best practice for reading large objects.
void print_vector(const vector<int>& nums) {
    cout << "  [";
    for (int i = 0; i < (int)nums.size(); i++) {
        if (i > 0) cout << ", ";
        cout << nums[i];
    }
    cout << "]" << endl;
}

// ═══════════════════════════════════════════════════════════════════
// 2. Scope and shadowing
// ═══════════════════════════════════════════════════════════════════

int x = 100;  // Global variable

void scope_demo() {
    // This 'x' is LOCAL and SHADOWS the global 'x'.
    int x = 42;
    cout << "  Local x = " << x << endl;

    {
        // A new block creates a new scope.
        int x = 7;
        cout << "  Inner block x = " << x << endl;
    }

    // Back to the function-level x.
    cout << "  Back to local x = " << x << endl;
}

void scope_demo_no_shadow() {
    // No local 'x' defined, so this reads the global one.
    cout << "  Using global x = " << x << endl;
}

// ═══════════════════════════════════════════════════════════════════
// 3. Function overloading
// ═══════════════════════════════════════════════════════════════════
// C++ lets you have multiple functions with the SAME NAME as long as
// their parameter lists are different. The compiler picks the right
// one based on the arguments you pass.

double area(double radius) {
    // Area of a circle
    return 3.14159265358979 * radius * radius;
}

double area(double width, double height) {
    // Area of a rectangle
    return width * height;
}

double area(double a, double b, double c) {
    // Area of a triangle using Heron's formula
    double s = (a + b + c) / 2.0;
    return sqrt(s * (s - a) * (s - b) * (s - c));
}

// ═══════════════════════════════════════════════════════════════════
// 4. Lambda functions
// ═══════════════════════════════════════════════════════════════════
// Lambdas are small anonymous functions you can define inline.
// Syntax:  [capture](parameters) -> return_type { body }
// The return type is usually auto-deduced so you can omit -> type.

// ═══════════════════════════════════════════════════════════════════
// main — run all the demos
// ═══════════════════════════════════════════════════════════════════
int main() {
    // ── 1. Pass by value vs reference ────────────────────────────
    cout << "=== 1. Pass by value vs reference ===" << endl;

    cout << "\n  --- Integers ---" << endl;
    int num = 10;
    cout << "  Before double_value: num = " << num << endl;
    double_value(num);
    cout << "  After double_value:  num = " << num << "  (unchanged!)" << endl;

    cout << endl;
    cout << "  Before double_ref: num = " << num << endl;
    double_ref(num);
    cout << "  After double_ref:  num = " << num << "  (changed!)" << endl;

    cout << "\n  --- Vectors ---" << endl;
    vector<int> v1 = {1, 2, 3};
    cout << "  Before add_one_copy: ";
    print_vector(v1);
    add_one_copy(v1);
    cout << "  After add_one_copy:  ";
    print_vector(v1);  // Still {1, 2, 3}

    cout << endl;
    cout << "  Before add_one_ref: ";
    print_vector(v1);
    add_one_ref(v1);
    cout << "  After add_one_ref:  ";
    print_vector(v1);  // Now {2, 3, 4}

    cout << endl;

    // ── 2. Scope and shadowing ───────────────────────────────────
    cout << "=== 2. Scope and shadowing ===" << endl;
    cout << "  Global x = " << x << endl;
    scope_demo();
    scope_demo_no_shadow();
    cout << "  Global x is still = " << x << endl;
    cout << endl;

    // ── 3. Function overloading ──────────────────────────────────
    cout << "=== 3. Function overloading ===" << endl;
    cout << "  area(5.0)          = " << area(5.0) << "  (circle)" << endl;
    cout << "  area(4.0, 6.0)     = " << area(4.0, 6.0) << "  (rectangle)" << endl;
    cout << "  area(3.0, 4.0, 5.0) = " << area(3.0, 4.0, 5.0) << "  (triangle)" << endl;
    cout << endl;

    // ── 4. Lambda functions ──────────────────────────────────────
    cout << "=== 4. Lambda functions ===" << endl;

    // Basic lambda stored in a variable
    auto square = [](int n) { return n * n; };
    cout << "  square(7) = " << square(7) << endl;

    // Lambda with capture — [&] captures all local variables by reference
    int factor = 3;
    auto multiply = [&factor](int n) { return n * factor; };
    cout << "  multiply(5) with factor=3: " << multiply(5) << endl;
    factor = 10;
    cout << "  multiply(5) with factor=10: " << multiply(5) << endl;

    // Lambda with [=] captures all local variables by value (snapshot)
    int base = 100;
    auto add_to_base = [=](int n) { return base + n; };
    base = 999;  // Doesn't affect the lambda — it captured a copy
    cout << "  add_to_base(5) (base was 100 at capture): " << add_to_base(5) << endl;

    // Lambdas are great with algorithms
    cout << "\n  Using lambdas with algorithms:" << endl;
    vector<int> nums = {5, 2, 8, 1, 9, 3};
    cout << "  Original: ";
    print_vector(nums);

    // Sort ascending (default)
    sort(nums.begin(), nums.end());
    cout << "  Sorted ascending:  ";
    print_vector(nums);

    // Sort descending using a lambda comparator
    sort(nums.begin(), nums.end(), [](int a, int b) { return a > b; });
    cout << "  Sorted descending: ";
    print_vector(nums);

    // Filter with a lambda (using copy_if + back_inserter)
    vector<int> evens;
    copy_if(nums.begin(), nums.end(), back_inserter(evens),
            [](int n) { return n % 2 == 0; });
    cout << "  Even numbers only: ";
    print_vector(evens);

    cout << "\nAll examples done!" << endl;
    return 0;
}
