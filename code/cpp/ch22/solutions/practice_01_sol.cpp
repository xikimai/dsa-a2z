/*
 * Solution for Practice 1: Daily Temperatures
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: Monotonic stack of indices, process left to right.
 * TIME: O(n), SPACE: O(n)
 */
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

vector<int> solve(vector<int> temperatures) {
    int n = temperatures.size();
    vector<int> result(n, 0);
    stack<int> stk;
    for (int i = 0; i < n; i++) {
        while (!stk.empty() && temperatures[stk.top()] < temperatures[i]) {
            int j = stk.top(); stk.pop();
            result[j] = i - j;
        }
        stk.push(i);
    }
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> temps(n);
    for (int i = 0; i < n; i++) cin >> temps[i];
    for (int x : solve(temps)) cout << x << " ";
    cout << endl;
    return 0;
}
