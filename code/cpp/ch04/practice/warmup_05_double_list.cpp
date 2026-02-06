/*
 * Warmup 5: Double List
 * =====================
 * Chapter 4: Functions
 *
 * PROBLEM:
 *   Double every element in a vector IN PLACE (using pass-by-reference)
 *   and also return the modified vector.
 *
 * EXAMPLES:
 *   solve({1, 2, 3})     -> {2, 4, 6}     (original also becomes {2, 4, 6})
 *   solve({0, -1, 5})    -> {0, -2, 10}
 *   solve({})            -> {}
 *
 * CONSTRAINTS:
 *   - The function takes a reference (vector<int>&), so it modifies the original
 *   - It also returns the vector for convenience
 *
 * NOTE:
 *   The '&' in the parameter means pass-by-reference. The original vector
 *   is modified directly — no copy is made!
 */

#include <iostream>
#include <vector>
using namespace std;

/**
 * Doubles every element in nums in place and returns the vector.
 */
vector<int> solve(vector<int>& nums) {
    // TODO: Replace this with your solution
    return nums;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    vector<int> result = solve(nums);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
