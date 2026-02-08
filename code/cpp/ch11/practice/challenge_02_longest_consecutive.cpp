/*
 * Challenge 2: Longest Consecutive Sequence
 * ===========================================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given an unsorted array of integers, find the length of the longest
 *   consecutive elements sequence. Must run in O(n) time using a hash set.
 *
 * EXAMPLES:
 *   solve({100,4,200,1,3,2})            -> 4   (sequence: 1,2,3,4)
 *   solve({0,3,7,2,5,8,4,6,0,1})       -> 9   (sequence: 0-8)
 *   solve({})                           -> 0
 *   solve({1})                          -> 1
 *   solve({9,1,4,7,3,-1,0,5,8,-1,6})   -> 11  (sequence: -1 to 9)
 *
 * CONSTRAINTS:
 *   - 0 <= nums.size() <= 10^5
 *   - -10^9 <= nums[i] <= 10^9
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
    return 0;
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
