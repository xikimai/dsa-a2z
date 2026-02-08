/*
 * Practice 5: Jump Game II
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Minimum jumps to reach last index.
 * EXAMPLES: solve({2,3,1,1,4}) -> 2
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> nums) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n; cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << solve(nums) << endl;
    return 0;
}
