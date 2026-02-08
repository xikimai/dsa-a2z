/*
 * Challenge 4: Flatten a Multilevel Doubly Linked List
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * Uses a simple recursive representation: a nested vector structure.
 * Since C++ doesn't have a built-in heterogeneous list, we use a
 * special encoding: positive values are data, INT_MIN marks the
 * start of a sublist, INT_MIN+1 marks the end.
 *
 * For simplicity in testing, we use a flat vector<int> input where
 * -999999 means "start sublist" and -999998 means "end sublist".
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <vector>
using namespace std;

static const int BEGIN_LIST = -999999;
static const int END_LIST = -999998;

vector<int> solve(vector<int> encoded) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int n; cin >> n;
    vector<int> encoded(n);
    for (int i = 0; i < n; i++) cin >> encoded[i];
    vector<int> res = solve(encoded);
    for (int i = 0; i < (int)res.size(); i++) cout << (i ? " " : "") << res[i];
    cout << endl;
    return 0;
}
