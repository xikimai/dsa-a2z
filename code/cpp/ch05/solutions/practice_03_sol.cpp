/*
 * Solution -- Practice 3: Two Sum
 * ================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   Use an unordered_map to store each number's index. For each element,
 *   compute the complement (target - nums[i]) and check if we've seen
 *   it before. If yes, return both indices. One pass.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(n) for the hash map
 */

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> solve(vector<int>& nums, int target) {
    unordered_map<int, int> seen;  // value -> index
    for (int i = 0; i < (int)nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.count(complement)) {
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {-1, -1};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    int target;
    cin >> target;
    vector<int> result = solve(nums, target);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
