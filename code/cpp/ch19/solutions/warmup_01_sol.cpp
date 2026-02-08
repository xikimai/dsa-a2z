#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    for (auto& nbrs : adj) sort(nbrs.begin(), nbrs.end());
    return adj;
}

int main() {
    int n, m; cin >> n >> m;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    auto adj = solve(n, edges);
    for (int i = 0; i < n; i++) {
        cout << i << ": [";
        for (int j = 0; j < (int)adj[i].size(); j++) {
            if (j > 0) cout << ", ";
            cout << adj[i][j];
        }
        cout << "]" << endl;
    }
    return 0;
}
