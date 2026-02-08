/*
 * Challenge 1: Largest Rectangle in Histogram
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Given bar heights, find area of the largest rectangle.
 * EXAMPLES: solve({2,1,5,6,2,3}) -> 10
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int solve(vector<int> heights) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int n;
    cin >> n;
    vector<int> heights(n);
    for (int i = 0; i < n; i++) cin >> heights[i];
    cout << solve(heights) << endl;
    return 0;
}
