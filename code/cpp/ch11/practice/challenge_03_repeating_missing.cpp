/*
 * Challenge 3: Repeating and Missing Number
 * ===========================================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given an array of n integers where elements are in range [1, n],
 *   one number appears twice and one is missing. Return {repeating, missing}.
 *
 * EXAMPLES:
 *   solve({3,1,2,5,3})    -> {3,4}
 *   solve({1,1})           -> {1,2}
 *   solve({2,2})           -> {2,1}
 *   solve({4,3,6,2,1,1})  -> {1,5}
 *
 * CONSTRAINTS:
 *   - 2 <= nums.size() <= 10^5
 *   - 1 <= nums[i] <= n
 *   - Exactly one number repeats, exactly one is missing
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

vector<int> solve(vector<int> nums) {
    // TODO: Replace this with your solution
    return {0, 0};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<int> result = solve(nums);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
