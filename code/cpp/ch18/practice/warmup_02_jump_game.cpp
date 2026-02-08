/*
 * Warmup 2: Jump Game I
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Can you reach the last index?
 * EXAMPLES: solve({2,3,1,1,4}) -> true
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> nums) {
    // TODO: Replace this with your solution
    return false;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n; cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cout << (solve(nums) ? "true" : "false") << endl;
    return 0;
}
