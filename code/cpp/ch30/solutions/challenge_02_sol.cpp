/*
 * Solution: Challenge 2 — Distinct Values in Range (Offline + BIT)
 */
#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;
vector<int> solve(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size();
    vector<int> bit(n + 2, 0);
    auto update = [&](int i, int d) { for (i++; i <= n; i += i & (-i)) bit[i] += d; };
    auto prefix = [&](int i) -> int { int s = 0; for (i++; i > 0; i -= i & (-i)) s += bit[i]; return s; };

    vector<array<int,3>> indexed(queries.size());
    for (int i = 0; i < (int)queries.size(); i++) { indexed[i] = {queries[i][0], queries[i][1], i}; }
    sort(indexed.begin(), indexed.end(), [](auto& a, auto& b) { return a[1] < b[1]; });

    vector<int> results(queries.size());
    unordered_map<int,int> lastSeen;
    int j = 0;
    for (auto& q : indexed) {
        int l = q[0], r = q[1], origIdx = q[2];
        while (j <= r) {
            int val = arr[j];
            if (lastSeen.count(val)) update(lastSeen[val], -1);
            lastSeen[val] = j; update(j, 1); j++;
        }
        results[origIdx] = prefix(r) - (l > 0 ? prefix(l - 1) : 0);
    }
    return results;
}
int main() { return 0; }
