/*
 * Tests for Chapter 12: Bit Manipulation — The Language of Computers
 * Build: g++ -std=c++17 -o /tmp/test_ch12 code/cpp/ch12/tests/test_ch12.cpp && /tmp/test_ch12
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// --- W1: Binary Representation ---
string ref_binary_rep(int n) {
    if (n == 0) return "0";
    string bits;
    while (n > 0) {
        bits += char('0' + n % 2);
        n /= 2;
    }
    reverse(bits.begin(), bits.end());
    return bits;
}

// --- W2: Count Set Bits ---
int ref_count_set_bits(int n) {
    int count = 0;
    while (n) {
        n &= (n - 1);
        count++;
    }
    return count;
}

// --- W3: Check Power of Two ---
bool ref_power_of_two(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}

// --- W4: Check i-th Bit ---
bool ref_ith_bit(int n, int i) {
    return (n >> i) & 1;
}

// --- P1: Single Number ---
int ref_single_number(vector<int> nums) {
    int result = 0;
    for (int x : nums) result ^= x;
    return result;
}

// --- P2: Toggle i-th Bit ---
int ref_toggle(int n, int i) {
    return n ^ (1 << i);
}

// --- P3: Set and Clear Bits ---
int ref_set_bit(int n, int i) { return n | (1 << i); }
int ref_clear_bit(int n, int i) { return n & ~(1 << i); }

// --- P4: Power Set ---
vector<vector<int>> ref_power_set(vector<int> nums) {
    int n = nums.size();
    vector<vector<int>> result;
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            if ((mask >> i) & 1) subset.push_back(nums[i]);
        }
        result.push_back(subset);
    }
    return result;
}

// --- C1: Single Number Three Ways ---
int ref_single_sort(vector<int> nums) {
    sort(nums.begin(), nums.end());
    for (int i = 0; i < (int)nums.size() - 1; i += 2) {
        if (nums[i] != nums[i + 1]) return nums[i];
    }
    return nums.back();
}

int ref_single_hash(vector<int> nums) {
    unordered_map<int, int> freq;
    for (int x : nums) freq[x]++;
    for (auto& [val, cnt] : freq) {
        if (cnt == 1) return val;
    }
    return -1;
}

int ref_single_xor(vector<int> nums) {
    int result = 0;
    for (int x : nums) result ^= x;
    return result;
}

// --- C2: Two Odd Occurring ---
vector<int> ref_two_odd(vector<int> nums) {
    int xorAll = 0;
    for (int x : nums) xorAll ^= x;
    int diffBit = xorAll & (-xorAll);
    int a = 0, b = 0;
    for (int x : nums) {
        if (x & diffBit) a ^= x;
        else b ^= x;
    }
    if (a > b) swap(a, b);
    return {a, b};
}

// --- C3: Min Bit Flips ---
int ref_min_flips(int start, int goal) {
    int x = start ^ goal;
    int count = 0;
    while (x) {
        x &= (x - 1);
        count++;
    }
    return count;
}

// =====================================================================
// Test framework
// =====================================================================

int tests_passed = 0;
int tests_total = 0;

void check(bool condition, const string& name) {
    tests_total++;
    if (condition) {
        tests_passed++;
    } else {
        cout << "  FAIL: " << name << endl;
    }
}

// =====================================================================
// Test functions
// =====================================================================

void test_w1_binary_representation() {
    cout << "Testing W1: Binary Representation..." << endl;
    check(ref_binary_rep(0) == "0", "0");
    check(ref_binary_rep(1) == "1", "1");
    check(ref_binary_rep(5) == "101", "5");
    check(ref_binary_rep(42) == "101010", "42");
    check(ref_binary_rep(255) == "11111111", "255");
    check(ref_binary_rep(1024) == "10000000000", "1024");
    check(ref_binary_rep(1000000000) != "", "10^9 non-empty");
}

void test_w2_count_set_bits() {
    cout << "Testing W2: Count Set Bits..." << endl;
    check(ref_count_set_bits(0) == 0, "0");
    check(ref_count_set_bits(1) == 1, "1");
    check(ref_count_set_bits(42) == 3, "42");
    check(ref_count_set_bits(255) == 8, "255");
    check(ref_count_set_bits(1023) == 10, "1023");
    check(ref_count_set_bits(1024) == 1, "1024");
    check(ref_count_set_bits(999999999) == __builtin_popcount(999999999), "10^9-1");
}

void test_w3_check_power_of_two() {
    cout << "Testing W3: Check Power of Two..." << endl;
    check(ref_power_of_two(1) == true, "1");
    check(ref_power_of_two(2) == true, "2");
    check(ref_power_of_two(4) == true, "4");
    check(ref_power_of_two(1024) == true, "1024");
    check(ref_power_of_two(0) == false, "0");
    check(ref_power_of_two(3) == false, "3");
    check(ref_power_of_two(6) == false, "6");
    check(ref_power_of_two(-4) == false, "-4");
    check(ref_power_of_two(1 << 20) == true, "2^20");
    check(ref_power_of_two((1 << 20) + 1) == false, "2^20+1");
}

void test_w4_check_ith_bit() {
    cout << "Testing W4: Check i-th Bit..." << endl;
    check(ref_ith_bit(42, 1) == true, "42 bit 1");
    check(ref_ith_bit(42, 2) == false, "42 bit 2");
    check(ref_ith_bit(42, 3) == true, "42 bit 3");
    check(ref_ith_bit(42, 5) == true, "42 bit 5");
    check(ref_ith_bit(42, 6) == false, "42 bit 6");
    check(ref_ith_bit(0, 0) == false, "0 bit 0");
    check(ref_ith_bit(1, 0) == true, "1 bit 0");
    check(ref_ith_bit(16, 4) == true, "16 bit 4");
}

void test_p1_single_number() {
    cout << "Testing P1: Single Number..." << endl;
    check(ref_single_number({4,1,2,1,2}) == 4, "[4,1,2,1,2]");
    check(ref_single_number({2,2,1}) == 1, "[2,2,1]");
    check(ref_single_number({1}) == 1, "[1]");
    check(ref_single_number({1,3,5,3,1}) == 5, "[1,3,5,3,1]");
    check(ref_single_number({-1,2,-1}) == 2, "[-1,2,-1]");
    check(ref_single_number({0,5,0}) == 5, "[0,5,0]");
}

void test_p2_toggle_ith_bit() {
    cout << "Testing P2: Toggle i-th Bit..." << endl;
    check(ref_toggle(42, 0) == 43, "42 toggle 0");
    check(ref_toggle(42, 1) == 40, "42 toggle 1");
    check(ref_toggle(0, 3) == 8, "0 toggle 3");
    check(ref_toggle(42, 5) == 10, "42 toggle 5");
    check(ref_toggle(ref_toggle(42, 3), 3) == 42, "double toggle");
    check(ref_toggle(255, 0) == 254, "255 toggle 0");
}

void test_p3_set_and_clear_bits() {
    cout << "Testing P3: Set and Clear Bits..." << endl;
    check(ref_set_bit(42, 0) == 43, "set 42 bit 0");
    check(ref_set_bit(42, 1) == 42, "set 42 bit 1 (already set)");
    check(ref_set_bit(0, 5) == 32, "set 0 bit 5");
    check(ref_clear_bit(42, 1) == 40, "clear 42 bit 1");
    check(ref_clear_bit(42, 0) == 42, "clear 42 bit 0 (already clear)");
    int n = 255;
    for (int i = 0; i < 8; i++) n = ref_clear_bit(n, i);
    check(n == 0, "clear all bits of 255");
    int m = ref_set_bit(42, 0);
    check(m == 43, "set bit 0 of 42");
    m = ref_clear_bit(m, 0);
    check(m == 42, "clear bit 0 back");
}

void test_p4_power_set() {
    cout << "Testing P4: Power Set..." << endl;
    auto r3 = ref_power_set({1, 2, 3});
    check((int)r3.size() == 8, "[1,2,3] size");
    vector<vector<int>> expected3 = {{}, {1}, {2}, {1,2}, {3}, {1,3}, {2,3}, {1,2,3}};
    check(r3 == expected3, "[1,2,3] content");
    auto r0 = ref_power_set({});
    check(r0 == vector<vector<int>>{{}}, "[] content");
    auto r1 = ref_power_set({5});
    check(r1 == (vector<vector<int>>{{}, {5}}), "[5] content");
    auto r2 = ref_power_set({10, 20});
    check(r2 == (vector<vector<int>>{{}, {10}, {20}, {10,20}}), "[10,20] content");
    check((int)ref_power_set({1,2,3,4}).size() == 16, "[1,2,3,4] count");
}

void test_c1_single_number_three_ways() {
    cout << "Testing C1: Single Number Three Ways..." << endl;
    vector<pair<vector<int>, int>> cases = {
        {{4,1,2,1,2}, 4},
        {{2,2,1}, 1},
        {{1}, 1},
        {{1,3,5,3,1}, 5},
        {{-1,2,-1}, 2}
    };
    for (auto& [nums, expected] : cases) {
        string label = "expected=" + to_string(expected);
        check(ref_single_sort(nums) == expected, "sort: " + label);
        check(ref_single_hash(nums) == expected, "hash: " + label);
        check(ref_single_xor(nums) == expected, "xor: " + label);
    }
}

void test_c2_two_odd_occurring() {
    cout << "Testing C2: Two Odd Occurring..." << endl;
    check(ref_two_odd({2,4,7,9,2,4}) == (vector<int>{7,9}), "[2,4,7,9,2,4]");
    check(ref_two_odd({1,2,3,2,1,4}) == (vector<int>{3,4}), "[1,2,3,2,1,4]");
    check(ref_two_odd({5,10}) == (vector<int>{5,10}), "[5,10]");
    check(ref_two_odd({1,1,2,2,3,3,100,200}) == (vector<int>{100,200}), "many pairs");
    check(ref_two_odd({7,7,7,9,3,3}) == (vector<int>{7,9}), "triple+single");
    check(ref_two_odd({999999,888888,999999,777777,888888,777777,11,22}) == (vector<int>{11,22}),
          "large numbers");
}

void test_c3_min_bit_flips() {
    cout << "Testing C3: Min Bit Flips..." << endl;
    check(ref_min_flips(10, 7) == 3, "10 -> 7");
    check(ref_min_flips(3, 4) == 3, "3 -> 4");
    check(ref_min_flips(0, 0) == 0, "0 -> 0");
    check(ref_min_flips(42, 42) == 0, "42 -> 42");
    check(ref_min_flips(0, 255) == 8, "0 -> 255");
    check(ref_min_flips(8, 0) == 1, "8 -> 0");
    check(ref_min_flips(1023, 0) == 10, "1023 -> 0");
}

// =====================================================================
// Main
// =====================================================================

int main() {
    test_w1_binary_representation();
    test_w2_count_set_bits();
    test_w3_check_power_of_two();
    test_w4_check_ith_bit();
    test_p1_single_number();
    test_p2_toggle_ith_bit();
    test_p3_set_and_clear_bits();
    test_p4_power_set();
    test_c1_single_number_three_ways();
    test_c2_two_odd_occurring();
    test_c3_min_bit_flips();

    cout << endl;
    if (tests_passed == tests_total) {
        cout << "All " << tests_total << " tests passed!" << endl;
    } else {
        cout << tests_passed << " / " << tests_total << " tests passed." << endl;
    }
    return (tests_passed == tests_total) ? 0 : 1;
}
