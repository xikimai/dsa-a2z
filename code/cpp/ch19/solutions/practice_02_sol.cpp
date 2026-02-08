#include <iostream>
#include <vector>
using namespace std;

bool dfs(vector<vector<int>>& adj, int node, int parent, vector<bool>& visited) {
    visited[node] = true;
    for (int nb : adj[node]) {
        if (!visited[nb]) {
            if (dfs(adj, nb, node, visited)) return true;
        } else if (nb != parent) {
            return true;
        }
    }
    return false;
}

bool solve(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<bool> visited(n, false);
    for (int v = 0; v < n; v++) {
        if (!visited[v]) {
            if (dfs(adj, v, -1, visited)) return true;
        }
    }
    return false;
}

int main() {
    int n, m; cin >> n >> m;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    cout << (solve(n, edges) ? "true" : "false") << endl;
    return 0;
}
