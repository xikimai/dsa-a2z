/*
 * Solution for Challenge 1: Minimum Height Trees
 * Chapter 28: Topological Sort — Ordering Dependencies
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(int n, vector<vector<int>>& edges) {
    if (n == 1) return {0};

    vector<set<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].insert(e[1]);
        adj[e[1]].insert(e[0]);
    }

    queue<int> leaves;
    for (int i = 0; i < n; i++)
        if ((int)adj[i].size() == 1) leaves.push(i);

    int remaining = n;
    while (remaining > 2) {
        int sz = leaves.size();
        remaining -= sz;
        queue<int> newLeaves;
        for (int i = 0; i < sz; i++) {
            int leaf = leaves.front(); leaves.pop();
            for (int neighbor : adj[leaf]) {
                adj[neighbor].erase(leaf);
                if ((int)adj[neighbor].size() == 1) newLeaves.push(neighbor);
            }
        }
        leaves = newLeaves;
    }

    vector<int> result;
    while (!leaves.empty()) {
        result.push_back(leaves.front());
        leaves.pop();
    }
    return result;
}

int main() { return 0; }
