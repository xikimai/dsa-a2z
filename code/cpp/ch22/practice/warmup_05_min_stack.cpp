/*
 * Warmup 5: Min Stack
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Implement a stack with push, pop, top, getMin in O(1).
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(vector<pair<string,int>> operations) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    vector<pair<string,int>> ops = {{"push",-2},{"push",0},{"push",-3},
                                    {"getMin",0},{"pop",0},{"top",0},{"getMin",0}};
    vector<int> result = solve(ops);
    for (int r : result) cout << r << " ";
    cout << endl;
    return 0;
}
