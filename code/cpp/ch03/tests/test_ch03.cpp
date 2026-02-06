/*
 * Tests for Chapter 3: Decisions and Loops
 * ==========================================
 * Chapter 3: Decisions and Loops
 *
 * This file tests all 13 problems from Chapter 3.
 * Each problem has its own solve function (with a unique name to avoid
 * conflicts) and a set of assert-based tests.
 *
 * Build and run:
 *   g++ -std=c++17 -o test_ch03 code/cpp/ch03/tests/test_ch03.cpp && ./test_ch03
 *
 * Or from the ch03/tests directory:
 *   g++ -std=c++17 -o test_ch03 test_ch03.cpp && ./test_ch03
 */

#include <cassert>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// ═══════════════════════════════════════════════════════════════════════
// Reference solutions (one per problem, uniquely named)
// ═══════════════════════════════════════════════════════════════════════

// Warmup 01: Even or Odd
string solve_even_odd(int n) {
    return (n % 2 == 0) ? "Even" : "Odd";
}

// Warmup 02: Absolute Value
int solve_absolute_value(int n) {
    if (n < 0) return -n;
    return n;
}

// Warmup 03: Largest of Three
int solve_largest_of_three(int a, int b, int c) {
    int largest = a;
    if (b > largest) largest = b;
    if (c > largest) largest = c;
    return largest;
}

// Warmup 04: Count Down
vector<int> solve_count_down(int n) {
    vector<int> result;
    for (int i = n; i >= 1; i--) {
        result.push_back(i);
    }
    return result;
}

