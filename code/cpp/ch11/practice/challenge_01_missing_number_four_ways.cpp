/*
 * Challenge 1: Missing Number Four Ways
 * =======================================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given an array containing n distinct numbers in the range [0, n],
 *   find the missing number using FOUR different techniques:
 *     1. solve_sort  — sort then scan
 *     2. solve_xor   — XOR all indices and values
 *     3. solve_math  — Gauss formula: n*(n+1)/2 - sum
 *     4. solve_hash  — hash set lookup
 *   Also provide solve() which delegates to solve_math.
 *
 * EXAMPLES:
 *   solve({3,0,1})  -> 2
 *   solve({0,1})    -> 2
 *   solve({1})      -> 0
 *   solve({0})      -> 1
 *
 * CONSTRAINTS:
 *   - n == nums.size()
 *   - 0 <= n <= 10^4
 *   - All numbers are unique
 *
 * INSTRUCTIONS:
 *   Replace the body of each function with your solution.
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

int solve_sort(vector<int> nums) {
    // TODO: Replace this with your solution
    return -1;
}

int solve_xor(vector<int> nums) {
    // TODO: Replace this with your solution
    return -1;
}

int solve_math(vector<int> nums) {
    // TODO: Replace this with your solution
    return -1;
}

int solve_hash(vector<int> nums) {
    // TODO: Replace this with your solution
    return -1;
}

int solve(vector<int> nums) {
    return solve_math(nums);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << "sort: " << solve_sort(nums) << endl;
    cout << "xor:  " << solve_xor(nums) << endl;
    cout << "math: " << solve_math(nums) << endl;
    cout << "hash: " << solve_hash(nums) << endl;
    return 0;
}
