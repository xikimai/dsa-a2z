/*
 * Solution for Challenge 3: Online Stock Span
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: Monotonic stack storing {price, span} pairs.
 * TIME: O(1) amortized per call, SPACE: O(n)
 */
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

vector<int> solve(vector<int> prices) {
    stack<pair<int,int>> stk; // {price, span}
    vector<int> result;
    for (int price : prices) {
        int span = 1;
        while (!stk.empty() && stk.top().first <= price) {
            span += stk.top().second;
            stk.pop();
        }
        stk.push({price, span});
        result.push_back(span);
    }
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> prices(n);
    for (int i = 0; i < n; i++) cin >> prices[i];
    for (int x : solve(prices)) cout << x << " ";
    cout << endl;
    return 0;
}
