/*
 * Solution for Challenge 1: Single Number — Three Ways
 */
#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int solve_sort(vector<int> nums) {
    sort(nums.begin(), nums.end());
    for (int i = 0; i < (int)nums.size() - 1; i += 2) {
        if (nums[i] != nums[i + 1]) return nums[i];
    }
    return nums.back();
}

int solve_hash(vector<int> nums) {
    unordered_map<int, int> freq;
    for (int x : nums) freq[x]++;
    for (auto& [val, cnt] : freq) {
        if (cnt == 1) return val;
    }
    return -1;
}

int solve_xor(vector<int> nums) {
    int result = 0;
    for (int x : nums) result ^= x;
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << "Sort: " << solve_sort(nums) << endl;
    cout << "Hash: " << solve_hash(nums) << endl;
    cout << "XOR:  " << solve_xor(nums) << endl;
    return 0;
}
