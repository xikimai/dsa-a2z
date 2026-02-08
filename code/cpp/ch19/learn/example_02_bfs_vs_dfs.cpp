/*
 * Example 02: BFS vs DFS
 * ========================
 * Chapter 19: Graphs I — Exploring Networks
 *
 * Demonstrates:
 *   Part 1: BFS traversal
 *   Part 2: DFS traversal
 *   Part 3: BFS finds shortest paths, DFS does not
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

void dfsHelper(vector<vector<int>>& adj, int node,
               vector<bool>& visited, vector<int>& order) {
    visited[node] = true;
    order.push_back(node);
    vector<int> nbrs = adj[node];
    sort(nbrs.begin(), nbrs.end());
    for (int nb : nbrs) {
        if (!visited[nb]) dfsHelper(adj, nb, visited, order);
    }
}

int main() {
    int n = 5;
    vector<vector<int>> adj(n);
    int edges[][2] = {{0,1},{0,2},{1,3},{2,3},{3,4}};
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }

    // ── Part 1: BFS ───────────────────────────────
    cout << "=== Part 1: BFS from node 0 ===" << endl;
    vector<bool> visitedBfs(n, false);
    visitedBfs[0] = true;
    queue<int> q;
    q.push(0);
    vector<int> bfsOrder;
    while (!q.empty()) {
        int node = q.front(); q.pop();
        bfsOrder.push_back(node);
        vector<int> nbrs = adj[node];
        sort(nbrs.begin(), nbrs.end());
        for (int nb : nbrs) {
            if (!visitedBfs[nb]) {
                visitedBfs[nb] = true;
                q.push(nb);
            }
        }
    }
    cout << "  BFS order: ";
    for (int x : bfsOrder) cout << x << " ";
    cout << endl;

    // ── Part 2: DFS ───────────────────────────────
    cout << "\n=== Part 2: DFS from node 0 ===" << endl;
    vector<bool> visitedDfs(n, false);
    vector<int> dfsOrder;
    dfsHelper(adj, 0, visitedDfs, dfsOrder);
    cout << "  DFS order: ";
    for (int x : dfsOrder) cout << x << " ";
    cout << endl;

    // ── Part 3: Shortest Paths ────────────────────
    cout << "\n=== Part 3: Shortest Paths ===" << endl;
    // Smaller graph: 0-1, 0-2, 1-3, 2-3
    int m = 4;
    vector<vector<int>> adj2(m);
    adj2[0].push_back(1); adj2[1].push_back(0);
    adj2[0].push_back(2); adj2[2].push_back(0);
    adj2[1].push_back(3); adj2[3].push_back(1);
    adj2[2].push_back(3); adj2[3].push_back(2);

    vector<int> dist(m, -1);
    dist[0] = 0;
    queue<int> q2;
    q2.push(0);
    while (!q2.empty()) {
        int node = q2.front(); q2.pop();
        for (int nb : adj2[node]) {
            if (dist[nb] == -1) {
                dist[nb] = dist[node] + 1;
                q2.push(nb);
            }
        }
    }
    cout << "  BFS distances from 0: ";
    for (int d : dist) cout << d << " ";
    cout << endl;
    cout << "  BFS is CORRECT for shortest paths!" << endl;

    return 0;
}
