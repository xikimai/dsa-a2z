/*
 * Solution for Challenge 3: Repeating and Missing Number
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Use an unordered_map to count frequencies. The number
 *           with count 2 is the repeating number, and the number
 *           with count 0 (in range [1, n]) is the missing number.
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

vector<int> solve(vector<int> nums) {
    int n = nums.size();
    unordered_map<int, int> freq;
    for (int x : nums) freq[x]++;
    int repeating = 0, missing = 0;
    for (int i = 1; i <= n; i++) {
        if (freq[i] == 2) repeating = i;
        if (freq[i] == 0) missing = i;
    }
    return {repeating, missing};
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
