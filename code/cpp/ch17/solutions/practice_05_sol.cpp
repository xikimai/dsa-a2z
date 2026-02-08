/*
 * Solution for Practice 5: K Closest Points to Origin
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Use a max-heap of size k keyed by squared distance.
 *           For each point, push it. If heap exceeds k, pop the farthest.
 *           Sort result by distance ascending.
 * TIME:  O(n log k)
 * SPACE: O(k)
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<vector<int>> points, int k) {
    // Max-heap by squared distance: (dist_sq, x, y)
    auto cmp = [](const tuple<int,int,int>& a, const tuple<int,int,int>& b) {
        return get<0>(a) < get<0>(b);  // max-heap by distance
    };
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, decltype(cmp)> pq(cmp);

    for (auto& p : points) {
        int dist_sq = p[0] * p[0] + p[1] * p[1];
        pq.push({dist_sq, p[0], p[1]});
        if ((int)pq.size() > k) pq.pop();
    }

    vector<vector<int>> result;
    while (!pq.empty()) {
        auto [d, x, y] = pq.top();
        pq.pop();
        result.push_back({x, y});
    }
    // Sort by distance ascending
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0]*a[0] + a[1]*a[1] < b[0]*b[0] + b[1]*b[1];
    });
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, k;
    cin >> n;
    vector<vector<int>> points(n, vector<int>(2));
    for (int i = 0; i < n; i++) cin >> points[i][0] >> points[i][1];
    cin >> k;
    vector<vector<int>> result = solve(points, k);
    for (auto& p : result) cout << p[0] << " " << p[1] << endl;
    return 0;
}
