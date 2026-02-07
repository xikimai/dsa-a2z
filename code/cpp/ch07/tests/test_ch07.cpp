/*
 * Tests for Chapter 7: Number Wizardry -- Math for Programmers
 * Build: g++ -std=c++17 -o /tmp/test_ch07 code/cpp/ch07/tests/test_ch07.cpp && /tmp/test_ch07
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named to avoid collisions)
// =====================================================================

// --- W1: Count Digits ---
int solve_count_digits(long long n) {
    n = abs(n);
    if (n == 0) return 1;
    int count = 0;
    while (n > 0) { count++; n /= 10; }
    return count;
}

// --- W2: Reverse Number ---
long long solve_reverse_number(long long n) {
    long long sign = (n < 0) ? -1 : 1;
    n = abs(n);
    long long reversed = 0;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    return sign * reversed;
}

// --- W3: Sum of Digits ---
int solve_sum_of_digits(long long n) {
    n = abs(n);
    int sum = 0;
    while (n > 0) { sum += (int)(n % 10); n /= 10; }
    return sum;
}

// --- W4: Palindrome ---
bool solve_palindrome(long long n) {
    if (n < 0) return false;
    long long original = n;
    long long reversed = 0;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    return original == reversed;
}

// --- W5: Armstrong ---
bool solve_armstrong(long long n) {
    if (n < 0) return false;
    int numDigits = 0;
    long long temp = n;
    if (n == 0) numDigits = 1;
    else while (temp > 0) { numDigits++; temp /= 10; }
    temp = n;
    long long sum = 0;
    while (temp > 0) {
        long long d = temp % 10;
        sum += (long long)pow(d, numDigits);
        temp /= 10;
    }
    return sum == n;
}

// --- P1: All Divisors ---
vector<int> solve_all_divisors(int n) {
    vector<int> divs;
    for (int i = 1; (long long)i * i <= n; i++) {
        if (n % i == 0) {
            divs.push_back(i);
            if (i != n / i) divs.push_back(n / i);
        }
    }
    sort(divs.begin(), divs.end());
    return divs;
}

// --- P2: GCD and LCM ---
long long gcd_helper(long long a, long long b) {
    while (b != 0) { long long t = b; b = a % b; a = t; }
    return a;
}

vector<long long> solve_gcd_lcm(long long a, long long b) {
    long long g = gcd_helper(a, b);
    long long lcm = (g == 0) ? 0 : a / g * b;
    return {g, lcm};
}

// --- P3: Mod Exponentiation ---
long long solve_mod_exp(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) result = result * base % mod;
        exp /= 2;
        base = base * base % mod;
    }
    return result;
}

// --- P4: Prime Factorization ---
vector<vector<int>> solve_prime_factors(long long n) {
    vector<vector<int>> factors;
    for (long long d = 2; d * d <= n; d++) {
        if (n % d == 0) {
            int count = 0;
            while (n % d == 0) { count++; n /= d; }
            factors.push_back({(int)d, count});
        }
    }
    if (n > 1) factors.push_back({(int)n, 1});
    return factors;
}

// --- P5: Trailing Zeros ---
int solve_trailing_zeros(int n) {
    int count = 0;
    long long p = 5;
    while (p <= n) { count += (int)(n / p); p *= 5; }
    return count;
}

// --- C1: GCD Three Ways ---
long long solve_gcd_subtract(long long a, long long b) {
    if (a == 0) return b;
    if (b == 0) return a;
    while (a != b) {
        if (a > b) a -= b; else b -= a;
    }
    return a;
}

long long solve_gcd_euclidean(long long a, long long b) {
    while (b != 0) { long long t = b; b = a % b; a = t; }
    return a;
}

vector<long long> solve_gcd_extended(long long a, long long b) {
    if (b == 0) return {a, 1, 0};
    auto r = solve_gcd_extended(b, a % b);
    long long x = r[2];
    long long y = r[1] - (a / b) * r[2];
    return {r[0], x, y};
}

// --- C2: Sieve ---
vector<int> solve_sieve(int n) {
    vector<int> primes;
    if (n < 2) return primes;
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; (long long)i * i <= n; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) is_prime[j] = false;
        }
    }
    for (int i = 2; i <= n; i++) if (is_prime[i]) primes.push_back(i);
    return primes;
}

// --- C3: GCD Pair Sum ---
long long solve_gcd_pair_sum(vector<int>& nums) {
    long long total = 0;
    int n = (int)nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            total += gcd_helper(nums[i], nums[j]);
        }
    }
    return total;
}

// =====================================================================
// Test functions
// =====================================================================

void test_warmup_01_count_digits() {
    assert(solve_count_digits(12345) == 5);
    assert(solve_count_digits(0) == 1);
    assert(solve_count_digits(-42) == 2);
    assert(solve_count_digits(7) == 1);
    assert(solve_count_digits(1000000000LL) == 10);
    cout << "  test_warmup_01_count_digits.......... PASS" << endl;
}

void test_warmup_02_reverse_number() {
    assert(solve_reverse_number(12345) == 54321);
    assert(solve_reverse_number(-123) == -321);
    assert(solve_reverse_number(1200) == 21);
    assert(solve_reverse_number(0) == 0);
    assert(solve_reverse_number(5) == 5);
    cout << "  test_warmup_02_reverse_number........ PASS" << endl;
}

void test_warmup_03_sum_of_digits() {
    assert(solve_sum_of_digits(12345) == 15);
    assert(solve_sum_of_digits(0) == 0);
    assert(solve_sum_of_digits(-456) == 15);
    assert(solve_sum_of_digits(999) == 27);
    assert(solve_sum_of_digits(100) == 1);
    cout << "  test_warmup_03_sum_of_digits......... PASS" << endl;
}

void test_warmup_04_palindrome() {
    assert(solve_palindrome(121) == true);
    assert(solve_palindrome(-121) == false);
    assert(solve_palindrome(10) == false);
    assert(solve_palindrome(0) == true);
    assert(solve_palindrome(1001) == true);
    assert(solve_palindrome(1234321) == true);
    cout << "  test_warmup_04_palindrome............ PASS" << endl;
}

void test_warmup_05_armstrong() {
    assert(solve_armstrong(153) == true);
    assert(solve_armstrong(370) == true);
    assert(solve_armstrong(9474) == true);
    assert(solve_armstrong(100) == false);
    assert(solve_armstrong(1) == true);
    assert(solve_armstrong(0) == true);
    cout << "  test_warmup_05_armstrong............. PASS" << endl;
}

void test_practice_01_all_divisors() {
    assert(solve_all_divisors(36) == (vector<int>{1,2,3,4,6,9,12,18,36}));
    assert(solve_all_divisors(1) == (vector<int>{1}));
    assert(solve_all_divisors(7) == (vector<int>{1,7}));
    assert(solve_all_divisors(12) == (vector<int>{1,2,3,4,6,12}));
    cout << "  test_practice_01_all_divisors........ PASS" << endl;
}

void test_practice_02_gcd_lcm() {
    assert(solve_gcd_lcm(12, 18) == (vector<long long>{6, 36}));
    assert(solve_gcd_lcm(7, 13) == (vector<long long>{1, 91}));
    assert(solve_gcd_lcm(0, 5) == (vector<long long>{5, 0}));
    assert(solve_gcd_lcm(100, 75) == (vector<long long>{25, 300}));
    cout << "  test_practice_02_gcd_lcm............. PASS" << endl;
}

void test_practice_03_mod_exp() {
    assert(solve_mod_exp(2, 10, 1000000007) == 1024);
    assert(solve_mod_exp(2, 20, 1000000007) == 1048576);
    assert(solve_mod_exp(123456789, 0, 1000000007) == 1);
    assert(solve_mod_exp(2, 100, 1000000007) == 976371285);
    cout << "  test_practice_03_mod_exp............. PASS" << endl;
}

void test_practice_04_prime_factors() {
    auto r1 = solve_prime_factors(12);
    assert(r1.size() == 2);
    assert(r1[0][0] == 2 && r1[0][1] == 2);
    assert(r1[1][0] == 3 && r1[1][1] == 1);

    assert(solve_prime_factors(1).empty());

    auto r3 = solve_prime_factors(7);
    assert(r3.size() == 1 && r3[0][0] == 7 && r3[0][1] == 1);

    auto r4 = solve_prime_factors(360);
    assert(r4.size() == 3);
    assert(r4[0][0] == 2 && r4[0][1] == 3);
    assert(r4[1][0] == 3 && r4[1][1] == 2);
    assert(r4[2][0] == 5 && r4[2][1] == 1);

    cout << "  test_practice_04_prime_factors....... PASS" << endl;
}

void test_practice_05_trailing_zeros() {
    assert(solve_trailing_zeros(5) == 1);
    assert(solve_trailing_zeros(10) == 2);
    assert(solve_trailing_zeros(25) == 6);
    assert(solve_trailing_zeros(100) == 24);
    assert(solve_trailing_zeros(0) == 0);
    cout << "  test_practice_05_trailing_zeros...... PASS" << endl;
}

void test_challenge_01_gcd_three_ways() {
    // Subtraction
    assert(solve_gcd_subtract(48, 18) == 6);
    assert(solve_gcd_subtract(7, 13) == 1);
    assert(solve_gcd_subtract(10, 10) == 10);

    // Euclidean
    assert(solve_gcd_euclidean(48, 18) == 6);
    assert(solve_gcd_euclidean(7, 13) == 1);
    assert(solve_gcd_euclidean(0, 5) == 5);
    assert(solve_gcd_euclidean(1000000000LL, 999999999LL) == 1);

    // Extended
    auto r1 = solve_gcd_extended(35, 15);
    assert(r1[0] == 5);
    assert(35 * r1[1] + 15 * r1[2] == 5);

    auto r2 = solve_gcd_extended(7, 11);
    assert(r2[0] == 1);
    assert(7 * r2[1] + 11 * r2[2] == 1);

    auto r3 = solve_gcd_extended(6, 6);
    assert(r3[0] == 6);
    assert(6 * r3[1] + 6 * r3[2] == 6);

    cout << "  test_challenge_01_gcd_three_ways..... PASS" << endl;
}

void test_challenge_02_sieve() {
    assert(solve_sieve(10) == (vector<int>{2,3,5,7}));
    assert(solve_sieve(1) == (vector<int>{}));
    assert(solve_sieve(2) == (vector<int>{2}));
    assert(solve_sieve(30) == (vector<int>{2,3,5,7,11,13,17,19,23,29}));
    assert(solve_sieve(0) == (vector<int>{}));
    cout << "  test_challenge_02_sieve.............. PASS" << endl;
}

void test_challenge_03_gcd_pair_sum() {
    vector<int> v1 = {2, 4, 6};
    assert(solve_gcd_pair_sum(v1) == 6);
    vector<int> v2 = {3, 6, 9};
    assert(solve_gcd_pair_sum(v2) == 9);
    vector<int> v3 = {12, 18, 24};
    assert(solve_gcd_pair_sum(v3) == 24);
    vector<int> v4 = {7};
    assert(solve_gcd_pair_sum(v4) == 0);
    vector<int> v5 = {2, 3, 5, 7};
    assert(solve_gcd_pair_sum(v5) == 6);
    cout << "  test_challenge_03_gcd_pair_sum....... PASS" << endl;
}

// =====================================================================
// Main -- run all tests
// =====================================================================
int main() {
    cout << "Testing Chapter 7..." << endl;
    cout << endl;

    cout << "--- Warmup Problems ---" << endl;
    test_warmup_01_count_digits();
    test_warmup_02_reverse_number();
    test_warmup_03_sum_of_digits();
    test_warmup_04_palindrome();
    test_warmup_05_armstrong();
    cout << endl;

    cout << "--- Practice Problems ---" << endl;
    test_practice_01_all_divisors();
    test_practice_02_gcd_lcm();
    test_practice_03_mod_exp();
    test_practice_04_prime_factors();
    test_practice_05_trailing_zeros();
    cout << endl;

    cout << "--- Challenge Problems ---" << endl;
    test_challenge_01_gcd_three_ways();
    test_challenge_02_sieve();
    test_challenge_03_gcd_pair_sum();
    cout << endl;

    cout << "All tests passed!" << endl;
    return 0;
}
