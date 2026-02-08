#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<bool> visited(n, false);
    int count = 0;
    for (int v = 0; v < n; v++) {
        if (!visited[v]) {
            queue<int> q;
            q.push(v);
            visited[v] = true;
            while (!q.empty()) {
                int node = q.front(); q.pop();
                for (int nb : adj[node]) {
                    if (!visited[nb]) { visited[nb] = true; q.push(nb); }
                }
            }
            count++;
        }
    }
    return count;
}

int main() {
    int n, m; cin >> n >> m;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    cout << solve(n, edges) << endl;
    return 0;
}
