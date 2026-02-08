#include <iostream>
#include <queue>
#include <vector>
using namespace std;

bool solve(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    vector<int> color(n, -1);
    for (int start = 0; start < n; start++) {
        if (color[start] != -1) continue;
        color[start] = 0;
        queue<int> q;
        q.push(start);
        while (!q.empty()) {
            int node = q.front(); q.pop();
            for (int nb : adj[node]) {
                if (color[nb] == -1) {
                    color[nb] = 1 - color[node];
                    q.push(nb);
                } else if (color[nb] == color[node]) {
                    return false;
                }
            }
        }
    }
    return true;
}

int main() {
    int n, m; cin >> n >> m;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    cout << (solve(n, edges) ? "true" : "false") << endl;
    return 0;
}
