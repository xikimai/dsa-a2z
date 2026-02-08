#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<vector<int>>& adj) {
    vector<vector<int>> clone;
    for (auto& nbrs : adj) {
        clone.push_back(vector<int>(nbrs.begin(), nbrs.end()));
    }
    return clone;
}

int main() {
    int n; cin >> n;
    vector<vector<int>> adj(n);
    for (int i = 0; i < n; i++) {
        int k; cin >> k;
        adj[i].resize(k);
        for (int j = 0; j < k; j++) cin >> adj[i][j];
    }
    auto clone = solve(adj);
    for (int i = 0; i < (int)clone.size(); i++) {
        cout << i << ": [";
        for (int j = 0; j < (int)clone[i].size(); j++) {
            if (j > 0) cout << ", ";
            cout << clone[i][j];
        }
        cout << "]" << endl;
    }
    return 0;
}
