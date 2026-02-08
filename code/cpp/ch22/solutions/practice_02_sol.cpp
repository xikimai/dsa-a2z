/*
 * Solution for Practice 2: Evaluate Reverse Polish Notation
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: Stack — push numbers, pop two on operator, push result.
 * TIME: O(n), SPACE: O(n)
 */
#include <iostream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int solve(vector<string> tokens) {
    stack<int> stk;
    for (const string& t : tokens) {
        if (t == "+" || t == "-" || t == "*" || t == "/") {
            int b = stk.top(); stk.pop();
            int a = stk.top(); stk.pop();
            if (t == "+") stk.push(a + b);
            else if (t == "-") stk.push(a - b);
            else if (t == "*") stk.push(a * b);
            else stk.push(a / b);
        } else {
            stk.push(stoi(t));
        }
    }
    return stk.top();
}

int main() {
    int n;
    cin >> n;
    vector<string> tokens(n);
    for (int i = 0; i < n; i++) cin >> tokens[i];
    cout << solve(tokens) << endl;
    return 0;
}
