/*
 * Challenge 2: Two Numbers Appearing Odd Times
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * PROBLEM: Find two odd-occurring elements. Return sorted.
 * EXAMPLES: solve({2,4,7,9,2,4}) -> {7,9}
 * CONSTRAINTS: 2 <= nums.size() <= 3*10^4
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> nums) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<int> result = solve(nums);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}
