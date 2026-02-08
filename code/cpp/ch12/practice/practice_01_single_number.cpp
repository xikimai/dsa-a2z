/*
 * Practice 1: Single Number
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * PROBLEM: Every element appears twice except one. Find it.
 * EXAMPLES: solve({4,1,2,1,2})=4, solve({2,2,1})=1
 * CONSTRAINTS: 1 <= nums.size() <= 3*10^4
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> nums) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << solve(nums) << endl;
    return 0;
}
