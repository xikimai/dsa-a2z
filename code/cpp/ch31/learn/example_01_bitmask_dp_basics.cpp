/*
 * Example 01: Bitmask DP Basics — Subset Encoding & TSP
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

void enumerateSubsets(int n) {
    for (int mask = 0; mask < (1 << n); mask++) {
        cout << "  mask=";
        for (int b = n - 1; b >= 0; b--) cout << ((mask >> b) & 1);
        cout << " (decimal " << mask << ") -> {";
        bool first = true;
        for (int i = 0; i < n; i++)
            if (mask & (1 << i)) { if (!first) cout << ","; cout << i; first = false; }
        cout << "}" << endl;
    }
}

int tsp(int n, vector<vector<int>>& dist) {
    int INF = INT_MAX / 2;
    int full = (1 << n) - 1;
    vector<vector<int>> dp(1 << n, vector<int>(n, INF));
    dp[1][0] = 0;

    for (int mask = 1; mask <= full; mask++)
        for (int u = 0; u < n; u++) {
            if (dp[mask][u] >= INF) continue;
            if (!(mask & (1 << u))) continue;
            for (int v = 0; v < n; v++) {
                if (mask & (1 << v)) continue;
                int nm = mask | (1 << v);
                dp[nm][v] = min(dp[nm][v], dp[mask][u] + dist[u][v]);
            }
        }

    int ans = INF;
    for (int u = 0; u < n; u++)
        ans = min(ans, dp[full][u] + dist[u][0]);
    return ans;
}

int main() {
    cout << "BITMASK BASICS: Subsets of {0,1,2,3}" << endl;
    enumerateSubsets(4);

    cout << "\nTSP Example:" << endl;
    vector<vector<int>> dist = {{0,10,15,20},{10,0,35,25},{15,35,0,30},{20,25,30,0}};
    cout << "  Min tour cost: " << tsp(4, dist) << endl;  // 80
    return 0;
}
