/*
 * Tests for Chapter 2: Your First Programs
 * ==========================================
 * Chapter 2: Your First Programs — Speaking Three Languages
 *
 * This file tests all 10 problems from Chapter 2.
 * Each problem has its own solve function (with a unique name to avoid
 * conflicts) and a set of assert-based tests.
 *
 * Build and run:
 *   g++ -std=c++17 -o test_ch02 code/cpp/ch02/tests/test_ch02.cpp && ./test_ch02
 *
 * Or from the ch02/tests directory:
 *   g++ -std=c++17 -o test_ch02 test_ch02.cpp && ./test_ch02
 */

#include <cassert>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <tuple>
#include <utility>
using namespace std;

// ── Helper: compare doubles with tolerance ──────────────────────────
bool approx(double a, double b, double eps = 1e-6) {
    return fabs(a - b) < eps;
}

// ═══════════════════════════════════════════════════════════════════════
// Reference solutions (one per problem, uniquely named)
// ═══════════════════════════════════════════════════════════════════════

// Warmup 01: Greeting
string solve_greeting(string name) {
    return "Hello, " + name + "!";
}

// Warmup 02: Rectangle Area
int solve_rectangle_area(int length, int width) {
    return length * width;
}

// Warmup 03: Celsius to Fahrenheit
double solve_celsius_to_fahrenheit(double celsius) {
    return celsius * 9.0 / 5.0 + 32.0;
}

// Warmup 04: Swap
pair<int, int> solve_swap(int a, int b) {
    return {b, a};
}

// Warmup 05: Last Digit
int solve_last_digit(int n) {
    return abs(n) % 10;
}

// Practice 01: Circle Properties
pair<double, double> solve_circle(double radius) {
    double area = M_PI * radius * radius;
    double circumference = 2.0 * M_PI * radius;
    return {area, circumference};
}

// Practice 02: Time Conversion
tuple<int, int, int> solve_time_conversion(int totalSeconds) {
    int h = totalSeconds / 3600;
    int m = (totalSeconds % 3600) / 60;
    int s = totalSeconds % 60;
    return {h, m, s};
}

// Practice 03: Distance Between Points
double solve_distance(double x1, double y1, double x2, double y2) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    return sqrt(dx * dx + dy * dy);
}

// Challenge 01: Extract Digits
tuple<int, int, int> solve_extract_digits(int n) {
    int hundreds = n / 100;
    int tens = (n / 10) % 10;
    int ones = n % 10;
    return {hundreds, tens, ones};
}

// Challenge 02: Quadratic Discriminant
pair<double, int> solve_quadratic(double a, double b, double c) {
    double disc = b * b - 4.0 * a * c;
    int numRoots;
    if (disc > 0) {
        numRoots = 2;
    } else if (disc == 0) {
        numRoots = 1;
    } else {
        numRoots = 0;
    }
    return {disc, numRoots};
}

// ═══════════════════════════════════════════════════════════════════════
// Test functions
// ═══════════════════════════════════════════════════════════════════════

void test_warmup_01_greeting() {
    assert(solve_greeting("Maya") == "Hello, Maya!");
    assert(solve_greeting("World") == "Hello, World!");
    assert(solve_greeting("Captain Hook") == "Hello, Captain Hook!");
    assert(solve_greeting("A") == "Hello, A!");
    cout << "  test_warmup_01_greeting.............. PASS" << endl;
}

void test_warmup_02_rectangle_area() {
    assert(solve_rectangle_area(5, 3) == 15);
    assert(solve_rectangle_area(10, 10) == 100);
    assert(solve_rectangle_area(1, 1) == 1);
    assert(solve_rectangle_area(100, 200) == 20000);
    cout << "  test_warmup_02_rectangle_area........ PASS" << endl;
}

void test_warmup_03_celsius_to_fahrenheit() {
    assert(approx(solve_celsius_to_fahrenheit(0), 32.0));
    assert(approx(solve_celsius_to_fahrenheit(100), 212.0));
    assert(approx(solve_celsius_to_fahrenheit(-40), -40.0));
    assert(approx(solve_celsius_to_fahrenheit(37), 98.6));
    cout << "  test_warmup_03_celsius_to_fahrenheit. PASS" << endl;
}

void test_warmup_04_swap() {
    assert(solve_swap(3, 7) == make_pair(7, 3));
    assert(solve_swap(0, 0) == make_pair(0, 0));
    assert(solve_swap(-1, 5) == make_pair(5, -1));
    assert(solve_swap(42, 42) == make_pair(42, 42));
    cout << "  test_warmup_04_swap.................. PASS" << endl;
}

