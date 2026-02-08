/*
 * Tests for Chapter 10: The Magic of Recursion
 * Build: g++ -std=c++17 -o /tmp/test_ch10 code/cpp/ch10/tests/test_ch10.cpp && /tmp/test_ch10
 */

#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named to avoid collisions)
// =====================================================================

// --- W1: Factorial ---
long long ref_factorial(int n) {
    if (n == 0) return 1;
    return (long long)n * ref_factorial(n - 1);
}

// --- W2: Sum of First N ---
int ref_sum_first_n(int n) {
    if (n == 0) return 0;
    return n + ref_sum_first_n(n - 1);
}

// --- W3: Reverse String ---
string ref_reverse_string(string s) {
    if (s.size() <= 1) return s;
    return ref_reverse_string(s.substr(1)) + s[0];
}

// --- W4: Check Palindrome ---
bool ref_check_palindrome(string s) {
    if (s.size() <= 1) return true;
    if (s.front() != s.back()) return false;
    return ref_check_palindrome(s.substr(1, s.size() - 2));
}

// --- W5: Power ---
long long ref_power(int base, int exp) {
    if (exp == 0) return 1;
    return (long long)base * ref_power(base, exp - 1);
}

// --- P1: Fibonacci (memoized) ---
int ref_fib_helper(int n, unordered_map<int, int>& memo) {
    if (n <= 1) return n;
    if (memo.count(n)) return memo[n];
    memo[n] = ref_fib_helper(n - 1, memo) + ref_fib_helper(n - 2, memo);
    return memo[n];
}

int ref_fibonacci(int n) {
    unordered_map<int, int> memo;
    return ref_fib_helper(n, memo);
}

// --- P2: Sum of Digits ---
int ref_sum_digits(int n) {
    if (n < 0) n = -n;
    if (n < 10) return n;
    return n % 10 + ref_sum_digits(n / 10);
}

// --- P3: Count Occurrences ---
int ref_count_helper(const vector<int>& arr, int target, int idx) {
    if (idx == (int)arr.size()) return 0;
    int count = (arr[idx] == target) ? 1 : 0;
    return count + ref_count_helper(arr, target, idx + 1);
}

int ref_count_occurrences(vector<int> arr, int target) {
    return ref_count_helper(arr, target, 0);
}

// --- P4: Recursive Binary Search ---
int ref_bs_helper(const vector<int>& arr, int target, int lo, int hi) {
    if (lo > hi) return -1;
    int mid = lo + (hi - lo) / 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] < target) return ref_bs_helper(arr, target, mid + 1, hi);
    return ref_bs_helper(arr, target, lo, mid - 1);
}

int ref_binary_search(vector<int> arr, int target) {
    return ref_bs_helper(arr, target, 0, (int)arr.size() - 1);
}

// --- P5: Generate Subsets ---
void ref_subsets_bt(const vector<int>& nums, int idx, vector<int>& current,
                    vector<vector<int>>& result) {
    if (idx == (int)nums.size()) {
        result.push_back(current);
        return;
    }
    current.push_back(nums[idx]);
    ref_subsets_bt(nums, idx + 1, current, result);
    current.pop_back();
    ref_subsets_bt(nums, idx + 1, current, result);
}

vector<vector<int>> ref_generate_subsets(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<int> current;
    ref_subsets_bt(nums, 0, current, result);
    sort(result.begin(), result.end());
    return result;
}

// --- C1: Fibonacci Three Ways ---
long long ref_fib_naive(int n) {
    if (n <= 1) return n;
    return ref_fib_naive(n - 1) + ref_fib_naive(n - 2);
}

long long ref_fib_memo_helper(int n, unordered_map<int, long long>& memo) {
    if (n <= 1) return n;
    if (memo.count(n)) return memo[n];
    memo[n] = ref_fib_memo_helper(n - 1, memo) + ref_fib_memo_helper(n - 2, memo);
    return memo[n];
}

