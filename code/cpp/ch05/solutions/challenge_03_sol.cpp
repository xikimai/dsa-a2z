/*
 * Solution -- Challenge 3: Rotate Array
 * =======================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   The "three-reverse" trick:
 *   1. Normalize k = k % n (handle k > size)
 *   2. Reverse the entire array
 *   3. Reverse the first k elements
 *   4. Reverse the remaining n-k elements
 *
 *   Example: [1,2,3,4,5,6,7], k=3
 *     Reverse all:     [7,6,5,4,3,2,1]
 *     Reverse first 3: [5,6,7,4,3,2,1]
 *     Reverse last 4:  [5,6,7,1,2,3,4]
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(1) — in-place
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int>& nums, int k) {
    int n = (int)nums.size();
    if (n == 0) return nums;

    k = k % n;
    if (k == 0) return nums;

    // Reverse entire array
    reverse(nums.begin(), nums.end());
    // Reverse first k
    reverse(nums.begin(), nums.begin() + k);
    // Reverse remaining n-k
    reverse(nums.begin() + k, nums.end());

    return nums;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    int k;
    cin >> k;
    vector<int> result = solve(nums, k);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
