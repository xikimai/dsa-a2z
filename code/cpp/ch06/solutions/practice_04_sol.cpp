/*
 * Solution -- Practice 4: Majority Element
 * ==========================================
 * Chapter 6: How Fast Is Your Code?
 *
 * APPROACH:
 *   Boyer-Moore Voting Algorithm. Maintain a candidate and a count.
 *   If count drops to 0, pick the current element as the new candidate.
 *   Increment count if the element matches the candidate, decrement
 *   otherwise. The final candidate is the majority element.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int>& nums) {
    int candidate = 0;
    int count = 0;

    for (int x : nums) {
        if (count == 0) {
            candidate = x;
        }
        count += (x == candidate) ? 1 : -1;
    }

    return candidate;
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
