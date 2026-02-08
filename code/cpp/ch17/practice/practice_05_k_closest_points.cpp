/*
 * Practice 5: K Closest Points to Origin
 * =========================================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM:
 *   Given an array of points where points[i] = {xi, yi}, return the k
 *   closest points to the origin (0, 0), sorted by distance ascending.
 *   Use squared Euclidean distance (no need for sqrt).
 *
 * EXAMPLES:
 *   solve({{1,3},{-2,2}}, 1)              -> {{-2,2}}
 *   solve({{3,3},{5,-1},{-2,4}}, 2)       -> {{3,3},{-2,4}}
 *
 * CONSTRAINTS:
 *   - 1 <= k <= points.size() <= 10^4
 *   - -10^4 <= xi, yi <= 10^4
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<vector<int>> points, int k) {
    // TODO: Replace this with your solution
    return {};
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
