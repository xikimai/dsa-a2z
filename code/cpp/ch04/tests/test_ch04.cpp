/*
 * Tests for Chapter 4: Functions
 * Build: g++ -std=c++17 -o test_ch04 code/cpp/ch04/tests/test_ch04.cpp && ./test_ch04
 */

#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// ═══════════════════════════════════════════════════════════════════
// Reference solutions (uniquely named to avoid collisions)
// ═══════════════════════════════════════════════════════════════════

// --- Warmup 01: Greeting ---
string solve_greeting(string name) {
    return "Hello, " + name + "!";
}

// --- Warmup 02: Power ---
long long solve_power(int base, int exponent) {
    long long result = 1;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}

// --- Warmup 03: Min of Three ---
int min_of_two(int a, int b) {
    return (a < b) ? a : b;
}

int solve_min_of_three(int a, int b, int c) {
    return min_of_two(a, min_of_two(b, c));
}

// --- Warmup 04: Repeat String ---
string solve_repeat(string s, int n = 3) {
    if (n <= 0) return "";
    string result = "";
    for (int i = 0; i < n; i++) {
        if (i > 0) result += " ";
        result += s;
    }
    return result;
}

// --- Warmup 05: Double List ---
vector<int> solve_double_list(vector<int>& nums) {
    for (int i = 0; i < (int)nums.size(); i++) {
        nums[i] *= 2;
    }
    return nums;
}

// --- Practice 01: Calculator ---
int calc_add(int a, int b) { return a + b; }
int calc_subtract(int a, int b) { return a - b; }
int calc_multiply(int a, int b) { return a * b; }
int calc_divide(int a, int b) { return a / b; }

bool solve_calc_valid(int a, string op, int b) {
    if (op == "add" || op == "subtract" || op == "multiply") return true;
    if (op == "divide" && b != 0) return true;
    return false;
}

int solve_calc(int a, string op, int b) {
    if (!solve_calc_valid(a, op, b)) return 0;
    if (op == "add") return calc_add(a, b);
    if (op == "subtract") return calc_subtract(a, b);
    if (op == "multiply") return calc_multiply(a, b);
    if (op == "divide") return calc_divide(a, b);
    return 0;
}

// --- Practice 02: Password Strength ---
bool pw_has_digit(string s) {
    for (char c : s) {
        if (c >= '0' && c <= '9') return true;
    }
    return false;
}

bool pw_has_upper(string s) {
    for (char c : s) {
        if (c >= 'A' && c <= 'Z') return true;
    }
    return false;
}

string solve_password(string password) {
    if ((int)password.length() < 8) return "weak";
    if (pw_has_digit(password) && pw_has_upper(password)) return "strong";
    return "medium";
}

// --- Practice 03: Temperature ---
double temp_c_to_f(double c) { return c * 9.0 / 5.0 + 32.0; }
double temp_f_to_c(double f) { return (f - 32.0) * 5.0 / 9.0; }
double temp_c_to_k(double c) { return c + 273.15; }
double temp_k_to_c(double k) { return k - 273.15; }

double solve_temp(double value, string from_unit, string to_unit) {
    if (from_unit != "C" && from_unit != "F" && from_unit != "K") return -1.0;
    if (to_unit != "C" && to_unit != "F" && to_unit != "K") return -1.0;
    if (from_unit == to_unit) return round(value * 10.0) / 10.0;

    double celsius = value;
    if (from_unit == "F") celsius = temp_f_to_c(value);
    if (from_unit == "K") celsius = temp_k_to_c(value);

    double result = celsius;
    if (to_unit == "F") result = temp_c_to_f(celsius);
    if (to_unit == "K") result = temp_c_to_k(celsius);

    return round(result * 10.0) / 10.0;
}

// --- Practice 04: Stats ---
int stats_find_min(vector<int>& nums) {
    int result = nums[0];
    for (int i = 1; i < (int)nums.size(); i++) {
        if (nums[i] < result) result = nums[i];
    }
    return result;
}

int stats_find_max(vector<int>& nums) {
    int result = nums[0];
    for (int i = 1; i < (int)nums.size(); i++) {
        if (nums[i] > result) result = nums[i];
    }
    return result;
}

double stats_find_average(vector<int>& nums) {
    double sum = 0;
    for (int val : nums) sum += val;
    return sum / nums.size();
}

vector<double> solve_stats(vector<int> nums) {
    if (nums.empty()) return {};
    double mn = (double)stats_find_min(nums);
    double mx = (double)stats_find_max(nums);
    double avg = round(stats_find_average(nums) * 100.0) / 100.0;
    return {mn, mx, avg};
}

// --- Challenge 01: Prime Check ---
bool is_prime_v3(int n) {
    if (n < 2) return false;
    if (n < 4) return true;
    if (n % 2 == 0) return false;
    if (n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0) return false;
        if (n % (i + 2) == 0) return false;
    }
    return true;
}