void test_warmup_05_last_digit() {
    assert(solve_last_digit(123) == 3);
    assert(solve_last_digit(-456) == 6);
    assert(solve_last_digit(0) == 0);
    assert(solve_last_digit(10) == 0);
    assert(solve_last_digit(-7) == 7);
    cout << "  test_warmup_05_last_digit............ PASS" << endl;
}

void test_practice_01_circle() {
    auto [area1, circ1] = solve_circle(1.0);
    assert(approx(area1, M_PI));
    assert(approx(circ1, 2.0 * M_PI));

    auto [area5, circ5] = solve_circle(5.0);
    assert(approx(area5, 25.0 * M_PI));
    assert(approx(circ5, 10.0 * M_PI));

    auto [area10, circ10] = solve_circle(10.0);
    assert(approx(area10, 100.0 * M_PI));
    assert(approx(circ10, 20.0 * M_PI));
    cout << "  test_practice_01_circle.............. PASS" << endl;
}

void test_practice_02_time_conversion() {
    assert(solve_time_conversion(3661) == make_tuple(1, 1, 1));
    assert(solve_time_conversion(0) == make_tuple(0, 0, 0));
    assert(solve_time_conversion(7200) == make_tuple(2, 0, 0));
    assert(solve_time_conversion(90) == make_tuple(0, 1, 30));
    assert(solve_time_conversion(86399) == make_tuple(23, 59, 59));
    cout << "  test_practice_02_time_conversion..... PASS" << endl;
}

void test_practice_03_distance() {
    assert(approx(solve_distance(0, 0, 3, 4), 5.0));
    assert(approx(solve_distance(1, 1, 1, 1), 0.0));
    assert(approx(solve_distance(0, 0, 1, 1), sqrt(2.0)));
    assert(approx(solve_distance(-1, -1, 2, 3), 5.0));
    cout << "  test_practice_03_distance............ PASS" << endl;
}

void test_challenge_01_extract_digits() {
    assert(solve_extract_digits(123) == make_tuple(1, 2, 3));
    assert(solve_extract_digits(905) == make_tuple(9, 0, 5));
    assert(solve_extract_digits(100) == make_tuple(1, 0, 0));
    assert(solve_extract_digits(999) == make_tuple(9, 9, 9));
    cout << "  test_challenge_01_extract_digits..... PASS" << endl;
}

void test_challenge_02_quadratic() {
    // 1x^2 - 3x + 2 = 0 => disc = 1, 2 roots
    auto [disc1, nr1] = solve_quadratic(1, -3, 2);
    assert(approx(disc1, 1.0));
    assert(nr1 == 2);

    // 1x^2 + 2x + 1 = 0 => disc = 0, 1 root
    auto [disc2, nr2] = solve_quadratic(1, 2, 1);
    assert(approx(disc2, 0.0));
    assert(nr2 == 1);

    // 1x^2 + 0x + 1 = 0 => disc = -4, 0 roots
    auto [disc3, nr3] = solve_quadratic(1, 0, 1);
    assert(approx(disc3, -4.0));
    assert(nr3 == 0);

    // 2x^2 + 5x - 3 = 0 => disc = 25 + 24 = 49, 2 roots
    auto [disc4, nr4] = solve_quadratic(2, 5, -3);
    assert(approx(disc4, 49.0));
    assert(nr4 == 2);
    cout << "  test_challenge_02_quadratic.......... PASS" << endl;
}

// ═══════════════════════════════════════════════════════════════════════
// Runner
// ═══════════════════════════════════════════════════════════════════════

int main() {
    cout << "=== Chapter 2: Your First Programs ===" << endl;
    cout << endl;

    cout << "--- Warmup Problems ---" << endl;
    test_warmup_01_greeting();
    test_warmup_02_rectangle_area();
    test_warmup_03_celsius_to_fahrenheit();
    test_warmup_04_swap();
    test_warmup_05_last_digit();
    cout << endl;

    cout << "--- Practice Problems ---" << endl;
    test_practice_01_circle();
    test_practice_02_time_conversion();
    test_practice_03_distance();
    cout << endl;

    cout << "--- Challenge Problems ---" << endl;
    test_challenge_01_extract_digits();
    test_challenge_02_quadratic();
    cout << endl;

    cout << "All Chapter 2 tests passed!" << endl;
    return 0;
}
