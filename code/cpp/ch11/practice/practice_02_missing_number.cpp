/*
 * Practice 2: Missing Number
 * ===========================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given an array containing n distinct numbers in the range [0, n],
 *   return the one number that is missing from the array.
 *   Use a hash set approach.
 *
 * EXAMPLES:
 *   solve({3,0,1})                -> 2
 *   solve({0,1})                  -> 2
 *   solve({9,6,4,2,3,5,7,0,1})   -> 8
 *   solve({0})                    -> 1
 *
 * CONSTRAINTS:
 *   - n == nums.size()
 *   - 0 <= n <= 10^4
 *   - All numbers are unique
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

int solve(vector<int> nums) {
    // TODO: Replace this with your solution
    return -1;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << solve(nums) << endl;
    return 0;
}
