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
    vector<int> dist(n, -1);
    dist[source] = 0;
    queue<int> q;
    q.push(source);
    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (int nb : adj[node]) {
            if (dist[nb] == -1) {
                dist[nb] = dist[node] + 1;
                q.push(nb);
            }
        }
    }
    return dist;
}

int main() {
    int n, m, source; cin >> n >> m >> source;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    auto dist = solve(n, edges, source);
    for (int i = 0; i < n; i++) cout << dist[i] << " ";
    cout << endl;
    return 0;
}
