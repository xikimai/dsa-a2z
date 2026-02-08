/*
 * Practice 3: Sliding Window Maximum
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Given array and window size k, return max of each window.
 * EXAMPLES: solve({1,3,-1,-3,5,3,6,7}, 3) -> {3,3,5,5,6,7}
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <deque>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> nums, int k) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int n, k;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    cin >> k;
    vector<int> result = solve(nums, k);
    for (int x : result) cout << x << " ";
    cout << endl;
    return 0;
}
