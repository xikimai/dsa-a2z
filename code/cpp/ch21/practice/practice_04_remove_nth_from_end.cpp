/*
 * Practice 4: Remove Nth Node From End
 * Chapter 21: Linked Lists — Pointers and Connections
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr, int n) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int sz; cin >> sz;
    vector<int> arr(sz);
    for (int i = 0; i < sz; i++) cin >> arr[i];
    int n; cin >> n;
    vector<int> res = solve(arr, n);
    for (int i = 0; i < (int)res.size(); i++) cout << (i ? " " : "") << res[i];
    cout << endl;
    return 0;
}
