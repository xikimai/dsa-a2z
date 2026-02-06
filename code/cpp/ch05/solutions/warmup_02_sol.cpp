/*
 * Solution -- Warmup 2: Reverse List
 * ====================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   Two-pointer swap. Start with left=0, right=size-1. Swap elements
 *   and move pointers inward until they meet.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(1) — in-place swap
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int>& nums) {
    int left = 0;
    int right = (int)nums.size() - 1;
    while (left < right) {
        swap(nums[left], nums[right]);
        left++;
        right--;
    }
    return nums;
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
