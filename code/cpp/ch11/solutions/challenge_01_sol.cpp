/*
 * Solution for Challenge 1: Missing Number Four Ways
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Four different techniques to find the missing number.
 *   1. Sort + scan:   O(n log n) time, O(1) space
 *   2. XOR:           O(n) time, O(1) space
 *   3. Math (Gauss):  O(n) time, O(1) space
 *   4. Hash set:      O(n) time, O(n) space
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

int solve_sort(vector<int> nums) {
    sort(nums.begin(), nums.end());
    for (int i = 0; i < (int)nums.size(); i++) {
        if (nums[i] != i) return i;
    }
    return (int)nums.size();
}

int solve_xor(vector<int> nums) {
    int n = nums.size();
    int result = n;  // start with n
    for (int i = 0; i < n; i++) {
        result ^= i ^ nums[i];
    }
    return result;
}

int solve_math(vector<int> nums) {
    int n = nums.size();
    long long expected = (long long)n * (n + 1) / 2;
    long long actual = 0;
    for (int x : nums) actual += x;
    return (int)(expected - actual);
}

int solve_hash(vector<int> nums) {
    unordered_set<int> seen(nums.begin(), nums.end());
    int n = nums.size();
    for (int i = 0; i <= n; i++) {
        if (!seen.count(i)) return i;
    }
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
