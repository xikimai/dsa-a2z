/*
 * Practice 2: Evaluate Reverse Polish Notation
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Evaluate postfix expression. Division truncates toward zero.
 * EXAMPLES: solve({"2","1","+","3","*"}) -> 9
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int solve(vector<string> tokens) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int n;
    cin >> n;
    vector<string> tokens(n);
    for (int i = 0; i < n; i++) cin >> tokens[i];
    cout << solve(tokens) << endl;
    return 0;
}