// Warmup 05: Sum 1 to N
int solve_sum_1_to_n(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

// Warmup 06: Multiplication Table
vector<string> solve_multiplication_table(int n) {
    vector<string> result;
    for (int i = 1; i <= 10; i++) {
        result.push_back(to_string(i) + " x " + to_string(n) + " = " + to_string(i * n));
    }
    return result;
}

// Practice 01: FizzBuzz
vector<string> solve_fizzbuzz(int n) {
    vector<string> result;
    for (int i = 1; i <= n; i++) {
        if (i % 15 == 0) {
            result.push_back("FizzBuzz");
        } else if (i % 3 == 0) {
            result.push_back("Fizz");
        } else if (i % 5 == 0) {
            result.push_back("Buzz");
        } else {
            result.push_back(to_string(i));
        }
    }
    return result;
}

// Practice 02: Digit Count
int solve_digit_count(int n) {
    if (n == 0) return 1;
    if (n < 0) n = -n;
    int count = 0;
    while (n > 0) {
        n /= 10;
        count++;
    }
    return count;
}

// Practice 03: Reverse Number
int solve_reverse_number(int n) {
    int sign = 1;
    if (n < 0) {
        sign = -1;
        n = -n;
    }
    int reversed = 0;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    return sign * reversed;
}

// Practice 04: Right Triangle
string solve_right_triangle(int n) {
    string result;
    for (int i = 1; i <= n; i++) {
        if (i > 1) result += "\n";
        result += string(n - i, ' ') + string(i, '*');
    }
    return result;
}

// Challenge 01: Diamond
string solve_diamond(int n) {
    string result;
    int totalRows = 2 * n - 1;
    for (int row = 1; row <= totalRows; row++) {
        if (row > 1) result += "\n";
        int i = (row <= n) ? row : (2 * n - row);
        int spaces = n - i;
        int stars = 2 * i - 1;
        result += string(spaces, ' ') + string(stars, '*');
    }
    return result;
}

// Challenge 02: Prime Check
bool solve_prime_check(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; (long long)i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

// Challenge 03: Collatz Sequence
vector<int> solve_collatz(int n) {
    vector<int> sequence;
    sequence.push_back(n);
    while (n != 1) {
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
        sequence.push_back(n);
    }
    return sequence;
}

// ═══════════════════════════════════════════════════════════════════════
// Test functions
// ═══════════════════════════════════════════════════════════════════════

void test_warmup_01_even_odd() {
    assert(solve_even_odd(4) == "Even");
    assert(solve_even_odd(7) == "Odd");
    assert(solve_even_odd(0) == "Even");
    assert(solve_even_odd(-3) == "Odd");
    assert(solve_even_odd(1) == "Odd");
    cout << "  test_warmup_01_even_odd.............. PASS" << endl;
}

void test_warmup_02_absolute_value() {
    assert(solve_absolute_value(5) == 5);
    assert(solve_absolute_value(-5) == 5);
    assert(solve_absolute_value(0) == 0);
    assert(solve_absolute_value(-100) == 100);
    assert(solve_absolute_value(1) == 1);
    cout << "  test_warmup_02_absolute_value........ PASS" << endl;
}

void test_warmup_03_largest_of_three() {
    assert(solve_largest_of_three(1, 2, 3) == 3);
    assert(solve_largest_of_three(3, 2, 1) == 3);
    assert(solve_largest_of_three(5, 5, 5) == 5);
    assert(solve_largest_of_three(-1, -2, -3) == -1);
    cout << "  test_warmup_03_largest_of_three...... PASS" << endl;
}

void test_warmup_04_count_down() {
    assert((solve_count_down(5) == vector<int>{5, 4, 3, 2, 1}));
    assert((solve_count_down(1) == vector<int>{1}));
    assert((solve_count_down(3) == vector<int>{3, 2, 1}));
    cout << "  test_warmup_04_count_down............ PASS" << endl;
}

void test_warmup_05_sum_1_to_n() {
    assert(solve_sum_1_to_n(5) == 15);
    assert(solve_sum_1_to_n(1) == 1);
    assert(solve_sum_1_to_n(10) == 55);
    assert(solve_sum_1_to_n(100) == 5050);
    assert(solve_sum_1_to_n(0) == 0);
    cout << "  test_warmup_05_sum_1_to_n............ PASS" << endl;
}

void test_warmup_06_multiplication_table() {
    vector<string> table7 = solve_multiplication_table(7);
    assert(table7.size() == 10);
    assert(table7[0] == "1 x 7 = 7");
    assert(table7[1] == "2 x 7 = 14");
    assert(table7[9] == "10 x 7 = 70");

    vector<string> table1 = solve_multiplication_table(1);
    assert(table1.size() == 10);
    assert(table1[0] == "1 x 1 = 1");
    assert(table1[9] == "10 x 1 = 10");
    cout << "  test_warmup_06_multiplication_table.. PASS" << endl;
}

void test_practice_01_fizzbuzz() {
    vector<string> fb15 = solve_fizzbuzz(15);
    assert(fb15.size() == 15);
    assert(fb15[0] == "1");
    assert(fb15[1] == "2");
    assert(fb15[2] == "Fizz");     // 3
    assert(fb15[4] == "Buzz");     // 5
    assert(fb15[14] == "FizzBuzz"); // 15

    vector<string> fb1 = solve_fizzbuzz(1);
    assert(fb1.size() == 1);
    assert(fb1[0] == "1");
    cout << "  test_practice_01_fizzbuzz............ PASS" << endl;
}

void test_practice_02_digit_count() {
    assert(solve_digit_count(12345) == 5);
    assert(solve_digit_count(0) == 1);
    assert(solve_digit_count(9) == 1);
    assert(solve_digit_count(-42) == 2);
    assert(solve_digit_count(1000000) == 7);
    cout << "  test_practice_02_digit_count......... PASS" << endl;
}

void test_practice_03_reverse_number() {
    assert(solve_reverse_number(1234) == 4321);
    assert(solve_reverse_number(1200) == 21);
    assert(solve_reverse_number(5) == 5);
    assert(solve_reverse_number(-123) == -321);
    assert(solve_reverse_number(0) == 0);
    cout << "  test_practice_03_reverse_number...... PASS" << endl;
}

void test_practice_04_right_triangle() {
    assert(solve_right_triangle(1) == "*");
    assert(solve_right_triangle(3) == "  *\n **\n***");
    assert(solve_right_triangle(4) == "   *\n  **\n ***\n****");
    cout << "  test_practice_04_right_triangle...... PASS" << endl;
}

void test_challenge_01_diamond() {
    assert(solve_diamond(1) == "*");
    assert(solve_diamond(2) == " *\n***\n *");

    string d3 = solve_diamond(3);
    // 5 lines: "  *", " ***", "*****", " ***", "  *"
    assert(d3 == "  *\n ***\n*****\n ***\n  *");
    cout << "  test_challenge_01_diamond............ PASS" << endl;
}

void test_challenge_02_prime_check() {
    assert(solve_prime_check(2) == true);
    assert(solve_prime_check(3) == true);
    assert(solve_prime_check(4) == false);
    assert(solve_prime_check(1) == false);
    assert(solve_prime_check(0) == false);
    assert(solve_prime_check(17) == true);
    assert(solve_prime_check(25) == false);
    assert(solve_prime_check(97) == true);
    assert(solve_prime_check(-5) == false);
    cout << "  test_challenge_02_prime_check........ PASS" << endl;
}

void test_challenge_03_collatz() {
    assert((solve_collatz(6) == vector<int>{6, 3, 10, 5, 16, 8, 4, 2, 1}));
    assert((solve_collatz(1) == vector<int>{1}));
    assert((solve_collatz(2) == vector<int>{2, 1}));
    cout << "  test_challenge_03_collatz............ PASS" << endl;
}

// ═══════════════════════════════════════════════════════════════════════
// Runner
// ═══════════════════════════════════════════════════════════════════════

int main() {
    cout << "=== Chapter 3: Decisions and Loops ===" << endl;
    cout << endl;

    cout << "--- Warmup Problems ---" << endl;
    test_warmup_01_even_odd();
    test_warmup_02_absolute_value();
    test_warmup_03_largest_of_three();
    test_warmup_04_count_down();
    test_warmup_05_sum_1_to_n();
    test_warmup_06_multiplication_table();
    cout << endl;

    cout << "--- Practice Problems ---" << endl;
    test_practice_01_fizzbuzz();
    test_practice_02_digit_count();
    test_practice_03_reverse_number();
    test_practice_04_right_triangle();
    cout << endl;

    cout << "--- Challenge Problems ---" << endl;
    test_challenge_01_diamond();
    test_challenge_02_prime_check();
    test_challenge_03_collatz();
    cout << endl;

    cout << "All Chapter 3 tests passed!" << endl;
    return 0;
}
