/*
 * Warmup 3: Implement Queue Using Array
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Implement queue operations: enqueue, dequeue, front, is_empty.
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
    vector<pair<string,int>> ops = {{"enqueue",1},{"enqueue",2},{"front",0},{"dequeue",0},{"is_empty",0}};
    vector<int> result = solve(ops);
    for (int r : result) cout << r << " ";
    cout << endl;
    return 0;
}