bool solve_prime(int n) {
    return is_prime_v3(n);
}

// --- Challenge 02: Apply Operations ---
void ref_op_double(vector<int>& nums) {
    for (int& x : nums) x *= 2;
}
void ref_op_negate(vector<int>& nums) {
    for (int& x : nums) x *= -1;
}
void ref_op_sort(vector<int>& nums) {
    sort(nums.begin(), nums.end());
}
void ref_op_reverse(vector<int>& nums) {
    reverse(nums.begin(), nums.end());
}
void ref_op_square(vector<int>& nums) {
    for (int& x : nums) x = x * x;
}

vector<int> solve_apply(vector<int> nums, vector<string> operations) {
    for (const string& op : operations) {
        if (op == "double")       ref_op_double(nums);
        else if (op == "negate")  ref_op_negate(nums);
        else if (op == "sort")    ref_op_sort(nums);
        else if (op == "reverse") ref_op_reverse(nums);
        else if (op == "square")  ref_op_square(nums);
    }
    return nums;
}

// ═══════════════════════════════════════════════════════════════════
// Test functions
// ═══════════════════════════════════════════════════════════════════

void test_warmup_01_greeting() {
    assert(solve_greeting("Maya") == "Hello, Maya!");
    assert(solve_greeting("World") == "Hello, World!");
    assert(solve_greeting("") == "Hello, !");
    assert(solve_greeting("A") == "Hello, A!");
    assert(solve_greeting("C++ Learner") == "Hello, C++ Learner!");
    cout << "  test_warmup_01_greeting.............. PASS" << endl;
}

void test_warmup_02_power() {
    assert(solve_power(2, 10) == 1024);
    assert(solve_power(3, 0) == 1);
    assert(solve_power(5, 3) == 125);
    assert(solve_power(7, 1) == 7);
    assert(solve_power(1, 100) == 1);
    assert(solve_power(2, 0) == 1);
    cout << "  test_warmup_02_power................. PASS" << endl;
}

void test_warmup_03_min_of_three() {
    assert(solve_min_of_three(3, 1, 2) == 1);
    assert(solve_min_of_three(5, 5, 5) == 5);
    assert(solve_min_of_three(-1, 0, 1) == -1);
    assert(solve_min_of_three(10, 3, 7) == 3);
    assert(solve_min_of_three(1, 2, 3) == 1);
    assert(solve_min_of_three(3, 2, 1) == 1);
    cout << "  test_warmup_03_min_of_three.......... PASS" << endl;
}

void test_warmup_04_repeat_string() {
    assert(solve_repeat("ha", 3) == "ha ha ha");
    assert(solve_repeat("yo", 2) == "yo yo");
    assert(solve_repeat("ok", 1) == "ok");
    assert(solve_repeat("abc") == "abc abc abc");  // default n=3
    assert(solve_repeat("hi", 0) == "");
    assert(solve_repeat("x", 5) == "x x x x x");
    cout << "  test_warmup_04_repeat_string......... PASS" << endl;
}

void test_warmup_05_double_list() {
    // Test 1: normal case — verify both return and in-place modification
    vector<int> v1 = {1, 2, 3};
    vector<int> r1 = solve_double_list(v1);
    assert(r1 == (vector<int>{2, 4, 6}));
    assert(v1 == (vector<int>{2, 4, 6}));  // original modified in place

    // Test 2: with zero and negative
    vector<int> v2 = {0, -1, 5};
    vector<int> r2 = solve_double_list(v2);
    assert(r2 == (vector<int>{0, -2, 10}));
    assert(v2 == (vector<int>{0, -2, 10}));

    // Test 3: empty vector
    vector<int> v3 = {};
    vector<int> r3 = solve_double_list(v3);
    assert(r3.empty());
    assert(v3.empty());

    // Test 4: single element
    vector<int> v4 = {7};
    vector<int> r4 = solve_double_list(v4);
    assert(r4 == (vector<int>{14}));
    assert(v4 == (vector<int>{14}));

    cout << "  test_warmup_05_double_list........... PASS" << endl;
}

void test_practice_01_calculator() {
    // Valid operations
    assert(solve_calc(10, "add", 5) == 15);
    assert(solve_calc_valid(10, "add", 5) == true);

    assert(solve_calc(10, "subtract", 3) == 7);
    assert(solve_calc_valid(10, "subtract", 3) == true);

    assert(solve_calc(10, "multiply", 4) == 40);
    assert(solve_calc_valid(10, "multiply", 4) == true);

    assert(solve_calc(10, "divide", 3) == 3);
    assert(solve_calc_valid(10, "divide", 3) == true);

    // Invalid: divide by zero
    assert(solve_calc(10, "divide", 0) == 0);
    assert(solve_calc_valid(10, "divide", 0) == false);

    // Invalid: unknown operator
    assert(solve_calc(10, "modulo", 3) == 0);
    assert(solve_calc_valid(10, "modulo", 3) == false);

    cout << "  test_practice_01_calculator.......... PASS" << endl;
}

