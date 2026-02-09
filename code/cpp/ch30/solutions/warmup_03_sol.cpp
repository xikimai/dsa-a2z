/*
 * Solution: Warmup 3 — Prefix Sum with BIT
 */
#include <vector>
using namespace std;
vector<int> solve(vector<int> arr, vector<vector<int>> queries) {
    int n = arr.size();
    vector<int> bit(n + 1, 0);
    auto update = [&](int i, int d) { for (i++; i <= n; i += i & (-i)) bit[i] += d; };
    auto prefix = [&](int i) -> int { int s = 0; for (i++; i > 0; i -= i & (-i)) s += bit[i]; return s; };
    for (int i = 0; i < n; i++) update(i, arr[i]);
    vector<int> res;
    for (auto& q : queries) {
        if (q[0] == 1) res.push_back(prefix(q[1]));
        else update(q[1], q[2]);
    }
    return res;
}
int main() { return 0; }
