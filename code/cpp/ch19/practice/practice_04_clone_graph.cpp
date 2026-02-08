/*
 * Practice 4: Clone Graph
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Deep clone an adjacency list.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<vector<int>>& adj) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int n; cin >> n;
    vector<vector<int>> adj(n);
    for (int i = 0; i < n; i++) {
        int k; cin >> k;
        adj[i].resize(k);
        for (int j = 0; j < k; j++) cin >> adj[i][j];
    }
    auto clone = solve(adj);
    for (int i = 0; i < (int)clone.size(); i++) {
        cout << i << ": [";
        for (int j = 0; j < (int)clone[i].size(); j++) {
            if (j > 0) cout << ", ";
            cout << clone[i][j];
        }
        cout << "]" << endl;
    }
    return 0;
}
