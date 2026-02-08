/*
 * Challenge 2: Trapping Rain Water
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Given elevation map, compute total trapped water.
 * EXAMPLES: solve({0,1,0,2,1,0,1,3,2,1,2,1}) -> 6
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> height) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int n;
    cin >> n;
    vector<int> height(n);
    for (int i = 0; i < n; i++) cin >> height[i];
    cout << solve(height) << endl;
    return 0;
}
