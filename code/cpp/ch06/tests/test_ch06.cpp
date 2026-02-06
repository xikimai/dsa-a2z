/*
 * Tests for Chapter 6: How Fast Is Your Code?
 * Build: g++ -std=c++17 -o test_ch06 code/cpp/ch06/tests/test_ch06.cpp && ./test_ch06
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named to avoid collisions)
// =====================================================================

// --- Warmup 01: Count the Steps ---
int solve_count_steps(string code_id, int n) {
    if (code_id == "single_loop") return n;
    if (code_id == "double_loop") return n * n;
    if (code_id == "half_loop") return n / 2;
    if (code_id == "dependent_loop") return n * (n + 1) / 2;
    if (code_id == "log_loop") {
        if (n < 1) return 0;
        return (int)(log2(n));
    }
    return 0;
}

// --- Warmup 02: Is It Fast Enough? ---
bool solve_fast_enough(int n, string complexity) {
    long long limit = 100000000LL;
    long long ops = 0;

    if (complexity == "1") {
        ops = 1;
    } else if (complexity == "log_n") {
        ops = (long long)(log2(n));
    } else if (complexity == "n") {
        ops = (long long)n;
    } else if (complexity == "n_log_n") {
        ops = (long long)((double)n * log2(n));
    } else if (complexity == "n^2") {
        ops = (long long)n * n;
    } else if (complexity == "n^3") {
        ops = (long long)n * n * n;
    } else if (complexity == "2^n") {
        if (n > 30) return false;
        ops = 1LL << n;
    }

    return ops < limit;
}

// --- Warmup 03: Mystery Complexity ---
string solve_mystery_complexity(vector<int> n_values, vector<int> counts) {
    int k = (int)n_values.size();

    // Check if all counts are the same -> O(1)
    bool all_same = true;
    for (int i = 1; i < k; i++) {
        if (counts[i] != counts[0]) {
            all_same = false;
            break;
        }
    }
    if (all_same) return "O(1)";

    // Look at ratio of counts vs ratio of n values (last two points)
    double n_ratio = (double)n_values[k - 1] / n_values[k - 2];
    double c_ratio = (double)counts[k - 1] / counts[k - 2];

    if (abs(c_ratio - n_ratio * n_ratio) < 0.5) return "O(n^2)";
    if (abs(c_ratio - n_ratio) < 0.5) return "O(n)";
    return "O(log n)";
}

// --- Warmup 04: Sum of 1 to N ---
vector<int> solve_sum_to_n(int n) {
    int loop_sum = 0;
    for (int i = 1; i <= n; i++) loop_sum += i;

    int formula_sum = n * (n + 1) / 2;

    int nested_sum = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            nested_sum += 1;
        }
    }

    return {loop_sum, formula_sum, nested_sum};
}

// --- Practice 01: Contains Duplicate ---
bool solve_contains_duplicate(vector<int> nums) {
    unordered_set<int> seen;
    for (int x : nums) {
        if (seen.count(x)) return true;
        seen.insert(x);
    }
    return false;
}

// --- Practice 02: Max Subarray Sum (Brute) ---
int solve_max_subarray_brute(vector<int> nums) {
    if (nums.empty()) return 0;

    int max_sum = INT_MIN;
    for (int i = 0; i < (int)nums.size(); i++) {
        int current_sum = 0;
        for (int j = i; j < (int)nums.size(); j++) {
            current_sum += nums[j];
            max_sum = max(max_sum, current_sum);
        }
    }
    return max_sum;
}

// --- Practice 03: Sorted Squares ---
vector<int> solve_sorted_squares(vector<int> nums) {
    int n = (int)nums.size();
    if (n == 0) return {};

    vector<int> result(n);
    int left = 0;
    int right = n - 1;
    int pos = n - 1;

    while (left <= right) {
        int left_sq = nums[left] * nums[left];
        int right_sq = nums[right] * nums[right];
        if (left_sq > right_sq) {
            result[pos] = left_sq;
            left++;
        } else {
            result[pos] = right_sq;
            right--;
        }
        pos--;
    }

    return result;
}

// --- Practice 04: Majority Element ---
int solve_majority_element(vector<int> nums) {
    int candidate = 0;
    int count = 0;

    for (int x : nums) {
        if (count == 0) {
            candidate = x;
        }
        count += (x == candidate) ? 1 : -1;
    }

    return candidate;
}

// --- Challenge 01: Two Sum (three approaches) ---
vector<int> solve_two_sum_brute(vector<int> nums, int target) {
    int n = (int)nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] == target) {
                return {i, j};
            }
        }
    }
    return {-1, -1};
}

vector<int> solve_two_sum_sort(vector<int> nums, int target) {
    int n = (int)nums.size();
    vector<pair<int, int>> indexed(n);
    for (int i = 0; i < n; i++) {
        indexed[i] = {nums[i], i};
    }
    sort(indexed.begin(), indexed.end());

    int left = 0;
    int right = n - 1;
    while (left < right) {
        int sum = indexed[left].first + indexed[right].first;
        if (sum == target) {
            int i = indexed[left].second;
            int j = indexed[right].second;
            if (i > j) swap(i, j);
            return {i, j};
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return {-1, -1};
}

vector<int> solve_two_sum_hash(vector<int> nums, int target) {
    unordered_map<int, int> seen;
    for (int i = 0; i < (int)nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.count(complement)) {
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {-1, -1};
}

// --- Challenge 02: Performance Showdown ---
static double get_ops(string complexity, int n) {
    if (complexity == "1") return 1.0;
    if (complexity == "log_n") return log2((double)n);
    if (complexity == "n") return (double)n;
    if (complexity == "n_log_n") return (double)n * log2((double)n);
    if (complexity == "n^2") return (double)n * n;
    if (complexity == "n^3") return (double)n * n * n;
    if (complexity == "2^n") return pow(2.0, n);
    return 0.0;
}

string solve_performance_showdown(string a, string b, int n) {
    double ops_a = get_ops(a, n);
    double ops_b = get_ops(b, n);

    if (ops_a < ops_b) return "A";
    if (ops_b < ops_a) return "B";
    return "TIE";
}

// =====================================================================
// Test functions
// =====================================================================

void test_warmup_01_count_steps() {
    assert(solve_count_steps("single_loop", 100) == 100);
    assert(solve_count_steps("double_loop", 10) == 100);
    assert(solve_count_steps("half_loop", 100) == 50);
    assert(solve_count_steps("half_loop", 7) == 3);
    assert(solve_count_steps("dependent_loop", 4) == 10);
    assert(solve_count_steps("log_loop", 16) == 4);
    assert(solve_count_steps("log_loop", 1) == 0);
    assert(solve_count_steps("log_loop", 1024) == 10);
    cout << "  test_warmup_01_count_steps........... PASS" << endl;
}

void test_warmup_02_fast_enough() {
    assert(solve_fast_enough(1000, "n^2") == true);
    assert(solve_fast_enough(100000, "n^2") == false);
    assert(solve_fast_enough(10000, "n^2") == false);
    assert(solve_fast_enough(9999, "n^2") == true);
    assert(solve_fast_enough(20, "2^n") == true);
    assert(solve_fast_enough(30, "2^n") == false);
    assert(solve_fast_enough(1000000, "n") == true);
    cout << "  test_warmup_02_fast_enough........... PASS" << endl;
}

void test_warmup_03_mystery_complexity() {
    assert(solve_mystery_complexity({1, 10, 100, 1000}, {5, 5, 5, 5}) == "O(1)");
    assert(solve_mystery_complexity({1, 2, 4, 8, 16}, {0, 1, 2, 3, 4}) == "O(log n)");
    assert(solve_mystery_complexity({100, 200, 400, 800}, {100, 200, 400, 800}) == "O(n)");
    assert(solve_mystery_complexity({10, 20, 40, 80}, {100, 400, 1600, 6400}) == "O(n^2)");
    cout << "  test_warmup_03_mystery_complexity.... PASS" << endl;
}

void test_warmup_04_sum_to_n() {
    assert(solve_sum_to_n(10) == (vector<int>{55, 55, 55}));
    assert(solve_sum_to_n(1) == (vector<int>{1, 1, 1}));
    assert(solve_sum_to_n(100) == (vector<int>{5050, 5050, 5050}));
    assert(solve_sum_to_n(0) == (vector<int>{0, 0, 0}));
    cout << "  test_warmup_04_sum_to_n.............. PASS" << endl;
}

void test_practice_01_contains_duplicate() {
    assert(solve_contains_duplicate({1, 2, 3, 1}) == true);
    assert(solve_contains_duplicate({1, 2, 3, 4}) == false);
    assert(solve_contains_duplicate({}) == false);
    assert(solve_contains_duplicate({1}) == false);
    assert(solve_contains_duplicate({1, 1}) == true);
    cout << "  test_practice_01_contains_duplicate.. PASS" << endl;
}

void test_practice_02_max_subarray_brute() {
    assert(solve_max_subarray_brute({-2, 1, -3, 4, -1, 2, 1, -5, 4}) == 6);
    assert(solve_max_subarray_brute({1}) == 1);
    assert(solve_max_subarray_brute({-1, -2, -3}) == -1);
    assert(solve_max_subarray_brute({5, 4, -1, 7, 8}) == 23);
    assert(solve_max_subarray_brute({}) == 0);
    cout << "  test_practice_02_max_subarray_brute.. PASS" << endl;
}

void test_practice_03_sorted_squares() {
    assert(solve_sorted_squares({-4, -1, 0, 3, 10}) == (vector<int>{0, 1, 9, 16, 100}));
    assert(solve_sorted_squares({-3, -2, -1}) == (vector<int>{1, 4, 9}));
    assert(solve_sorted_squares({0, 1, 2, 3}) == (vector<int>{0, 1, 4, 9}));
    assert(solve_sorted_squares({}) == (vector<int>{}));
    assert(solve_sorted_squares({-5, 5}) == (vector<int>{25, 25}));
    cout << "  test_practice_03_sorted_squares...... PASS" << endl;
}

void test_practice_04_majority_element() {
    assert(solve_majority_element({3, 2, 3}) == 3);
    assert(solve_majority_element({2, 2, 1, 1, 1, 2, 2}) == 2);
    assert(solve_majority_element({1}) == 1);
    assert(solve_majority_element({6, 6, 6, 7, 7}) == 6);
    cout << "  test_practice_04_majority_element.... PASS" << endl;
}

void test_challenge_01_two_sum_three_ways() {
    // Test brute force
    assert(solve_two_sum_brute({2, 7, 11, 15}, 9) == (vector<int>{0, 1}));
    assert(solve_two_sum_brute({3, 3}, 6) == (vector<int>{0, 1}));
    assert(solve_two_sum_brute({1, 2, 3}, 10) == (vector<int>{-1, -1}));
    assert(solve_two_sum_brute({1, 5, 3, 8}, 8) == (vector<int>{1, 2}));

    // Test sort + two pointers
    assert(solve_two_sum_sort({2, 7, 11, 15}, 9) == (vector<int>{0, 1}));
    assert(solve_two_sum_sort({3, 3}, 6) == (vector<int>{0, 1}));
    assert(solve_two_sum_sort({1, 2, 3}, 10) == (vector<int>{-1, -1}));
    assert(solve_two_sum_sort({1, 5, 3, 8}, 8) == (vector<int>{1, 2}));

    // Test hash map
    assert(solve_two_sum_hash({2, 7, 11, 15}, 9) == (vector<int>{0, 1}));
    assert(solve_two_sum_hash({3, 3}, 6) == (vector<int>{0, 1}));
    assert(solve_two_sum_hash({1, 2, 3}, 10) == (vector<int>{-1, -1}));
    assert(solve_two_sum_hash({1, 5, 3, 8}, 8) == (vector<int>{1, 2}));

    cout << "  test_challenge_01_two_sum_3_ways..... PASS" << endl;
}

void test_challenge_02_performance_showdown() {
    assert(solve_performance_showdown("n^2", "n_log_n", 1000) == "B");
    assert(solve_performance_showdown("n", "n", 100) == "TIE");
    assert(solve_performance_showdown("1", "log_n", 1000000) == "A");
    assert(solve_performance_showdown("n^2", "n^3", 10) == "A");
    cout << "  test_challenge_02_performance_shwdwn. PASS" << endl;
}

// =====================================================================
// Main -- run all tests
// =====================================================================
int main() {
    cout << "Testing Chapter 6..." << endl;
    cout << endl;

    cout << "--- Warmup Problems ---" << endl;
    test_warmup_01_count_steps();
    test_warmup_02_fast_enough();
    test_warmup_03_mystery_complexity();
    test_warmup_04_sum_to_n();
    cout << endl;

    cout << "--- Practice Problems ---" << endl;
    test_practice_01_contains_duplicate();
    test_practice_02_max_subarray_brute();
    test_practice_03_sorted_squares();
    test_practice_04_majority_element();
    cout << endl;

    cout << "--- Challenge Problems ---" << endl;
    test_challenge_01_two_sum_three_ways();
    test_challenge_02_performance_showdown();
    cout << endl;

    cout << "All tests passed!" << endl;
    return 0;
}
