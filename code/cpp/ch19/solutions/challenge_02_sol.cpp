#include <iostream>
#include <vector>
using namespace std;

bool hasCycle(vector<vector<int>>& adj, int node, vector<int>& state) {
    state[node] = 1; // in progress
    for (int nb : adj[node]) {
        if (state[nb] == 1) return true;
        if (state[nb] == 0 && hasCycle(adj, nb, state)) return true;
    }
    state[node] = 2; // done
    return false;
}

bool solve(int numCourses, vector<vector<int>>& prerequisites) {
    vector<vector<int>> adj(numCourses);
    for (auto& p : prerequisites) {
        adj[p[1]].push_back(p[0]);
    }
    vector<int> state(numCourses, 0);
    for (int c = 0; c < numCourses; c++) {
        if (state[c] == 0) {
            if (hasCycle(adj, c, state)) return false;
        }
    }
    return true;
}

int main() {
    int numCourses, m; cin >> numCourses >> m;
    vector<vector<int>> prereqs(m, vector<int>(2));
    for (int i = 0; i < m; i++) cin >> prereqs[i][0] >> prereqs[i][1];
    cout << (solve(numCourses, prereqs) ? "true" : "false") << endl;
    return 0;
}
