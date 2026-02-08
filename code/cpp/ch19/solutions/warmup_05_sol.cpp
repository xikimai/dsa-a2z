#include <iostream>
#include <queue>
#include <vector>
using namespace std;

bool solve(int n, vector<vector<int>>& edges, int source, int dest) {
    if (source == dest) return true;
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<bool> visited(n, false);
    visited[source] = true;
    queue<int> q;
    q.push(source);
    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (int nb : adj[node]) {
            if (nb == dest) return true;
            if (!visited[nb]) { visited[nb] = true; q.push(nb); }
        }
    }
    return false;
}

int main() {
    int n, m, source, dest; cin >> n >> m >> source >> dest;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    cout << (solve(n, edges, source, dest) ? "true" : "false") << endl;
    return 0;
}
