/*
 * Solution: Warmup 4 — Count Inversions (BIT)
 */
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
int solve(vector<int> arr) {
    if (arr.empty()) return 0;
    vector<int> sorted = arr;
    sort(sorted.begin(), sorted.end());
    sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());
    map<int,int> rank;
    for (int i = 0; i < (int)sorted.size(); i++) rank[sorted[i]] = i + 1;
    int maxR = sorted.size();
    vector<int> bit(maxR + 1, 0);
    auto update = [&](int i, int d) { for (; i <= maxR; i += i & (-i)) bit[i] += d; };
    auto prefix = [&](int i) -> int { int s = 0; for (; i > 0; i -= i & (-i)) s += bit[i]; return s; };
    int inv = 0;
    for (int i = arr.size() - 1; i >= 0; i--) {
        int r = rank[arr[i]];
        inv += prefix(r - 1);
        update(r, 1);
    }
    return inv;
}
int main() { return 0; }
