#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

void dfs(vector<vector<int>>& adj, int node, int target,
         vector<int>& path, vector<vector<int>>& result) {
    if (node == target) {
        result.push_back(path);
        return;
    }
    vector<int> nbrs = adj[node];
    sort(nbrs.begin(), nbrs.end());
    for (int nb : nbrs) {
        path.push_back(nb);
        dfs(adj, nb, target, path, result);
        path.pop_back();
    }
}

vector<vector<int>> solve(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]); // directed
    }
    vector<vector<int>> result;
    vector<int> path = {0};
    dfs(adj, 0, n - 1, path, result);
    sort(result.begin(), result.end());
    return result;
}

int main() {
    int n, m; cin >> n >> m;
    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> edges[i][0] >> edges[i][1];
    auto paths = solve(n, edges);
    for (auto& path : paths) {
        for (int i = 0; i < (int)path.size(); i++) {
            if (i > 0) cout << " -> ";
            cout << path[i];
        }
        cout << endl;
    }
    return 0;
}
