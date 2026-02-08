/*
 * Solution for Practice 2: Missing Number
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Insert all numbers into an unordered_set, then check
 *           which number in [0, n] is missing.
 * TIME:  O(n)
 * SPACE: O(n)
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

int solve(vector<int> nums) {
    unordered_set<int> seen(nums.begin(), nums.end());
    int n = nums.size();
    for (int i = 0; i <= n; i++) {
        if (!seen.count(i)) return i;
    }
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
