/*
 * Solution for Practice 4: All Ancestors of a Node
 * Chapter 28: Topological Sort — Ordering Dependencies
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

vector<vector<int>> solve(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) adj[e[0]].push_back(e[1]);

    vector<set<int>> ancestors(n);

    for (int u = 0; u < n; u++) {
        stack<int> stk;
        stk.push(u);
        vector<bool> visited(n, false);
        while (!stk.empty()) {
            int node = stk.top(); stk.pop();
            for (int v : adj[node]) {
                if (!visited[v]) {
                    visited[v] = true;
                    ancestors[v].insert(u);
                    stk.push(v);
                }
            }
        }
    }

    vector<vector<int>> result(n);
    for (int i = 0; i < n; i++)
        result[i] = vector<int>(ancestors[i].begin(), ancestors[i].end());
    return result;
}

int main() { return 0; }
