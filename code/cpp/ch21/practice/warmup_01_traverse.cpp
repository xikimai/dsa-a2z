/*
 * Warmup 1: Traverse Linked List
 * Chapter 21: Linked Lists — Pointers and Connections
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> res = solve(arr);
    for (int i = 0; i < (int)res.size(); i++) cout << (i ? " " : "") << res[i];
    cout << endl;
    return 0;
}
