/*
 * Solution for Warmup 2: Convex Hull
 * Chapter 34: Computational Geometry & Sweep Line
 */
#include <algorithm>
#include <vector>
using namespace std;

long long cross_w2(vector<int>& o, vector<int>& a, vector<int>& b) {
    return (long long)(a[0] - o[0]) * (b[1] - o[1])
         - (long long)(a[1] - o[1]) * (b[0] - o[0]);
}

vector<vector<int>> solve(vector<vector<int>>& points) {
    auto pts = points;
    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());
    int n = pts.size();
    if (n <= 1) return pts;

    vector<vector<int>> hull;
    for (auto& p : pts) {
        while (hull.size() >= 2 && cross_w2(hull[hull.size()-2], hull[hull.size()-1], p) <= 0)
            hull.pop_back();
        hull.push_back(p);
    }
    int lower = hull.size() + 1;
    for (int i = n - 2; i >= 0; i--) {
        while ((int)hull.size() >= lower && cross_w2(hull[hull.size()-2], hull[hull.size()-1], pts[i]) <= 0)
            hull.pop_back();
        hull.push_back(pts[i]);
    }
    hull.pop_back();
    return hull;
}

int main() { return 0; }
