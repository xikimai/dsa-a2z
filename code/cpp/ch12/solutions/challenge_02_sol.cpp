/*
 * Solution for Challenge 2: Two Numbers Appearing Odd Times
 * TIME: O(n)   SPACE: O(1)
 */
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> nums) {
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

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    auto result = solve(nums);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}
