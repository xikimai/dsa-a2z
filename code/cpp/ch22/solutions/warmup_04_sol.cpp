/*
 * Solution for Warmup 4: Next Greater Element
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: Monotonic stack, process right to left.
 * TIME: O(n), SPACE: O(n)
 */
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    int n = arr.size();
    vector<int> result(n, -1);
    stack<int> stk;
    for (int i = n - 1; i >= 0; i--) {
        while (!stk.empty() && arr[stk.top()] <= arr[i]) stk.pop();
        if (!stk.empty()) result[i] = arr[stk.top()];
        stk.push(i);
    }
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int x : solve(arr)) cout << x << " ";
    cout << endl;
    return 0;
}
