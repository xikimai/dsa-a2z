/*
 * Solution -- Warmup 6: Move Zeros
 * ==================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   Use a write pointer. Scan through the array; whenever we find a
 *   non-zero element, write it at the write pointer and advance.
 *   After the scan, fill the rest with zeros.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(1) — in-place
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int>& nums) {
    int write = 0;
    for (int i = 0; i < (int)nums.size(); i++) {
        if (nums[i] != 0) {
            nums[write] = nums[i];
            write++;
        }
    }
    // Fill remaining positions with zeros
    while (write < (int)nums.size()) {
        nums[write] = 0;
        write++;
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
