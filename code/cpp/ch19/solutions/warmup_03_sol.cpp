#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

void dfsHelper(vector<vector<int>>& adj, int node, vector<bool>& visited, vector<int>& order) {
    visited[node] = true;
    order.push_back(node);
    vector<int> nbrs = adj[node];
    sort(nbrs.begin(), nbrs.end());
    for (int nb : nbrs) {
        if (!visited[nb]) dfsHelper(adj, nb, visited, order);
    }
}

vector<int> solve(int n, vector<vector<int>>& edges, int source) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<bool> visited(n, false);
    vector<int> order;
    dfsHelper(adj, source, visited, order);
    return order;
}

int main() {
    int n, m, source; cin >> n >> m >> source;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    auto result = solve(n, edges, source);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
