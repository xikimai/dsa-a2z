/*
 * Solution for Warmup 1: Valid Parentheses
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: Stack — push openers, pop on closers and check match.
 * TIME: O(n), SPACE: O(n)
 */
#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool solve(string s) {
    stack<char> stk;
    for (char ch : s) {
        if (ch == '(' || ch == '[' || ch == '{') {
            stk.push(ch);
        } else {
            if (stk.empty()) return false;
            char top = stk.top(); stk.pop();
            if ((ch == ')' && top != '(') ||
                (ch == ']' && top != '[') ||
                (ch == '}' && top != '{')) return false;
        }
    }
    return stk.empty();
}

int main() {
    string s;
    getline(cin, s);
    cout << (solve(s) ? "true" : "false") << endl;
    return 0;
}
