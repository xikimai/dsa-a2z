/*
 * Example 01: Basic Functions
 * ===========================
 * Chapter 4: Functions
 *
 * This file walks through the fundamentals of C++ functions:
 *   1. Basic function definition and calling
 *   2. Multiple parameters
 *   3. Return values
 *   4. Default parameters
 *   5. A function calling another function
 *
 * Build & run:
 *   g++ -std=c++17 -o example_01 code/cpp/ch04/learn/example_01_basic_functions.cpp && ./example_01
 */

#include <iostream>
#include <string>
using namespace std;

// ═══════════════════════════════════════════════════════════════════
// 1. Basic function definition
// ═══════════════════════════════════════════════════════════════════
// A function has: return type, name, parameters, and a body.
// 'void' means the function doesn't return anything.

void say_hello() {
    cout << "Hello from a function!" << endl;
}

// ═══════════════════════════════════════════════════════════════════
// 2. Multiple parameters
// ═══════════════════════════════════════════════════════════════════
// You can pass multiple values into a function.
// Each parameter needs its own type declaration.

void introduce(string name, int age) {
    cout << "Hi, I'm " << name << " and I'm " << age << " years old." << endl;
}

// ═══════════════════════════════════════════════════════════════════
// 3. Return values
// ═══════════════════════════════════════════════════════════════════
// Instead of 'void', specify the type of the value you want to return.
// The 'return' statement sends a value back to the caller.

int add(int a, int b) {
    return a + b;
}

double divide(double a, double b) {
    // Always think about edge cases!
    if (b == 0) {
        cout << "  Warning: division by zero!" << endl;
        return 0.0;
    }
    return a / b;
}

// ═══════════════════════════════════════════════════════════════════
// 4. Default parameters
// ═══════════════════════════════════════════════════════════════════
// You can give parameters default values. If the caller doesn't
// provide them, the default kicks in. Defaults go at the END of
// the parameter list.

string greet(string name, string greeting = "Hello") {
    return greeting + ", " + name + "!";
}

// You can have multiple defaults:
void print_box(string text, int width = 20, char border = '*') {
    string line(width, border);
    cout << line << endl;
    cout << border << " " << text;
    // Pad the rest
    int padding = width - 3 - (int)text.size();
    if (padding > 0) {
        cout << string(padding, ' ');
    }
    cout << border << endl;
    cout << line << endl;
}

// ═══════════════════════════════════════════════════════════════════
// 5. A function calling another function
// ═══════════════════════════════════════════════════════════════════
// Functions can call other functions. This is how you build
// complex programs from small, reusable pieces.

int square(int n) {
    return n * n;
}

int sum_of_squares(int a, int b) {
    // Reuses square() instead of duplicating the logic
    return square(a) + square(b);
}

// A more practical example: computing the distance between two points
double distance(double x1, double y1, double x2, double y2) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    // sqrt lives in <cmath>, but we can compute it with this trick:
    // or just include <cmath> — we'll keep it simple here.
    return sqrt(dx * dx + dy * dy);
}

// ═══════════════════════════════════════════════════════════════════
// main — run all the demos
// ═══════════════════════════════════════════════════════════════════
int main() {
    cout << "=== 1. Basic function ===" << endl;
    say_hello();
    cout << endl;

    cout << "=== 2. Multiple parameters ===" << endl;
    introduce("Maya", 14);
    introduce("Alex", 15);
    cout << endl;

    cout << "=== 3. Return values ===" << endl;
    int sum = add(3, 7);
    cout << "  add(3, 7) = " << sum << endl;
    cout << "  divide(10, 3) = " << divide(10, 3) << endl;
    cout << "  divide(5, 0) = " << divide(5, 0) << endl;
    cout << endl;

    cout << "=== 4. Default parameters ===" << endl;
    cout << "  " << greet("Maya") << endl;              // Uses default "Hello"
    cout << "  " << greet("Maya", "Hey") << endl;       // Overrides default
    cout << "  " << greet("Sensei", "Konnichiwa") << endl;
    cout << endl;
    cout << "  Box with all defaults:" << endl;
    print_box("Hi!");
    cout << endl;
    cout << "  Box with custom width:" << endl;
    print_box("Hi!", 30);
    cout << endl;
    cout << "  Box with custom width and border:" << endl;
    print_box("Hi!", 30, '#');
    cout << endl;

    cout << "=== 5. Function calling function ===" << endl;
    cout << "  square(5) = " << square(5) << endl;
    cout << "  sum_of_squares(3, 4) = " << sum_of_squares(3, 4) << endl;
    cout << "  distance(0,0, 3,4) = " << distance(0, 0, 3, 4) << endl;
    cout << endl;

    cout << "All examples done!" << endl;
    return 0;
}
