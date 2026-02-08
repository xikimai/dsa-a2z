/*
 * Example 01: Graph Representations
 * ===================================
 * Chapter 19: Graphs I — Exploring Networks
 *
 * Demonstrates:
 *   Part 1: Adjacency list
 *   Part 2: Adjacency matrix
 *   Part 3: Comparison and queries
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Graph:
    //   0 --- 1
    //   |     |
    //   2 --- 3
    //         |
    //         4
    int n = 5;
    vector<pair<int,int>> edges = {{0,1},{0,2},{1,3},{2,3},{3,4}};

    // ── Part 1: Adjacency List ─────────────────────
    cout << "=== Part 1: Adjacency List ===" << endl;
    vector<vector<int>> adj(n);
    for (auto& [u, v] : edges) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    for (int i = 0; i < n; i++) {
        cout << "  " << i << ": [";
        for (int j = 0; j < (int)adj[i].size(); j++) {
            if (j > 0) cout << ", ";
            cout << adj[i][j];
        }
        cout << "]" << endl;
    }
    cout << "  Space: O(V + 2E) = O(" << (n + 2 * (int)edges.size()) << ")" << endl;

    // ── Part 2: Adjacency Matrix ───────────────────
    cout << "\n=== Part 2: Adjacency Matrix ===" << endl;
    vector<vector<int>> matrix(n, vector<int>(n, 0));
    for (auto& [u, v] : edges) {
        matrix[u][v] = 1;
        matrix[v][u] = 1;
    }
    cout << "     ";
    for (int i = 0; i < n; i++) cout << i << "  ";
    cout << endl;
    for (int i = 0; i < n; i++) {
        cout << "  " << i << ": ";
        for (int j = 0; j < n; j++) cout << matrix[i][j] << "  ";
        cout << endl;
    }
    cout << "  Space: O(V^2) = O(" << (n * n) << ")" << endl;

    // ── Part 3: Queries ────────────────────────────
    cout << "\n=== Part 3: Queries ===" << endl;
    cout << "  Neighbors of node 3: ";
    for (int nb : adj[3]) cout << nb << " ";
    cout << endl;
    cout << "  Edge between 0 and 3? " << (matrix[0][3] ? "yes" : "no") << endl;
    cout << "  Degree of node 3: " << adj[3].size() << endl;

    return 0;
}
