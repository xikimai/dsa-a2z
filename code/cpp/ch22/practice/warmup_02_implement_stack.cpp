/*
 * Warmup 2: Implement Stack Using Array
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Implement stack operations: push, pop, top, is_empty.
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
    vector<pair<string,int>> ops = {{"push",1},{"push",2},{"top",0},{"pop",0},{"is_empty",0}};
    vector<int> result = solve(ops);
    for (int r : result) cout << r << " ";
    cout << endl;
    return 0;
}
