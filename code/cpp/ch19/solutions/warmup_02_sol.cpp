#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> solve(int n, vector<vector<int>>& edges, int source) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<bool> visited(n, false);
    visited[source] = true;
    queue<int> q;
    q.push(source);
    vector<int> order;
    while (!q.empty()) {
        int node = q.front(); q.pop();
        order.push_back(node);
        vector<int> nbrs = adj[node];
        sort(nbrs.begin(), nbrs.end());
        for (int nb : nbrs) {
            if (!visited[nb]) { visited[nb] = true; q.push(nb); }
        }
    }
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