long long ref_fib_memo(int n) {
    unordered_map<int, long long> memo;
    return ref_fib_memo_helper(n, memo);
}

long long ref_fib_iter(int n) {
    if (n <= 1) return n;
    long long a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        long long temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

// --- C2: Generate Permutations ---
void ref_perm_bt(vector<int>& nums, int start, vector<vector<int>>& result) {
    if (start == (int)nums.size()) {
        result.push_back(nums);
        return;
    }
    for (int i = start; i < (int)nums.size(); i++) {
        swap(nums[start], nums[i]);
        ref_perm_bt(nums, start + 1, result);
        swap(nums[start], nums[i]);
    }
}

vector<vector<int>> ref_generate_permutations(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    ref_perm_bt(nums, 0, result);
    sort(result.begin(), result.end());
    return result;
}

// --- C3: Combination Sum ---
void ref_combo_bt(const vector<int>& candidates, int target, int start,
                  vector<int>& current, vector<vector<int>>& result) {
    if (target == 0) {
        result.push_back(current);
        return;
    }
    for (int i = start; i < (int)candidates.size(); i++) {
        if (candidates[i] > target) break;
        current.push_back(candidates[i]);
        ref_combo_bt(candidates, target - candidates[i], i, current, result);
        current.pop_back();
    }
}

vector<vector<int>> ref_combination_sum(vector<int> candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> result;
    vector<int> current;
    ref_combo_bt(candidates, target, 0, current, result);
    sort(result.begin(), result.end());
    return result;
}

// --- C4: Subset Sum ---
bool ref_subset_sum_helper(const vector<int>& nums, int idx, int remaining) {
    if (remaining == 0) return true;
    if (idx == (int)nums.size()) return false;
    if (ref_subset_sum_helper(nums, idx + 1, remaining - nums[idx])) return true;
    return ref_subset_sum_helper(nums, idx + 1, remaining);
}

bool ref_subset_sum(vector<int> nums, int target) {
    return ref_subset_sum_helper(nums, 0, target);
}

// =====================================================================
// Test functions
// =====================================================================

void test_warmup_01() {
    assert(ref_factorial(0) == 1);
    assert(ref_factorial(1) == 1);
    assert(ref_factorial(5) == 120);
    assert(ref_factorial(10) == 3628800);
    assert(ref_factorial(13) == 6227020800LL);
    assert(ref_factorial(20) == 2432902008176640000LL);
    cout << "  test_warmup_01_factorial............. PASS" << endl;
}

void test_warmup_02() {
    assert(ref_sum_first_n(0) == 0);
    assert(ref_sum_first_n(1) == 1);
    assert(ref_sum_first_n(5) == 15);
    assert(ref_sum_first_n(100) == 5050);
    assert(ref_sum_first_n(10) == 55);
    cout << "  test_warmup_02_sum_first_n........... PASS" << endl;
}

void test_warmup_03() {
    assert(ref_reverse_string("hello") == "olleh");
    assert(ref_reverse_string("") == "");
    assert(ref_reverse_string("a") == "a");
    assert(ref_reverse_string("abcdef") == "fedcba");
    assert(ref_reverse_string("ab") == "ba");
    cout << "  test_warmup_03_reverse_string........ PASS" << endl;
}

void test_warmup_04() {
    assert(ref_check_palindrome("racecar") == true);
    assert(ref_check_palindrome("hello") == false);
    assert(ref_check_palindrome("") == true);
    assert(ref_check_palindrome("a") == true);
    assert(ref_check_palindrome("aa") == true);
    assert(ref_check_palindrome("ab") == false);
    assert(ref_check_palindrome("abba") == true);
    assert(ref_check_palindrome("abca") == false);
    cout << "  test_warmup_04_check_palindrome...... PASS" << endl;
}

void test_warmup_05() {
    assert(ref_power(2, 0) == 1);
    assert(ref_power(2, 10) == 1024);
    assert(ref_power(3, 4) == 81);
    assert(ref_power(5, 3) == 125);
    assert(ref_power(1, 20) == 1);
    assert(ref_power(10, 5) == 100000);
    cout << "  test_warmup_05_power................. PASS" << endl;
}

void test_practice_01() {
    assert(ref_fibonacci(0) == 0);
    assert(ref_fibonacci(1) == 1);
    assert(ref_fibonacci(2) == 1);
    assert(ref_fibonacci(10) == 55);
    assert(ref_fibonacci(15) == 610);
    assert(ref_fibonacci(20) == 6765);
    cout << "  test_practice_01_fibonacci........... PASS" << endl;
}

void test_practice_02() {
    assert(ref_sum_digits(12345) == 15);
    assert(ref_sum_digits(0) == 0);
    assert(ref_sum_digits(999) == 27);
    assert(ref_sum_digits(-123) == 6);
    assert(ref_sum_digits(7) == 7);
    assert(ref_sum_digits(100) == 1);
    cout << "  test_practice_02_sum_digits.......... PASS" << endl;
}

void test_practice_03() {
    assert(ref_count_occurrences({1,2,3,2,4,2}, 2) == 3);
    assert(ref_count_occurrences({1,2,3}, 4) == 0);
    assert(ref_count_occurrences({}, 1) == 0);
    assert(ref_count_occurrences({5,5,5,5,5}, 5) == 5);
    assert(ref_count_occurrences({1}, 1) == 1);
    assert(ref_count_occurrences({1}, 2) == 0);
    cout << "  test_practice_03_count_occurrences... PASS" << endl;
}

void test_practice_04() {
    assert(ref_binary_search({1,3,5,7,9}, 5) == 2);
    assert(ref_binary_search({1,3,5,7,9}, 4) == -1);
    assert(ref_binary_search({}, 1) == -1);
    assert(ref_binary_search({1,3,5,7,9}, 1) == 0);
    assert(ref_binary_search({1,3,5,7,9}, 9) == 4);
    assert(ref_binary_search({42}, 42) == 0);
    assert(ref_binary_search({42}, 10) == -1);
    cout << "  test_practice_04_binary_search....... PASS" << endl;
}

void test_practice_05() {
    // Empty input
    vector<vector<int>> r1 = ref_generate_subsets({});
    assert(r1.size() == 1);
    assert(r1[0].empty());

    // Single element
    vector<vector<int>> r2 = ref_generate_subsets({1});
    assert(r2.size() == 2);
    vector<vector<int>> expected2 = {{}, {1}};
    assert(r2 == expected2);

    // Three elements
    vector<vector<int>> r3 = ref_generate_subsets({1, 2, 3});
    assert((int)r3.size() == 8);
    vector<vector<int>> expected3 = {{}, {1}, {1,2}, {1,2,3}, {1,3}, {2}, {2,3}, {3}};
    assert(r3 == expected3);

    // Unsorted input should still produce sorted output
    vector<vector<int>> r4 = ref_generate_subsets({3, 1, 2});
    assert((int)r4.size() == 8);
    assert(r4 == expected3);

    cout << "  test_practice_05_generate_subsets.... PASS" << endl;
}

void test_challenge_01() {
    // Naive -- small n only
    assert(ref_fib_naive(0) == 0);
    assert(ref_fib_naive(1) == 1);
    assert(ref_fib_naive(10) == 55);
    assert(ref_fib_naive(15) == 610);

    // Memo -- can handle larger n
    assert(ref_fib_memo(0) == 0);
    assert(ref_fib_memo(1) == 1);
    assert(ref_fib_memo(10) == 55);
    assert(ref_fib_memo(30) == 832040);
    assert(ref_fib_memo(40) == 102334155);

    // Iter -- can handle larger n
    assert(ref_fib_iter(0) == 0);
    assert(ref_fib_iter(1) == 1);
    assert(ref_fib_iter(10) == 55);
    assert(ref_fib_iter(30) == 832040);
    assert(ref_fib_iter(50) == 12586269025LL);

    // All three agree on small values
    for (int n = 0; n <= 15; n++) {
        long long naive = ref_fib_naive(n);
        long long memo = ref_fib_memo(n);
        long long iter = ref_fib_iter(n);
        assert(naive == memo);
        assert(memo == iter);
    }

    cout << "  test_challenge_01_fib_three_ways..... PASS" << endl;
}

void test_challenge_02() {
    // Single element
    vector<vector<int>> r1 = ref_generate_permutations({1});
    assert(r1.size() == 1);
    assert(r1[0] == (vector<int>{1}));

    // Two elements
    vector<vector<int>> r2 = ref_generate_permutations({1, 2});
    assert(r2.size() == 2);
    vector<vector<int>> exp2 = {{1,2}, {2,1}};
    assert(r2 == exp2);

    // Three elements
    vector<vector<int>> r3 = ref_generate_permutations({1, 2, 3});
    assert(r3.size() == 6);
    vector<vector<int>> exp3 = {
        {1,2,3}, {1,3,2}, {2,1,3}, {2,3,1}, {3,1,2}, {3,2,1}
    };
    assert(r3 == exp3);

    // Unsorted input
    vector<vector<int>> r4 = ref_generate_permutations({3, 1, 2});
    assert(r4.size() == 6);
    assert(r4 == exp3);

    cout << "  test_challenge_02_gen_permutations... PASS" << endl;
}

void test_challenge_03() {
    // Standard case
    vector<vector<int>> r1 = ref_combination_sum({2, 3, 6, 7}, 7);
    vector<vector<int>> exp1 = {{2,2,3}, {7}};
    assert(r1 == exp1);

    // Multiple combinations
    vector<vector<int>> r2 = ref_combination_sum({2, 3, 5}, 8);
    vector<vector<int>> exp2 = {{2,2,2,2}, {2,3,3}, {3,5}};
    assert(r2 == exp2);

    // No combinations
    vector<vector<int>> r3 = ref_combination_sum({2}, 1);
    assert(r3.empty());

    // Single candidate equals target
    vector<vector<int>> r4 = ref_combination_sum({3}, 3);
    vector<vector<int>> exp4 = {{3}};
    assert(r4 == exp4);

    // Single candidate repeated
    vector<vector<int>> r5 = ref_combination_sum({2}, 4);
    vector<vector<int>> exp5 = {{2,2}};
    assert(r5 == exp5);

    cout << "  test_challenge_03_combination_sum.... PASS" << endl;
}

void test_challenge_04() {
    assert(ref_subset_sum({3,34,4,12,5,2}, 9) == true);
    assert(ref_subset_sum({3,34,4,12,5,2}, 30) == false);
    assert(ref_subset_sum({}, 0) == true);
    assert(ref_subset_sum({1,2,3}, 6) == true);
    assert(ref_subset_sum({1,2,3}, 7) == false);
    assert(ref_subset_sum({5}, 5) == true);
    assert(ref_subset_sum({5}, 3) == false);
    assert(ref_subset_sum({1,2,3,4,5}, 10) == true);
    assert(ref_subset_sum({1,2,3,4,5}, 16) == false);
    cout << "  test_challenge_04_subset_sum......... PASS" << endl;
}

// =====================================================================
// Main -- run all tests
// =====================================================================
int main() {
    cout << "Testing Chapter 10..." << endl;
    cout << endl;

    cout << "--- Warmup Problems ---" << endl;
    test_warmup_01();
    test_warmup_02();
    test_warmup_03();
    test_warmup_04();
    test_warmup_05();
    cout << endl;

    cout << "--- Practice Problems ---" << endl;
    test_practice_01();
    test_practice_02();
    test_practice_03();
    test_practice_04();
    test_practice_05();
    cout << endl;

    cout << "--- Challenge Problems ---" << endl;
    test_challenge_01();
    test_challenge_02();
    test_challenge_03();
    test_challenge_04();
    cout << endl;

    cout << "All tests passed!" << endl;
    return 0;
}
