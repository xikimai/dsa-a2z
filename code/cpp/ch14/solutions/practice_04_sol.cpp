#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(int n, vector<vector<int>> updates) {
    vector<long long> diff(n + 1, 0);
    for (auto& u : updates) {
        diff[u[0]] += u[2];
        if (u[1] + 1 <= n) diff[u[1] + 1] -= u[2];
    }
    vector<long long> result(n);
    long long running = 0;
    for (int i = 0; i < n; i++) { running += diff[i]; result[i] = running; }
    return result;
}

int main() {
    int n, q;
    cin >> n >> q;
    vector<vector<int>> updates(q, vector<int>(3));
    for (int i = 0; i < q; i++) cin >> updates[i][0] >> updates[i][1] >> updates[i][2];
    auto result = solve(n, updates);
    for (int i = 0; i < (int)result.size(); i++)
        cout << result[i] << (i < (int)result.size()-1 ? " " : "\n");
    return 0;
}
