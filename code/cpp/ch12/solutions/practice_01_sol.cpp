/*
 * Solution for Practice 1: Single Number (XOR)
 * TIME: O(n)   SPACE: O(1)
 */
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> nums) {
    int result = 0;
    for (int x : nums) result ^= x;
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << solve(nums) << endl;
    return 0;
}
