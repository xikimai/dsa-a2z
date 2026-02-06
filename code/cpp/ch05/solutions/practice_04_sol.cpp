/*
 * Solution -- Practice 4: Sort by Frequency
 * ===========================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   1. Build a frequency map.
 *   2. Sort the array with a custom comparator:
 *      - Higher frequency first
 *      - On tie, smaller value first
 *
 * TIME COMPLEXITY:  O(n log n)
 * SPACE COMPLEXITY: O(n) for the frequency map
 */

#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> solve(vector<int>& nums) {
    unordered_map<int, int> freq;
    for (int x : nums) freq[x]++;

    vector<int> result = nums;
    sort(result.begin(), result.end(), [&freq](int a, int b) {
        if (freq[a] != freq[b]) return freq[a] > freq[b];  // higher freq first
        return a < b;  // smaller value first on tie
    });
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<int> result = solve(nums);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
