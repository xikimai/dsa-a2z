/*
 * Solution for Warmup 5: Min Stack
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: Two stacks — main and min (parallel tracking).
 * TIME: O(1) per op, SPACE: O(n)
 */
#include <climits>
#include <iostream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(vector<pair<string,int>> operations) {
    stack<int> stk, minStk;
    vector<int> results;
    for (auto& [op, val] : operations) {
        if (op == "push") {
            stk.push(val);
            if (minStk.empty() || val <= minStk.top())
                minStk.push(val);
            else
                minStk.push(minStk.top());
        } else if (op == "pop") {
            stk.pop();
            minStk.pop();
        } else if (op == "top") {
            results.push_back(stk.top());
        } else if (op == "getMin") {
            results.push_back(minStk.top());
        }
    }
    return results;
}

int main() {
    vector<pair<string,int>> ops = {{"push",-2},{"push",0},{"push",-3},
                                    {"getMin",0},{"pop",0},{"top",0},{"getMin",0}};
    for (int r : solve(ops)) cout << r << " ";
    cout << endl;
    return 0;
}
