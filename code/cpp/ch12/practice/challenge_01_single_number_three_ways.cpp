/*
 * Challenge 1: Single Number — Three Ways
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * PROBLEM: Find single element using sort, hash, and XOR approaches.
 * CONSTRAINTS: 1 <= nums.size() <= 3*10^4
 */

#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int solve_sort(vector<int> nums) {
    // TODO: Replace this with your solution
    return 0;
}

int solve_hash(vector<int> nums) {
    // TODO: Replace this with your solution
    return 0;
}

int solve_xor(vector<int> nums) {
    // TODO: Replace this with your solution
    return 0;
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
