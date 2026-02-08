/*
 * Warmup 3: Delete Node at Position
 * Chapter 21: Linked Lists — Pointers and Connections
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr, int pos) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int pos; cin >> pos;
    vector<int> res = solve(arr, pos);
    for (int i = 0; i < (int)res.size(); i++) cout << (i ? " " : "") << res[i];
    cout << endl;
    return 0;
}
