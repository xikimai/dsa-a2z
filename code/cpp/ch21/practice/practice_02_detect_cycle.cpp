/*
 * Practice 2: Detect Cycle
 * Chapter 21: Linked Lists — Pointers and Connections
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> arr, int cyclePos) {
    // TODO: Replace this with your solution
    return false;
}

int main() {
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int cyclePos; cin >> cyclePos;
    cout << (solve(arr, cyclePos) ? "true" : "false") << endl;
    return 0;
}
