/*
 * Solution for Practice 2: Parallel Courses
 * Chapter 28: Topological Sort — Ordering Dependencies
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

int solve(int n, vector<vector<int>>& relations) {
    vector<vector<int>> adj(n + 1);
    vector<int> inDeg(n + 1, 0);
    for (auto& r : relations) {
        adj[r[0]].push_back(r[1]);
        inDeg[r[1]]++;
    }
    queue<int> q;
    for (int i = 1; i <= n; i++)
        if (inDeg[i] == 0) q.push(i);
    int semesters = 0, count = 0;
    while (!q.empty()) {
        semesters++;
        int sz = q.size();
        for (int i = 0; i < sz; i++) {
            int u = q.front(); q.pop();
            count++;
            for (int v : adj[u])
                if (--inDeg[v] == 0) q.push(v);
        }
    }
    return count == n ? semesters : -1;
}

int main() { return 0; }
