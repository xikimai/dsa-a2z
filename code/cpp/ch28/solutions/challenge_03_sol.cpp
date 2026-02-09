/*
 * Solution for Challenge 3: Largest Color Value in Directed Graph
 * Chapter 28: Topological Sort — Ordering Dependencies
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

int solve(string colors, vector<vector<int>>& edges) {
    int n = colors.size();
    vector<vector<int>> adj(n);
    vector<int> inDeg(n, 0);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        inDeg[e[1]]++;
    }

    vector<vector<int>> dp(n, vector<int>(26, 0));
    queue<int> q;
    for (int i = 0; i < n; i++)
        if (inDeg[i] == 0) q.push(i);

    int count = 0, result = 0;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        count++;
        dp[u][colors[u] - 'a']++;
        for (int c = 0; c < 26; c++)
            result = max(result, dp[u][c]);
        for (int v : adj[u]) {
            for (int c = 0; c < 26; c++)
                dp[v][c] = max(dp[v][c], dp[u][c]);
            if (--inDeg[v] == 0) q.push(v);
        }
    }
    return count == n ? result : -1;
}

int main() { return 0; }