void test_practice_02_password_strength() {
    assert(solve_password("hi") == "weak");
    assert(solve_password("short") == "weak");
    assert(solve_password("abcdefgh") == "medium");
    assert(solve_password("abcdefg1") == "medium");
    assert(solve_password("Abcdefgh") == "medium");
    assert(solve_password("Abcdefg1") == "strong");
    assert(solve_password("PASSWORD1") == "strong");
    cout << "  test_practice_02_password............ PASS" << endl;
}

void test_practice_03_temperature() {
    // Helper to compare doubles with tolerance
    auto close = [](double a, double b) {
        return fabs(a - b) < 0.01;
    };

    assert(close(solve_temp(100.0, "C", "F"), 212.0));
    assert(close(solve_temp(32.0, "F", "C"), 0.0));
    assert(close(solve_temp(0.0, "C", "K"), 273.2));
    assert(close(solve_temp(300.0, "K", "F"), 80.3));
    assert(close(solve_temp(50.0, "C", "C"), 50.0));
    assert(close(solve_temp(50.0, "X", "C"), -1.0));
    assert(close(solve_temp(50.0, "C", "Z"), -1.0));
    cout << "  test_practice_03_temperature......... PASS" << endl;
}

void test_practice_04_stats() {
    auto close_vec = [](vector<double> a, vector<double> b) {
        if (a.size() != b.size()) return false;
        for (int i = 0; i < (int)a.size(); i++) {
            if (fabs(a[i] - b[i]) > 0.01) return false;
        }
        return true;
    };

    assert(close_vec(solve_stats({1, 2, 3, 4, 5}), {1.0, 5.0, 3.0}));
    assert(close_vec(solve_stats({10}), {10.0, 10.0, 10.0}));
    assert(close_vec(solve_stats({-3, 0, 3}), {-3.0, 3.0, 0.0}));
    assert(close_vec(solve_stats({7, 7, 7}), {7.0, 7.0, 7.0}));
    assert(solve_stats({}).empty());
    assert(close_vec(solve_stats({1, 2}), {1.0, 2.0, 1.5}));
    cout << "  test_practice_04_stats............... PASS" << endl;
}

void test_challenge_01_prime_check() {
    assert(solve_prime(2) == true);
    assert(solve_prime(3) == true);
    assert(solve_prime(4) == false);
    assert(solve_prime(17) == true);
    assert(solve_prime(1) == false);
    assert(solve_prime(0) == false);
    assert(solve_prime(-5) == false);
    assert(solve_prime(97) == true);
    assert(solve_prime(100) == false);
    assert(solve_prime(100003) == true);
    cout << "  test_challenge_01_prime_check........ PASS" << endl;
}

void test_challenge_02_apply_operations() {
    assert(solve_apply({1, 2, 3}, {"double"}) == (vector<int>{2, 4, 6}));
    assert(solve_apply({3, 1, 2}, {"sort"}) == (vector<int>{1, 2, 3}));
    assert(solve_apply({1, 2, 3}, {"double", "reverse"}) == (vector<int>{6, 4, 2}));
    assert(solve_apply({3, 1, 2}, {"sort", "negate"}) == (vector<int>{-1, -2, -3}));
    assert(solve_apply({1, 2, 3}, {"square", "sort"}) == (vector<int>{1, 4, 9}));
    assert(solve_apply({1, 2, 3}, {"unknown"}) == (vector<int>{1, 2, 3}));
    assert(solve_apply({}, {"double"}).empty());
    cout << "  test_challenge_02_apply_operations... PASS" << endl;
}

// ═══════════════════════════════════════════════════════════════════
// Main — run all tests
// ═══════════════════════════════════════════════════════════════════
int main() {
    cout << "=== Chapter 4: Functions ===" << endl;
    cout << endl;

    cout << "--- Warmup Problems ---" << endl;
    test_warmup_01_greeting();
    test_warmup_02_power();
    test_warmup_03_min_of_three();
    test_warmup_04_repeat_string();
    test_warmup_05_double_list();
    cout << endl;

    cout << "--- Practice Problems ---" << endl;
    test_practice_01_calculator();
    test_practice_02_password_strength();
    test_practice_03_temperature();
    test_practice_04_stats();
    cout << endl;

    cout << "--- Challenge Problems ---" << endl;
    test_challenge_01_prime_check();
    test_challenge_02_apply_operations();
    cout << endl;

    cout << "All Chapter 4 tests passed!" << endl;
    return 0;
}
