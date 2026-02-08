#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& isConnected) {
    int n = isConnected.size();
    vector<bool> visited(n, false);
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            queue<int> q;
            q.push(i);
            visited[i] = true;
            while (!q.empty()) {
                int city = q.front(); q.pop();
                for (int j = 0; j < n; j++) {
                    if (isConnected[city][j] == 1 && !visited[j]) {
                        visited[j] = true;
                        q.push(j);
                    }
                }
            }
            count++;
        }
    }
    return count;
}

int main() {
    int n; cin >> n;
    vector<vector<int>> isConnected(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> isConnected[i][j];
    cout << solve(isConnected) << endl;
    return 0;
}
