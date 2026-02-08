#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size();
    vector<long long> prefix(n + 1, 0);
    for (int i = 0; i < n; i++) prefix[i+1] = prefix[i] + arr[i];
    vector<long long> result;
    for (auto& q : queries) result.push_back(prefix[q[1]+1] - prefix[q[0]]);
    return result;
}

int main() {
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int q; cin >> q;
    vector<vector<int>> queries(q, vector<int>(2));
    for (int i = 0; i < q; i++) cin >> queries[i][0] >> queries[i][1];
    auto result = solve(arr, queries);
    for (int i = 0; i < (int)result.size(); i++)
        cout << result[i] << (i < (int)result.size()-1 ? " " : "\n");
    return 0;
}
