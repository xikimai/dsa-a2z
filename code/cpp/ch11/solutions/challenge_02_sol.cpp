/*
 * Solution for Challenge 2: Longest Consecutive Sequence
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Insert all numbers into an unordered_set. For each number
 *           that is the START of a sequence (num-1 not in set), count
 *           how far the sequence extends. Track the maximum length.
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
    if (nums.empty()) return 0;
    unordered_set<int> s(nums.begin(), nums.end());
    int best = 0;
    for (int num : s) {
        // Only start counting from the beginning of a sequence
        if (!s.count(num - 1)) {
            int current = num;
            int length = 1;
            while (s.count(current + 1)) {
                current++;
                length++;
            }
            best = max(best, length);
        }
    }
    return best;
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
