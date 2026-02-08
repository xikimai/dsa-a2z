/*
 * Challenge 3: Add Two Numbers
 * Chapter 21: Linked Lists — Pointers and Connections
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr1, vector<int> arr2) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int n1; cin >> n1;
    vector<int> arr1(n1);
    for (int i = 0; i < n1; i++) cin >> arr1[i];
    int n2; cin >> n2;
    vector<int> arr2(n2);
    for (int i = 0; i < n2; i++) cin >> arr2[i];
    vector<int> res = solve(arr1, arr2);
    for (int i = 0; i < (int)res.size(); i++) cout << (i ? " " : "") << res[i];
    cout << endl;
    return 0;
}
